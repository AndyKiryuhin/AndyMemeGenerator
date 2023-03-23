# Import necessary modules/packages
from typing import List
from .IngestorInterface import IngestorInterface
from models import QuoteModel

# Create a subclass named 'TXTIngestor' and inherit from the base class 'IngestorInterface'
class TXTIngestor(IngestorInterface):

    # Define a class method named 'can_ingest()' to determine whether the given file can be ingested or not (checking file extension)
    @classmethod
    def can_ingest(cls, path: str) -> bool:
        return path.endswith('.txt')

    # Define a class method named 'parse()' to parse the input file and return a list of QuoteModel objects
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        print(f'Called parse method in TXTIngestor for path: {path}')
        # Initialize an empty list to store QuoteModel objects
        quotes = []
        # Open the input file in read-mode
        try:
            with open(path, 'r') as f:
                # Read each line in the input file
                for line in f.readlines():
                    # Split the line into two parts - quote and author - separated by the '-' character
                    quote, author = line.strip().split(' - ')
                    # Create a new QuoteModel object and append it to the 'quotes' list
                    quotes.append(QuoteModel(quote, author))
        except Exception as e:
            print(f'Error parsing TXT file: {e}')
                
        # Return the final list of QuoteModel objects
        return quotes
