from PIL import Image, ImageDraw, ImageFont
from dotenv import load_dotenv
import qrcode
import os

# Load environment variables
load_dotenv()

form_id = os.getenv("FORM_ID")
users = os.getenv("USERS", "").split(",")

if not form_id:
    print("Error: FORM_ID environment variable is not set.")
    exit(1)

if not users or users == [""]:
    print("Error: USERS environment variable is not set.")
    exit(1)

QR_FOLDER = "qr_codes"
os.makedirs(QR_FOLDER, exist_ok=True)

FONT_PATH = "/usr/share/fonts/TTF/DejaVuSans-Bold.ttf"
FONT_SIZE = 30

def generate_qr_codes():
    for user in users:
        user = user.strip()
        qr_data = f"https://docs.google.com/forms/d/e/{form_id}/viewform?usp=pp_url&entry.898992391={user.replace(' ', '+')}"
        qr = qrcode.make(qr_data).convert("RGB")

        qr_size = qr.size[0]
        img_height = qr_size + 50
        image = Image.new("RGB", (qr_size, img_height), "white")
        image.paste(qr, (0, 0, qr_size, qr_size))

        draw = ImageDraw.Draw(image)
        try:
            font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
        except IOError:
            font = ImageFont.load_default()

        bbox = draw.textbbox((0, 0), user, font=font)
        text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
        text_position = ((qr_size - text_width) // 2, qr_size + 5)
        draw.text(text_position, user, fill="black", font=font)

        filename = os.path.join(QR_FOLDER, f"{user.replace(' ', '_')}.png")
        image.save(filename)
        print(f"✅ QR Code generated for {user}: {filename}")

generate_qr_codes()

