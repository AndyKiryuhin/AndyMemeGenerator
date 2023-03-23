import os
import uuid
from PIL import Image, ImageDraw, ImageFont


class MemeEngine:
    def __init__(self, output_dir):
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def make_meme(self, img_path, text, author, width=500) -> str:
        try:
            # Load image
            img = Image.open(img_path)
        except IOError as e:
            print(f"Error loading image: {e}")
            return None

        # Resize image proportionally with a max width of 500px
        aspect_ratio = img.width / img.height
        new_width = min(width, img.width)
        new_height = int(new_width / aspect_ratio)
        img = img.resize((new_width, new_height), Image.ANTIALIAS)

        try:
            # Add quote body and author
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('./fonts/NotoSans-Black.ttf', size=20)
        except IOError as e:
            print(f"Error loading font: {e}")
            return None

        text_to_draw = f'{text} - {author}'
        text_width, text_height = draw.textsize(text_to_draw, font=font)
        x = (img.width - text_width) / 2
        y = (img.height - text_height) / 2
        draw.text((x, y), text_to_draw, font=font, fill='white')

        # Save manipulated image
        output_path = os.path.join(self.output_dir, f'{uuid.uuid4()}.jpeg')
        try:
            img.save(output_path, 'JPEG')
        except IOError as e:
            print(f"Error saving manipulated image: {e}")
            return None

        return output_path
