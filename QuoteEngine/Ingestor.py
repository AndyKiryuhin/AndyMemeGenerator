"""Ingestor module to handle multiple file types containing quotes.

This module provides an Ingestor class that can handle multiple file types
such as CSV, DOCX, PDF, and TXT, containing quotes and author information,
and create a list of QuoteModel instances from the parsed data.
"""

from .CSVIngestor import CSVIngestor
from .DOCXIngestor import DOCXIngestor
from .IngestorInterface import IngestorInterface
from .PDFIngestor import PDFIngestor
from .TXTIngestor import TXTIngestor
from models import QuoteModel
from typing import List


class Ingestor(IngestorInterface):
    """Ingest and parse multiple file types with quotes and author information.

    The Ingestor class inherits from the IngestorInterface and implements
    the required class methods to handle multiple file types such as CSV, DOCX,
    PDF, and TXT, containing quotes and author information, and create a list
    of QuoteModel instances from the parsed data.
    """

    ingestors = [CSVIngestor, DOCXIngestor, PDFIngestor, TXTIngestor]

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if the given file can be ingested.

        Args:
            path (str): The path to the file.

        Returns:
            bool: True if the file can be ingested by
              any of the supported Ingestors, False otherwise.
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return True
        return False

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the file and create a list of QuoteModel instances.

        Args:
            path (str): The path to the file.

        Returns:
            List[QuoteModel]: A list of QuoteModel
              instances created from the parsed data.
        """
        print(f'Called patse method in Ingestor for path: {path}')
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
        raise ValueError(f'Cannot parse file: {path}')
