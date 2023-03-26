"""DOCXIngestor module to ingest and parse DOCX files with quotes.

This module provides a DOCXIngestor class that can ingest and parse DOCX files
containing quotes and author information, and create a list of QuoteModel
instances from the parsed data.
"""
import docx
from typing import List
from .IngestorInterface import IngestorInterface
from models import QuoteModel


class DOCXIngestor(IngestorInterface):
    """Ingest and parse DOCX files with quotes and author information.

    The DOCXIngestor class inherits from the IngestorInterface and implements
    the required class methods to parse DOCX files containing quotes and author
    information, and create a list of QuoteModel instances
      from the parsed data.
    """

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if the given file can be ingested.

        Args:
            path (str): The path to the file.

        Returns:
            bool: True if the file is a DOCX file, False otherwise.
        """
        return path.endswith('.docx')

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the DOCX file and create a list of QuoteModel instances.

        Args:
            path (str): The path to the DOCX file.

        Returns:
            List[QuoteModel]: A list of QuoteModel instances
              created from the parsed data.
        """
        print(f'Called parse method in DOCXIngestor for path: {path}')
        quotes = []
        try:
            doc = docx.Document(path)
            for paragraph in doc.paragraphs:
                if paragraph.text:
                    quote, author = paragraph.text.split(' - ')
                    quotes.append(QuoteModel(quote, author))
        except Exception as e:
            print(f"Error parsing DOCX file: {e}")

        # Return the final list of QuoteModel objects
        return quotes
