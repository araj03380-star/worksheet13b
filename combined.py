from pyfiglet import Figlet
from PIL import Image, ImageDraw, ImageFont

# Generate ASCII art with pyfiglet
fig = Figlet(font="slant")
banner = fig.renderText("PYTHON PROJECT")

# Create a background image with Pillow
image = Image.new("RGB", (1200, 500), "#14213d")
draw = ImageDraw.Draw(image)

# Use a monospace font so the ASCII art keeps its alignment
font_candidates = [
    "/System/Library/Fonts/Menlo.ttc",
    "/Library/Fonts/Courier New.ttf",
    "DejaVuSansMono.ttf",
]
font = None
for candidate in font_candidates:
    try:
        font = ImageFont.truetype(candidate, 18)
        break
    except OSError:
        pass

if font is None:
    font = ImageFont.load_default()

draw.multiline_text((30, 30), banner, fill="white", font=font, spacing=4)
image.save("python_banner.png")

print("Creative banner generated successfully!")
