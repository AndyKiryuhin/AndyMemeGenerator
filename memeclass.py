"""MemeEngine module to generate meme images with text.

This module provides a MemeEngine class that can create memes by combining
images with given text and author information, while resizing and centering
the text.
"""

import os
import random
import uuid
import textwrap
from PIL import Image, ImageDraw, ImageFont


class MemeEngine:
    """Generate meme images by combining images with text.

    The MemeEngine class takes an output directory during initialization
    and provides a method, make_meme, to generate memes by resizing images,
    adding text, and saving the resulting image in the specified directory.

    Attributes:
        output_dir (str): The output directory for the generated meme images.
    """

    def __init__(self, output_dir):
        """Create a new MemeEngine.

        Args:
            output_dir (str): The output directory for the
              generated meme images.
        """
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Generate a meme from the given image and text.

        Args:
            img_path (str): The path to the input image file.
            text (str): The quote body to add to the image.
            author (str): The quote author to add to the image.
            width (int, optional): The maximum width for the
              output image. Defaults to 500.

        Returns:
            str: The path to the generated meme image or
              None if an error occurs.
        """
        # Load image
        try:
            img = Image.open(img_path)
        except IOError as e:
            print(f"Error loading image: {e}")
            return None

        # Resize image proportionally with a max width of 500px
        aspect_ratio = img.width / img.height
        new_width = min(width, img.width)
        new_height = int(new_width / aspect_ratio)
        img = img.resize((new_width, new_height), Image.ANTIALIAS)

        # Add quote body and author
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('./fonts/NotoSans-Black.ttf', size=20)
        text_lines = textwrap.wrap(text, width=30)
        text_to_draw = "\n".join(text_lines + [author])
        text_width, text_height = draw.textsize(text_to_draw, font=font)

        if text_width > img.width:
            # Adjust x position range to avoid negative numbers
            x_range = (0, 0)
        else:
            x_range = (0, img.width - text_width)

        x = random.randint(*x_range)
        y = random.randint(0, img.height - text_height)
        draw.multiline_text((x, y), text_to_draw, font=font, fill='white')

        # Save manipulated image
        output_path = os.path.join(self.output_dir, f'{uuid.uuid4()}.jpeg')
        try:
            img.save(output_path, 'JPEG')
        except IOError as e:
            print(f"Error saving manipulated image: {e}")
            return None

        return output_path
