# import required libraries and modules
from typing import List
from PyPDF2 import PdfFileReader
from .IngestorInterface import IngestorInterface
from models import QuoteModel

class PDFIngestor(IngestorInterface):
    # check if the given file path can be ingested (PDF)
    @classmethod
    def can_ingest(cls, path: str) -> bool:
        return path.endswith('.pdf')

    # parse the quotes from each page of the given PDF file
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        print(f'Called parse method in PDFIngestor for path: {path}')
        quotes = []
        # read in binary mode to avoid decode errors
        try:
            with open(path, 'rb') as f:
                # create a PdfFileReader object for the given file
                pdf = PdfFileReader(f)
                # loop over every page in the PDF file
                for page_num in range(pdf.getNumPages()):
                    # extract the text content of the current page
                    page = pdf.getPage(page_num)
                    text = page.extractText()
                    # split the page text into lines and get the quote and author using delimiter - 
                    for line in text.split('\n'):
                        if line:
                            quote, author = line.split(' - ')
                            # append the parsed quote to the list of quotes
                            quotes.append(QuoteModel(quote, author))
        except (Exception) as e:
            print(f"Error parsing PDF file: {e}")
        # return the list of parsed quotes
        return quotes

