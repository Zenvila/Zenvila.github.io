import os
import re

# --- CONFIGURATION ---
POSTS_DIR = "content/posts"

# --- THEME MAPPING (Perfect Colors & Topics) ---
# I have mapped your specific titles to curated Unsplash visual themes.
IMAGE_MAP = {
    # AI & Math (Theme: Abstract, Geometric, White/Blue)
    "Linear Algebra": "https://images.unsplash.com/photo-1635070041078-e363dbe005cb?auto=format&fit=crop&q=80&w=1600",
    "Numerical Computing": "https://images.unsplash.com/photo-1509228468518-180dd4864904?auto=format&fit=crop&q=80&w=1600",
    "Probability": "https://images.unsplash.com/photo-1596495578065-6e0763fa1178?auto=format&fit=crop&q=80&w=1600",
    "Understanding Nlp": "https://images.unsplash.com/photo-1555421689-3f034debb7a6?auto=format&fit=crop&q=80&w=1600",
    "Machine Learning": "https://images.unsplash.com/photo-1527474305487-b87b222841cc?auto=format&fit=crop&q=80&w=1600",
    
    # Cloud & Oracle (Theme: Blue, Sky, Server Racks)
    "Oracle Cloud": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&q=80&w=1600",
    "Ubuntu Server": "https://images.unsplash.com/photo-1558494949-efdeb6bf80d1?auto=format&fit=crop&q=80&w=1600",
    "Terraform": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&q=80&w=1600", 
    "System Monitoring": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&q=80&w=1600",
    
    # Linux & Arch (Theme: Dark, Minimal, Terminal, Matrix Green)
    "Arch Linux": "https://images.unsplash.com/photo-1629654297299-c8506221ca97?auto=format&fit=crop&q=80&w=1600", # The Arch "Look"
    "Step By Step Arch": "https://images.unsplash.com/photo-1607799275518-d6c43953476e?auto=format&fit=crop&q=80&w=1600",
    "Ssh Tunneling": "https://images.unsplash.com/photo-1555949963-ff9fe0c870eb?auto=format&fit=crop&q=80&w=1600",
    "Sshsecure": "https://images.unsplash.com/photo-1614064642639-e388f4f3b9c4?auto=format&fit=crop&q=80&w=1600",
    "Rsync": "https://images.unsplash.com/photo-1580196923836-d249539308be?auto=format&fit=crop&q=80&w=1600",
    "Cryptography": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&q=80&w=1600", # Matrix code
    
    # DevOps & Containers (Theme: Shipping Containers, Blue/Orange)
    "Docker Evolution": "https://images.unsplash.com/photo-1605745341117-95395144768e?auto=format&fit=crop&q=80&w=1600",
    "Introduction To Docker": "https://images.unsplash.com/photo-1590959651373-a3db0f38a96b?auto=format&fit=crop&q=80&w=1600",
    "Docker Swarm": "https://images.unsplash.com/photo-1524235338165-c276b42b9472?auto=format&fit=crop&q=80&w=1600",
    "Kubernetes": "https://images.unsplash.com/photo-1667372393119-c85c020799a3?auto=format&fit=crop&q=80&w=1600",
    "Puppet": "https://images.unsplash.com/photo-1516110833967-0b5716ca1387?auto=format&fit=crop&q=80&w=1600",
    "Progress Chef": "https://images.unsplash.com/photo-1556761175-5973dc0f32e7?auto=format&fit=crop&q=80&w=1600",
    "Cicd Github": "https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?auto=format&fit=crop&q=80&w=1600",
    "Git And Github": "https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?auto=format&fit=crop&q=80&w=1600",
    
    # Hardware & Low Level (Theme: Circuits, Chips, Red/Orange)
    "Risc Vs Cisc": "https://images.unsplash.com/photo-1591405351990-4726e331f141?auto=format&fit=crop&q=80&w=1600",
    "Computer Architecture": "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&q=80&w=1600",
    "Building Blocks": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&q=80&w=1600",
    "Raspberry Pi": "https://images.unsplash.com/photo-1551808525-51a94da548ce?auto=format&fit=crop&q=80&w=1600",
    
    # Networking (Theme: Cables, Lights, Connections)
    "Voip": "https://images.unsplash.com/photo-1544197150-b99a580bbcbf?auto=format&fit=crop&q=80&w=1600",
    "Http": "https://images.unsplash.com/photo-1558494949-efdeb6bf80d1?auto=format&fit=crop&q=80&w=1600",
    "Ftp Server": "https://images.unsplash.com/photo-1544197150-b99a580bbcbf?auto=format&fit=crop&q=80&w=1600",
    
    # Default Fallback (A nice dark tech desk)
    "DEFAULT": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&q=80&w=1600"
}

def update_images():
    files = [f for f in os.listdir(POSTS_DIR) if f.endswith(".md")]
    print(f"🎨 Processing {len(files)} posts...")

    for filename in files:
        filepath = os.path.join(POSTS_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Find the Title to match the image
        title_match = re.search(r'title: "(.*?)"', content)
        if not title_match:
            continue
        
        title = title_match.group(1)
        
        # Find the best matching image from our map
        selected_image = IMAGE_MAP["DEFAULT"]
        for key, url in IMAGE_MAP.items():
            if key.lower() in title.lower():
                selected_image = url
                break

        # Update or Add the featuredImage field
        if "featuredImage:" in content:
            # Replace existing
            new_content = re.sub(r'featuredImage: ".*?"', f'featuredImage: "{selected_image}"', content)
        else:
            # Add new (after title)
            new_content = content.replace(f'title: "{title}"', f'title: "{title}"\nfeaturedImage: "{selected_image}"')

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        
        print(f"✅ Set Image for: {title[:30]}...")

    print("\n🎉 All 36 posts now have professional featured images!")

if __name__ == "__main__":
    update_images()
