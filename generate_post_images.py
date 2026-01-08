#!/usr/bin/env python3
"""
Generate colorful, computer-generated featured images for blog posts
Based on post titles with unique color schemes for each
"""

import os
import re
import hashlib
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import colorsys
import random

# Configuration
POSTS_DIR = Path("content/posts")
OUTPUT_DIR = Path("static/images/posts")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Image dimensions (Hugo/Blowfish recommended: 1200x630 for social sharing)
WIDTH = 1200
HEIGHT = 630

# Color palettes (cool, modern colors)
COLOR_PALETTES = [
    # Blue/Purple gradients
    [(0, 102, 204), (51, 51, 153), (102, 0, 204)],
    [(0, 153, 255), (0, 102, 204), (0, 51, 153)],
    [(102, 0, 204), (153, 51, 255), (204, 102, 255)],
    # Teal/Cyan gradients
    [(0, 153, 153), (0, 204, 204), (51, 255, 255)],
    [(0, 102, 102), (0, 153, 153), (0, 204, 204)],
    # Green/Blue gradients
    [(0, 153, 76), (0, 204, 102), (51, 255, 153)],
    [(0, 102, 153), (0, 153, 204), (51, 204, 255)],
    # Purple/Pink gradients
    [(102, 0, 153), (153, 51, 204), (204, 102, 255)],
    [(153, 0, 102), (204, 51, 153), (255, 102, 204)],
    # Orange/Red gradients
    [(204, 102, 0), (255, 153, 51), (255, 204, 102)],
    [(153, 0, 0), (204, 51, 51), (255, 102, 102)],
    # Dark Blue/Indigo
    [(25, 25, 112), (72, 61, 139), (106, 90, 205)],
    # Cyan/Blue
    [(0, 191, 255), (30, 144, 255), (70, 130, 180)],
    # Magenta/Purple
    [(186, 85, 211), (147, 112, 219), (138, 43, 226)],
    # Emerald/Teal
    [(0, 206, 209), (64, 224, 208), (72, 209, 204)],
    # Slate/Gray-Blue
    [(112, 128, 144), (119, 136, 153), (176, 196, 222)],
]

def get_palette_for_title(title):
    """Get a consistent color palette for a title using hash"""
    hash_obj = hashlib.md5(title.encode())
    hash_int = int(hash_obj.hexdigest(), 16)
    return COLOR_PALETTES[hash_int % len(COLOR_PALETTES)]

def create_gradient_background(width, height, colors):
    """Create a gradient background with multiple colors"""
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    
    # Create vertical gradient
    num_colors = len(colors)
    for y in range(height):
        # Determine which color segment we're in
        segment = int((y / height) * (num_colors - 1))
        if segment >= num_colors - 1:
            segment = num_colors - 2
        
        # Interpolate between two colors
        t = (y / height) * (num_colors - 1) - segment
        c1 = colors[segment]
        c2 = colors[segment + 1]
        
        r = int(c1[0] * (1 - t) + c2[0] * t)
        g = int(c1[1] * (1 - t) + c2[1] * t)
        b = int(c1[2] * (1 - t) + c2[2] * t)
        
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    return img

def add_geometric_shapes(draw, width, height):
    """Add cool geometric shapes for visual interest"""
    # Add some circles
    for _ in range(3):
        x = random.randint(0, width)
        y = random.randint(0, height)
        radius = random.randint(50, 200)
        alpha = random.randint(30, 80)
        # Draw semi-transparent circle outline
        bbox = [x - radius, y - radius, x + radius, y + radius]
        draw.ellipse(bbox, outline=(255, 255, 255, alpha), width=3)
    
    # Add some lines
    for _ in range(2):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
        draw.line([(x1, y1), (x2, y2)], fill=(255, 255, 255, 50), width=2)

def wrap_text(text, max_width, font):
    """Wrap text to fit within max_width"""
    words = text.split()
    lines = []
    current_line = []
    
    for word in words:
        test_line = ' '.join(current_line + [word])
        bbox = font.getbbox(test_line)
        if bbox[2] - bbox[0] <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(' '.join(current_line))
            current_line = [word]
    
    if current_line:
        lines.append(' '.join(current_line))
    
    return lines

def generate_post_image(title, output_path):
    """Generate a featured image for a post"""
    # Get color palette for this title
    palette = get_palette_for_title(title)
    
    # Create gradient background
    img = create_gradient_background(WIDTH, HEIGHT, palette)
    draw = ImageDraw.Draw(img, 'RGBA')
    
    # Add geometric shapes
    add_geometric_shapes(draw, WIDTH, HEIGHT)
    
    # Try to load a nice font, fallback to default
    try:
        # Try to use a system font
        font_large = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 72)
        font_medium = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 48)
    except:
        try:
            font_large = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 72)
            font_medium = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 48)
        except:
            # Fallback to default font
            font_large = ImageFont.load_default()
            font_medium = ImageFont.load_default()
    
    # Prepare title text (clean it up)
    title_clean = title.replace(" For ", " for ").replace(" And ", " and ")
    title_clean = title_clean.replace(" Vs ", " vs ").replace(" Voip ", " VoIP ")
    title_clean = title_clean.replace(" Ssh ", " SSH ").replace(" Ftp ", " FTP ")
    title_clean = title_clean.replace(" Http", " HTTP").replace(" Oci ", " OCI ")
    title_clean = title_clean.replace(" Ai ", " AI ").replace(" Nlp ", " NLP ")
    title_clean = title_clean.replace(" Cicd ", " CI/CD ")
    
    # Wrap text
    max_text_width = WIDTH - 200  # Margins
    lines = wrap_text(title_clean, max_text_width, font_large)
    
    # Calculate text position (centered)
    line_height = 90
    total_height = len(lines) * line_height
    start_y = (HEIGHT - total_height) // 2
    
    # Draw title text with shadow effect
    for i, line in enumerate(lines):
        y = start_y + i * line_height
        
        # Draw shadow (slightly offset)
        shadow_offset = 4
        draw.text((WIDTH//2 + shadow_offset, y + shadow_offset), line, 
                 font=font_large, fill=(0, 0, 0, 100), anchor="mm")
        
        # Draw main text (white)
        draw.text((WIDTH//2, y), line, 
                 font=font_large, fill=(255, 255, 255, 255), anchor="mm")
    
    # Add a subtle overlay pattern
    overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    
    # Add diagonal lines pattern
    for i in range(0, WIDTH + HEIGHT, 30):
        overlay_draw.line([(i, 0), (i - HEIGHT, HEIGHT)], 
                          fill=(255, 255, 255, 5), width=1)
    
    # Composite overlay
    img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')
    
    # Save image
    img.save(output_path, 'JPEG', quality=90, optimize=True)
    print(f"✅ Generated: {output_path.name}")

def process_all_posts():
    """Process all posts and generate images"""
    posts = []
    
    # Read all posts
    for md_file in sorted(POSTS_DIR.glob("*.md")):
        if md_file.name == "_index.md":
            continue
        
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract title
        parts = content.split('---', 2)
        if len(parts) < 3:
            continue
        
        front_matter = parts[1]
        title_match = re.search(r'^title:\s*"([^"]+)"', front_matter, re.MULTILINE)
        
        if not title_match:
            continue
        
        title = title_match.group(1)
        
        # Generate slug from filename
        slug = md_file.stem
        image_filename = f"{slug}.jpeg"
        image_path = OUTPUT_DIR / image_filename
        
        # Generate image
        generate_post_image(title, image_path)
        
        posts.append({
            'file': md_file,
            'title': title,
            'slug': slug,
            'image_path': image_path,
            'image_url': f"https://zenvila.github.io/images/posts/{image_filename}"
        })
    
    return posts

if __name__ == "__main__":
    print("🎨 Generating featured images for all posts...\n")
    print("=" * 80)
    
    posts = process_all_posts()
    
    print("=" * 80)
    print(f"\n✅ Generated {len(posts)} featured images!")
    print(f"📁 Images saved to: {OUTPUT_DIR}")
    print(f"\n💡 Next step: Run update_post_images.py to add these images to posts")

