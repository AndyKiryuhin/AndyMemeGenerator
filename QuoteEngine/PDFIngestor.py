"""PDFIngestor module to parse quotes and authors from PDF files.

This module provides the PDFIngestor class that implements
 the IngestorInterface
for parsing quotes and authors from PDF files and creating
 a list of QuoteModel instances.
"""


# import required libraries and modules
import os
import random
import subprocess
from typing import List
from .IngestorInterface import IngestorInterface
from models import QuoteModel


class PDFIngestor(IngestorInterface):
    """Class to parse quotes and authors from PDF files.

    The PDFIngestor class implements the IngestorInterface
      for parsing quotes
    and authors from PDF files and creating a list of
      QuoteModel instances.
    """

    # check if the given file path can be ingested (PDF)
    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if the given file can be ingested (PDF).

        Args:
            path (str): The path to the file.

        Returns:
            bool: True if the file can be ingested,
              False otherwise.
        """
        return path.endswith('.pdf')

    # parse the quotes from each page of the given PDF file
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the quotes from each page of the given PDF file.

        Args:
            path (str): The path to the PDF file.

        Returns:
            List[QuoteModel]: A list of QuoteModel instances
              created from the parsed data.
        """
        print(f'Called parse method in PDFIngestor for path: {path}')
        quotes = []
        # read in binary mode to avoid decode errors
        try:
            # use pdftotext command-line utility to convert PDF to text
            text_path = f'./_data/DogQuotes/{random.randint(0, 1000)}.txt'
            subprocess.run(['pdftotext', path, text_path], check=True)

            # read the text file and parse quotes and authors
            with open(text_path, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line:
                        quote, author = line.split(' - ')
                        quotes.append(QuoteModel(quote, author))

            # remove temporary text file
            os.remove(text_path)
        except (Exception) as e:
            print(f"Error parsing PDF file: {e}")
        # return the list of parsed quotes
        return quotes
