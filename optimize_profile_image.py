from PIL import Image
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(base_dir, 'images', 'profile.jpg')
if not os.path.exists(path):
    raise FileNotFoundError(f'Image not found: {path}')

img = Image.open(path)
img.thumbnail((800, 800), Image.LANCZOS)
img = img.convert('RGB')
img.save(path, 'JPEG', quality=80, optimize=True)
print(f'Optimized image saved: {path}')
print(f'Size: {os.path.getsize(path) / 1024:.2f} KB')
