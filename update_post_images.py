#!/usr/bin/env python3
"""
Update all post markdown files with their generated featured images
"""

import re
from pathlib import Path

POSTS_DIR = Path("content/posts")
IMAGES_DIR = Path("static/images/posts")

def update_post_featured_image(post_file, image_url):
    """Update or add featuredimage to post front matter"""
    with open(post_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split front matter and body
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False
    
    front_matter = parts[1]
    body = parts[2]
    
    # Check if featureimage already exists
    if re.search(r'^featureimage:', front_matter, re.MULTILINE | re.IGNORECASE):
        # Update existing featureimage
        front_matter = re.sub(
            r'^featureimage:.*$',
            f'featureimage: "{image_url}"',
            front_matter,
            flags=re.MULTILINE | re.IGNORECASE
        )
    else:
        # Add featureimage after date
        if re.search(r'^date:', front_matter, re.MULTILINE):
            front_matter = re.sub(
                r'^(date:.*)$',
                r'\1\nfeatureimage: "' + image_url + '"',
                front_matter,
                flags=re.MULTILINE
            )
        else:
            # Add after title if no date
            if re.search(r'^title:', front_matter, re.MULTILINE):
                front_matter = re.sub(
                    r'^(title:.*)$',
                    r'\1\nfeatureimage: "' + image_url + '"',
                    front_matter,
                    flags=re.MULTILINE
                )
            else:
                # Just append at the end
                front_matter = front_matter.rstrip() + f'\nfeatureimage: "{image_url}"'
    
    # Reconstruct content
    new_content = f"---\n{front_matter}\n---\n{body}"
    
    # Write back
    with open(post_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True

def main():
    """Update all posts with their featured images"""
    updated = 0
    skipped = 0
    
    print("📝 Updating posts with featured images...\n")
    print("=" * 80)
    
    for md_file in sorted(POSTS_DIR.glob("*.md")):
        if md_file.name == "_index.md":
            continue
        
        slug = md_file.stem
        image_filename = f"{slug}.jpeg"
        image_path = IMAGES_DIR / image_filename
        
        # Check if image exists
        if not image_path.exists():
            print(f"⚠️  Image not found: {image_filename} (skipping {md_file.name})")
            skipped += 1
            continue
        
        image_url = f"https://zenvila.github.io/images/posts/{image_filename}"
        
        if update_post_featured_image(md_file, image_url):
            print(f"✅ Updated: {md_file.name}")
            updated += 1
        else:
            print(f"⚠️  Failed to update: {md_file.name}")
            skipped += 1
    
    print("=" * 80)
    print(f"\n✅ Updated {updated} posts")
    if skipped > 0:
        print(f"⚠️  Skipped {skipped} posts (no image found)")

if __name__ == "__main__":
    main()

