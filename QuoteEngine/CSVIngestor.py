"""CSVIngestor module to ingest and parse CSV files with quotes.

This module provides a CSVIngestor class that can ingest and parse CSV files
containing quotes and author information, and create a list of QuoteModel
instances from the parsed data.
"""

import csv
from typing import List
from QuoteEngine.IngestorInterface import IngestorInterface
from models import QuoteModel


class CSVIngestor(IngestorInterface):
    """Ingest and parse CSV files with quotes and author information.

    The CSVIngestor class inherits from the IngestorInterface and implements
    the required class methods to parse CSV files containing
      quotes and author
    information, and create a list of QuoteModel instances
      from the parsed data.
    """

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if the given file can be ingested.

        Args:
            path (str): The path to the file.

        Returns:
            bool: True if the file is a CSV file, False otherwise.
        """
        return path.endswith('.csv')

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the CSV file and create a list of QuoteModel instances.

        Args:
            path (str): The path to the CSV file.

        Returns:
            List[QuoteModel]: A list of QuoteModel instances
              created from the parsed data.
        """
        print(f'Called parse method in CSVIngestor for path: {path}')
        quotes = []
        try:
            with open(path, 'r') as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    quote = QuoteModel(row[0], row[1])
                    quotes.append(quote)
        except Exception as e:
            print(f"Error parsing CSV file: {e}")
        return quotes
