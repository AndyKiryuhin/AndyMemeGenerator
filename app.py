import random
import os
import requests
from QuoteEngine.Ingestor import Ingestor
from memeclass import MemeEngine
from flask import Flask, render_template, abort, request

# @TODO Import your Ingestor and MemeEngine classes

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # TODO: Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes = []
    for file in quote_files:
        quotes.extend(Ingestor.parse(file))



    images_path = "./_data/photos/dog/"

    # TODO: Use the pythons standard library os class to find all
    # images within the images images_path directory
    imgs = [os.path.join(images_path, img) for img in os.listdir(images_path)]

    return quotes, imgs



quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    # @TODO:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.quote, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    image_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']

    # 1. Use requests to save the image from the image_url form param to a temp local file.
    response = requests.get(image_url)
    temp_path = f"./tmp/{random.randint(0, 1000000)}.jpg"

    with open(temp_path, 'wb') as f:
        f.write(response.content)

    # 2. Use the meme object to generate a meme using this temp file and the body and author form paramaters.
    path = meme.make_meme(temp_path, body, author)

    # 3. Remove the temporary saved image.
    os.remove(temp_path)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
