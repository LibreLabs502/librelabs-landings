#!/usr/bin/env python3
"""Genera los assets web optimizados de las landings (héroes, OG y favicons).

Se ejecuta desde la raíz del repo:
    python scripts/generar_assets.py

Requiere Pillow. Los favicons se recortan de la región del logo de las
imagenes *_icon.jpg (que contienen el icono oficial de cada producto).
"""
import os

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "images")


def open_img(name):
    return Image.open(os.path.join(IMG, name)).convert("RGB")


def save_webp(img, path, q=80):
    img.save(path, "WEBP", quality=q, method=6)


def save_jpg(img, path, q=82):
    img.save(path, "JPEG", quality=q, optimize=True, progressive=True)


def main():
    # --- Héroes optimizados ---
    hero = open_img("libredrop.jpg")
    save_webp(hero, os.path.join(IMG, "libredrop-hero.webp"), 80)
    save_jpg(hero.resize((1407, 768)), os.path.join(IMG, "libredrop-hero.jpg"), 80)

    hero_cloud = open_img("libredrop_cloud.jpg")
    save_webp(hero_cloud, os.path.join(IMG, "libredrop-cloud-hero.webp"), 80)
    save_jpg(hero_cloud.resize((1407, 768)), os.path.join(IMG, "libredrop-cloud-hero.jpg"), 80)

    # --- OG 1200x630 (conserva el ancho completo) ---
    def make_og(src, dst):
        img = open_img(src)
        w, h = img.size
        ratio = 1200 / w
        img = img.resize((1200, int(h * ratio)), Image.LANCZOS)
        target = (1200, 630)
        if img.size[1] >= 630:
            top = (img.size[1] - 630) // 2
            img = img.crop((0, top, 1200, top + 630))
        else:
            canvas = Image.new("RGB", target, (255, 255, 255))
            canvas.paste(img, (0, (630 - img.size[1]) // 2))
            img = canvas
        save_jpg(img, dst, 85)

    make_og("libredrop_icon.jpg", os.path.join(IMG, "libredrop-og.jpg"))
    make_og("libredrop_cloud_icon.jpg", os.path.join(IMG, "libredrop-cloud-og.jpg"))

    # --- Favicons desde la región del logo de las *_icon ---
    def make_favicons(src, center, side, out_dir):
        img = open_img(src)
        w, h = img.size
        left = max(0, center[0] - side // 2)
        top = max(0, center[1] - side // 2)
        sq = img.crop((left, top, min(w, left + side), min(h, top + side)))
        sqside = max(sq.size)
        pad = Image.new("RGB", (sqside, sqside), (255, 255, 255))
        pad.paste(sq, ((sqside - sq.size[0]) // 2, (sqside - sq.size[1]) // 2))
        os.makedirs(out_dir, exist_ok=True)
        for size in (32, 64, 180, 512):
            pad.resize((size, size), Image.LANCZOS).save(
                os.path.join(out_dir, f"icon-{size}.png"), "PNG", optimize=True
            )

    # Centro del logo detectado en cada screenshot (región superior).
    make_favicons("libredrop_icon.jpg", (703, 131), 300, os.path.join(ROOT, "libredrop"))
    make_favicons("libredrop_cloud_icon.jpg", (703, 135), 300, os.path.join(ROOT, "libredrop-cloud"))

    # --- Héroes con tinte suave (fondos de sección) ---
    def tint(src, dst, color=(12, 80, 76), alpha=0.06):
        img = open_img(src)
        overlay = Image.new("RGB", img.size, color)
        img = Image.blend(img, overlay, alpha)
        save_webp(img, dst, 72)
        save_jpg(img, dst.replace(".webp", ".jpg"), 76)

    tint("libredrop.jpg", os.path.join(IMG, "libredrop-hero-soft.webp"))
    tint("libredrop_cloud.jpg", os.path.join(IMG, "libredrop-cloud-hero-soft.webp"))

    print("OK: assets regenerados en", IMG)


if __name__ == "__main__":
    main()