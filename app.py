"""Meme generator web application using Flask.

This module allows users to generate memes by choosing
random images and quotes
or by providing custom inputs through a web interface.
"""

import random
import os
import requests
from QuoteEngine.Ingestor import Ingestor
from memeclass import MemeEngine
from flask import Flask, render_template, abort, request


app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources and return quotes and images.

    Returns:
        tuple: A tuple containing a list of QuoteModel
        objects and a list of image paths.
    """
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for file in quote_files:
        quotes.extend(Ingestor.parse(file))

    images_path = "./_data/photos/dog/"
    imgs = [os.path.join(images_path, img) for img in os.listdir(images_path)]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme and render the meme.html template.

    Returns:
        str: Rendered HTML template with a randomly generated meme.
    """
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.quote, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """Render the meme_form.html template.

    Returns:
        str: Rendered HTML template for meme form input.
    """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme.

    Returns:
        str: Rendered HTML template with a user-defined meme.
    """
    image_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']

    # 1. Use requests to save the image from the image_url form param
    #  to a temp local file.
    response = requests.get(image_url)
    temp_path = f"./tmp/{random.randint(0, 1000000)}.jpg"

    with open(temp_path, 'wb') as f:
        f.write(response.content)

    # 2. Use the meme object to generate a meme using this
    #  temp file and the body and author form paramaters.
    path = meme.make_meme(temp_path, body, author)

    # 3. Remove the temporary saved image.
    os.remove(temp_path)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
