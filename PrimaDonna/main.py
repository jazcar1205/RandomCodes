from PIL import Image

# ---------- SETTINGS ----------
SOURCE_IMAGE = "PD_.png"
OVERLAY_IMAGE = "Additions.png"
OUTPUT_IMAGE = "Remix.png"

NEW_COLOR = (8, 148, 219)
TOLERANCE = 10  # how close a color must be to match
# -------------------------------


def color_close(c1, c2, tolerance):
    """Check if two RGB colors are within tolerance range."""
    return all(abs(a - b) <= tolerance for a, b in zip(c1, c2))


def recolor_image(img, target_colors, new_color, tolerance):
    """Recolor pixels that match target colors within tolerance."""
    pixels = img.load()
    width, height = img.size

    for y in range(height):
        for x in range(width):
            current_color = pixels[x, y]

            for target in target_colors:
                if color_close(current_color, target, tolerance):
                    pixels[x, y] = new_color
                    break  # stop checking once matched


def center_paste(base_img, overlay_img):
    """Paste overlay image in the center."""
    x = (base_img.width - overlay_img.width) // 2
    y = (base_img.height - overlay_img.height) // 2
    base_img.paste(overlay_img, (x, y), overlay_img)


# ---------- MAIN PROCESS ----------

# Load base image
img = Image.open(SOURCE_IMAGE).convert("RGB")

# Your original color groups
BG_COLORS = BG_1 + BG_2  # combine both sections

# Recolor
recolor_image(img, BG_COLORS, NEW_COLOR, TOLERANCE)

# Convert for transparency
img = img.convert("RGBA")

# Load overlay
overlay = Image.open(OVERLAY_IMAGE).convert("RGBA")

# Center and paste
center_paste(img, overlay)

# Save final
img.save(OUTPUT_IMAGE)

print("✅ Image successfully processed and saved as", OUTPUT_IMAGE)
