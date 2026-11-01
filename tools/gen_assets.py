"""生成站点用的占位图：头像、favicon、头图。
运行：python scripts/gen_assets.py
"""
import os
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "source", "img")
os.makedirs(OUT, exist_ok=True)

FONT_BOLD = "C:/Windows/Fonts/arialbd.ttf"


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def vertical_gradient(size, stops):
    w, h = size
    img = Image.new("RGB", size)
    d = ImageDraw.Draw(img)
    n = len(stops) - 1
    for y in range(h):
        p = y / max(h - 1, 1) * n
        i = min(int(p), n - 1)
        c = lerp(stops[i], stops[i + 1], p - i)
        d.line([(0, y), (w, y)], fill=c)
    return img


# ---------------- 头像 ----------------
S = 512
avatar = vertical_gradient((S, S), [(23, 48, 92), (42, 82, 152), (76, 122, 178)])

glow = Image.new("RGBA", (S, S), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
gd.ellipse([-S * 0.25, -S * 0.55, S * 1.05, S * 0.75], fill=(255, 255, 255, 16))
avatar = Image.alpha_composite(avatar.convert("RGBA"), glow).convert("RGB")

ad = ImageDraw.Draw(avatar)
font = ImageFont.truetype(FONT_BOLD, 230)
text = "LF"
bbox = ad.textbbox((0, 0), text, font=font)
w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
ad.text(((S - w) / 2 - bbox[0], (S - h) / 2 - bbox[1]), text, font=font, fill=(255, 255, 255))

avatar.save(os.path.join(OUT, "avatar-lf.png"))
avatar.resize((64, 64), Image.LANCZOS).save(os.path.join(OUT, "favicon.png"))

# ---------------- 头图 ----------------
W, H = 1920, 1080
banner = vertical_gradient((W, H), [(12, 26, 34), (28, 53, 62), (44, 83, 100), (26, 44, 58)])

layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ld = ImageDraw.Draw(layer)
# 右上角柔光
ld.ellipse([W * 0.55, -H * 0.45, W * 1.25, H * 0.55], fill=(120, 200, 220, 26))
# 左下角柔光
ld.ellipse([-W * 0.25, H * 0.55, W * 0.45, H * 1.35], fill=(90, 140, 200, 22))
# 细网格
for x in range(0, W, 48):
    ld.line([(x, 0), (x, H)], fill=(255, 255, 255, 8), width=1)
for y in range(0, H, 48):
    ld.line([(0, y), (W, y)], fill=(255, 255, 255, 8), width=1)
# 几条大圆弧
for r in (620, 760, 900):
    ld.arc([W * 0.62 - r, H * 0.5 - r, W * 0.62 + r, H * 0.5 + r],
           start=115, end=245, fill=(255, 255, 255, 20), width=2)

banner = Image.alpha_composite(banner.convert("RGBA"), layer).convert("RGB")
banner.save(os.path.join(OUT, "banner-default.jpg"), quality=88, optimize=True)

for name in ("avatar-lf.png", "favicon.png", "banner-default.jpg"):
    p = os.path.join(OUT, name)
    print(f"{name:12s} {os.path.getsize(p)/1024:8.1f} KB")
