"""Export Pioneer logo assets with transparent background."""
from pathlib import Path

from PIL import Image, ImageChops

SRC = Path(__file__).resolve().parents[1] / "website" / "static" / "website" / "images" / "pioneer-logo-source.png"
OUT = Path(__file__).resolve().parents[1] / "website" / "static" / "website" / "images"


def trim(im: Image.Image) -> Image.Image:
    bg = Image.new("RGBA", im.size, (0, 0, 0, 0))
    bbox = ImageChops.difference(im, bg).getbbox()
    return im.crop(bbox) if bbox else im


def white_transparent(img: Image.Image, threshold: int = 232) -> Image.Image:
    px = img.load()
    for y in range(img.height):
        for x in range(img.width):
            r, g, b, a = px[x, y]
            luminance = 0.299 * r + 0.587 * g + 0.114 * b
            if luminance >= threshold:
                px[x, y] = (255, 255, 255, 0)
    return img


def export_logo(src: Path) -> None:
    raw = Image.open(src).convert("RGBA")
    scale = 2
    raw = raw.resize((raw.width * scale, raw.height * scale), Image.Resampling.LANCZOS)
    img = white_transparent(raw)
    img = trim(img)
    OUT.mkdir(parents=True, exist_ok=True)
    img.save(OUT / "pioneer-logo.png")

    w, h = img.size
    icon = trim(img.crop((0, 0, w, int(h * 0.36))))
    icon.save(OUT / "pioneer-icon.png")

    mark = trim(img.crop((int(w * 0.02), 0, int(w * 0.98), int(h * 0.34))))
    mark_hd = mark.resize((mark.width * 2, mark.height * 2), Image.Resampling.LANCZOS)
    mark_hd.save(OUT / "pioneer-hero-mark.png")

    print("pioneer-logo.png", img.size)
    print("pioneer-icon.png", icon.size)
    print("pioneer-hero-mark.png", mark_hd.size)


if __name__ == "__main__":
    export_logo(SRC)
