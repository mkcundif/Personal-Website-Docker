from PIL import Image
from pathlib import Path

p = Path('images') / 'photo.jpg'
if not p.exists():
    raise SystemExit(f'Error: {p} not found')

with Image.open(p) as img:
    img = img.convert('RGB')
    w, h = img.size
    m = min(w, h)
    left = (w - m) // 2
    top = (h - m) // 2
    img = img.crop((left, top, left + m, top + m))
    img = img.resize((400, 400), Image.LANCZOS)
    img.save(p, format='JPEG', quality=85, optimize=True)
    print('Saved', p)
