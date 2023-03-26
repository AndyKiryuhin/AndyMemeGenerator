"""TXTIngestor module to parse quotes and authors from text files.

This module provides the TXTIngestor class that implements
 the IngestorInterface
for parsing quotes and authors from text files and creating
 a list of QuoteModel instances.
"""


# Import necessary modules/packages
from typing import List
from .IngestorInterface import IngestorInterface
from models import QuoteModel

# Create a subclass named 'TXTIngestor' and inherit
#  from the base class 'IngestorInterface'


class TXTIngestor(IngestorInterface):
    """Class to parse quotes and authors from text files.

    The TXTIngestor class implements the IngestorInterface
      for parsing quotes
    and authors from text files and creating
      a list of QuoteModel instances.
    """

    # Define a class method named 'can_ingest()' to determine whether
    #  the given file can be ingested or not (checking file extension)
    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if the given file can be ingested (text).

        Args:
            path (str): The path to the file.

        Returns:
            bool: True if the file can be ingested, False otherwise.
        """
        return path.endswith('.txt')

    # Define a class method named 'parse()' to parse the input file
    #  and return a list of QuoteModel objects
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the quotes and authors from the given text file.

        Args:
            path (str): The path to the text file.

        Returns:
            List[QuoteModel]: A list of QuoteModel instances
              created from the parsed data.
        """
        print(f'Called parse method in TXTIngestor for path: {path}')
        # Initialize an empty list to store QuoteModel objects
        quotes = []
        # Open the input file in read-mode
        try:
            with open(path, 'r') as f:
                # Read each line in the input file
                for line in f.readlines():
                    # Split the line into two parts - quote and author
                    #  - separated by the '-' character
                    quote, author = line.strip().split(' - ')
                    # Create a new QuoteModel object and append it to
                    #  the 'quotes' list
                    quotes.append(QuoteModel(quote, author))
        except Exception as e:
            print(f'Error parsing TXT file: {e}')

        # Return the final list of QuoteModel objects
        return quotes
