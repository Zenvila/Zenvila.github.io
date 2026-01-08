#!/usr/bin/env python3
"""
Smart migration script for Hashnode posts to Hugo content/posts
- Assigns dates: 2 posts per month starting Jan 2025
- Adds featured images based on content keywords
- Processes and moves files
"""

import os
import re
from pathlib import Path
from datetime import datetime, timedelta

source_dir = Path("hashnode_posts_md")
dest_dir = Path("content/posts")

def generate_title(filename):
    """Convert filename to title case"""
    return filename.replace('-', ' ').replace('_', ' ').title()

def get_featured_image(title, content):
    """Generate featured image URL based on title and content"""
    title_lower = title.lower()
    content_lower = content.lower()
    
    # Check for Linux-related content
    if any(keyword in title_lower or keyword in content_lower for keyword in ['linux', 'arch', 'ubuntu', 'debian', 'kernel', 'systemd']):
        return "https://source.unsplash.com/1600x900/?linux,server"
    
    # Check for Docker/Kubernetes
    if any(keyword in title_lower or keyword in content_lower for keyword in ['docker', 'kubernetes', 'container', 'swarm']):
        return "https://source.unsplash.com/1600x900/?docker,container"
    
    # Check for AI/ML
    if any(keyword in title_lower or keyword in content_lower for keyword in ['ai', 'machine learning', 'neural', 'tensorflow', 'pytorch', 'ml']):
        return "https://source.unsplash.com/1600x900/?ai,machine-learning"
    
    # Check for networking
    if any(keyword in title_lower or keyword in content_lower for keyword in ['network', 'ssh', 'ftp', 'http', 'tcp', 'ip']):
        return "https://source.unsplash.com/1600x900/?network,server"
    
    # Default tech/coding image
    return "https://source.unsplash.com/1600x900/?tech,coding"

def process_file(md_file, post_index):
    """Process a single markdown file"""
    # Read the file
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Generate title from filename
    filename = md_file.stem
    title = generate_title(filename)
    
    # Calculate date: 2 posts per month starting Jan 2025
    month = ((post_index - 1) // 2) + 1
    day = ((post_index - 1) % 2) + 1
    date = datetime(2025, month, day)
    date_str = date.strftime("%Y-%m-%d")
    
    # Get featured image
    featured_image = get_featured_image(title, content)
    
    # Generate front matter
    front_matter = f'''---
title: "{title}"
date: {date_str}
draft: false
layout: "article"
tags: ["migrated"]
featuredImage: "{featured_image}"
---

'''
    
    # Combine front matter with content
    new_content = front_matter + content
    
    # Write to destination
    dest_file = dest_dir / md_file.name
    with open(dest_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    # Delete original
    md_file.unlink()
    
    return title, date_str, featured_image

def main():
    """Main migration function"""
    # Ensure destination exists
    dest_dir.mkdir(parents=True, exist_ok=True)
    
    # Get all .md files
    md_files = sorted(list(source_dir.glob("*.md")))
    
    if not md_files:
        print("No markdown files found in hashnode_posts_md/")
        return
    
    print(f"Found {len(md_files)} markdown files to process\n")
    
    # Process each file
    for index, md_file in enumerate(md_files, start=1):
        title, date_str, featured_image = process_file(md_file, index)
        print(f"[{index}/{len(md_files)}] Processed: {md_file.name}")
        print(f"  Title: {title}")
        print(f"  Date: {date_str}")
        print(f"  Image: {featured_image[:50]}...")
        print()
    
    # Verify
    remaining = len(list(source_dir.glob("*.md")))
    migrated = len(list(dest_dir.glob("*.md")))
    
    print(f"\n✅ Migration complete!")
    print(f"  - Processed: {len(md_files)} files")
    print(f"  - Remaining in source: {remaining}")
    print(f"  - Total posts in content/posts/: {migrated}")

if __name__ == "__main__":
    main()

