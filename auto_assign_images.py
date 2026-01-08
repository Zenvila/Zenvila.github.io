#!/usr/bin/env python3
"""
Auto-assign images to projects based on filename similarity.
Matches images from project_uploads/ to projects in content/projects/
"""

import os
import re
import shutil
from pathlib import Path
from difflib import SequenceMatcher

def similarity(a, b):
    """Calculate similarity ratio between two strings."""
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def slugify(text):
    """Convert text to URL-friendly slug."""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')

def extract_front_matter(content):
    """Extract front matter from markdown content."""
    if not content.startswith('---'):
        return None, content
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        return None, content
    
    return parts[1], parts[2]

def update_front_matter(front_matter, new_image_path):
    """Update or add featureimage in front matter."""
    # Check if featureimage already exists (case insensitive)
    if re.search(r'^featureimage:', front_matter, re.MULTILINE | re.IGNORECASE):
        # Update existing
        front_matter = re.sub(
            r'^featureimage:.*$',
            f'featureimage: "{new_image_path}"',
            front_matter,
            flags=re.MULTILINE | re.IGNORECASE
        )
    else:
        # Add new featureimage before the closing ---
        # Find a good place to insert (after date or tags)
        if re.search(r'^date:', front_matter, re.MULTILINE):
            front_matter = re.sub(
                r'^(date:.*)$',
                r'\1\nfeatureimage: "' + new_image_path + '"',
                front_matter,
                flags=re.MULTILINE
            )
        elif re.search(r'^tags:', front_matter, re.MULTILINE):
            front_matter = re.sub(
                r'^(tags:.*)$',
                r'\1\nfeatureimage: "' + new_image_path + '"',
                front_matter,
                flags=re.MULTILINE
            )
        else:
            # Add at the end of front matter
            front_matter = front_matter.rstrip() + f'\nfeatureimage: "{new_image_path}"'
    
    return front_matter

def main():
    # Setup paths
    project_root = Path(__file__).parent
    projects_dir = project_root / "content" / "projects"
    uploads_dir = project_root / "project_uploads"
    target_dir = project_root / "static" / "images" / "projects"
    
    # Create target directory if it doesn't exist
    target_dir.mkdir(parents=True, exist_ok=True)
    
    # Check if uploads directory exists
    if not uploads_dir.exists():
        print(f"❌ Error: {uploads_dir} directory not found!")
        return
    
    # Read all project markdown files
    project_files = list(projects_dir.glob("*.md"))
    if not project_files:
        print(f"❌ No project files found in {projects_dir}")
        return
    
    # Read all image files
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.webp'}
    image_files = [f for f in uploads_dir.iterdir() 
                   if f.is_file() and f.suffix.lower() in image_extensions]
    
    if not image_files:
        print(f"❌ No image files found in {uploads_dir}")
        return
    
    print(f"📁 Found {len(project_files)} projects and {len(image_files)} images\n")
    
    # Extract project titles and create matching data
    projects_data = []
    for project_file in project_files:
        if project_file.name == "_index.md":
            continue
        
        with open(project_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        front_matter, body = extract_front_matter(content)
        if not front_matter:
            continue
        
        # Extract title
        title_match = re.search(r'^title:\s*"([^"]+)"', front_matter, re.MULTILINE)
        if not title_match:
            continue
        
        title = title_match.group(1)
        slug = slugify(title)
        
        projects_data.append({
            'file': project_file,
            'title': title,
            'slug': slug,
            'front_matter': front_matter,
            'body': body,
            'content': content
        })
    
    # Match images to projects
    matches = []
    used_images = set()
    
    for project in projects_data:
        best_match = None
        best_score = 0
        best_image = None
        
        for image_file in image_files:
            if image_file in used_images:
                continue
            
            image_name = image_file.stem.lower()
            project_title = project['title'].lower()
            project_slug = project['slug'].lower()
            
            # Calculate similarity
            score1 = similarity(image_name, project_title)
            score2 = similarity(image_name, project_slug)
            
            # Also check if slug is in image name or vice versa
            if project_slug in image_name or image_name in project_slug:
                score3 = 0.9
            else:
                score3 = 0
            
            max_score = max(score1, score2, score3)
            
            if max_score > best_score:
                best_score = max_score
                best_match = image_file
                best_image = image_file
        
        # Use threshold of 0.3 for matching (pretty lenient)
        if best_score >= 0.3 and best_match:
            matches.append({
                'project': project,
                'image': best_match,
                'score': best_score
            })
            used_images.add(best_match)
    
    # Process matches
    print("🖼️  Matching Results:\n")
    print("=" * 80)
    
    for match in matches:
        project = match['project']
        image = match['image']
        score = match['score']
        
        # Determine new filename
        new_filename = f"{project['slug']}{image.suffix.lower()}"
        target_path = target_dir / new_filename
        image_path = f"images/projects/{new_filename}"
        
        # Move and rename image
        shutil.copy2(image, target_path)
        print(f"✅ {project['title'][:50]:<50} → {new_filename} (score: {score:.2f})")
        
        # Update markdown file
        updated_front_matter = update_front_matter(project['front_matter'], image_path)
        new_content = f"---\n{updated_front_matter}\n---\n{project['body']}"
        
        with open(project['file'], 'w', encoding='utf-8') as f:
            f.write(new_content)
    
    print("=" * 80)
    print(f"\n✅ Processed {len(matches)} matches")
    print(f"📁 Images moved to: {target_dir}")
    print(f"📝 Project files updated in: {projects_dir}")
    
    # List unmatched images
    unmatched = [img for img in image_files if img not in used_images]
    if unmatched:
        print(f"\n⚠️  {len(unmatched)} unmatched images:")
        for img in unmatched:
            print(f"   - {img.name}")

if __name__ == "__main__":
    main()

