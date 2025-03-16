from PIL import Image, ImageDraw, ImageFont
from dotenv import load_dotenv
import qrcode
import os
import textwrap

# Load environment variables
load_dotenv()

form_id = os.getenv("FORM_ID")
users = os.getenv("USERS", "").split(",")
entry_number = os.getenv("ENTRY")

if not form_id:
    print("Error: FORM_ID environment variable is not set.")
    exit(1)

if not users or users == [""]:
    print("Error: USERS environment variable is not set.")
    exit(1)

if not entry_number:
    print("Error: ENTRY environment variable is not set.")
    exit(1)

QR_FOLDER = "qr_codes"
os.makedirs(QR_FOLDER, exist_ok=True)

FONT_PATH = "./fonts/Roboto-Black.ttf"
FONT_SIZE = 30
LINE_SPACING = 6  # Space between lines

def wrap_text(text, font, max_width):
    """Splits text into lines so it fits within max_width"""
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        test_line = f"{current_line} {word}".strip()
        bbox = font.getbbox(test_line)  # Get text width
        text_width = bbox[2] - bbox[0]

        if text_width <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    return lines

def generate_qr_codes():
    for user in users:
        user = user.strip()
        qr_data = f"https://docs.google.com/forms/d/e/{form_id}/viewform?usp=pp_url&entry.{entry_number}={user.replace(' ', '+')}"
        qr = qrcode.make(qr_data).convert("RGB")

        qr_size = qr.size[0]

        try:
            font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
        except IOError:
            font = ImageFont.load_default()

        # Wrap text to fit QR code width
        lines = wrap_text(user, font, qr_size)

        # Calculate image height dynamically
        text_height = sum(font.getbbox(line)[3] - font.getbbox(line)[1] for line in lines)
        total_text_height = text_height + (LINE_SPACING * (len(lines) - 1))
        img_height = qr_size + total_text_height + 30  # Extra padding

        # Create new image
        image = Image.new("RGB", (qr_size, img_height), "white")
        image.paste(qr, (0, 0, qr_size, qr_size))

        draw = ImageDraw.Draw(image)

        # Draw each line of text
        y_offset = qr_size + 5  # Start below QR code
        for line in lines:
            bbox = font.getbbox(line)
            text_width = bbox[2] - bbox[0]
            text_position = ((qr_size - text_width) // 2, y_offset)
            draw.text(text_position, line, fill="black", font=font)
            y_offset += bbox[3] - bbox[1] + LINE_SPACING  # Move to next line

        # Save image
        filename = os.path.join(QR_FOLDER, f"{user.replace(' ', '_')}.png")
        image.save(filename)
        print(f"✅ QR Code generated for {user}: {filename}")

generate_qr_codes()
