"""Meme generator module that creates memes.

This module allows users to generate memes by providing a path
to an image file,
a quote body, and a quote author, or by selecting random
 images and quotes from
the available resources.
"""

import os
import random
import argparse
from QuoteEngine.Ingestor import Ingestor
from models import QuoteModel
from memeclass import MemeEngine


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given a path and a quote.

    Args:
        path (str, optional): The path to the image file.
          Defaults to None.
        body (str, optional): The quote body to add to the image.
          Defaults to None.
        author (str, optional): The quote author to add to the image.
          Defaults to None.

    Raises:
        Exception: Raised when the author is not provided if the body is used.

    Returns:
        str: The path to the generated meme image.
    """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            print(f'Ingestor object:{Ingestor}')
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.quote, quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Meme Generator')
    parser.add_argument('--path', type=str, help='Path to an image file')
    parser.add_argument('--body', type=str,
                        help='Quote body to add to the image')
    parser.add_argument('--author', type=str,
                        help='Quote author to add to the image')
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
