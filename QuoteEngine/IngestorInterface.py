"""IngestorInterface module to define an abstract base class for file parsing.

This module provides an abstract base class, IngestorInterface, that defines
the required methods for ingesting and parsing files containing quotes and
author information to create a list of QuoteModel instances.
"""

from abc import ABC, abstractmethod
from typing import List
from models import QuoteModel


class IngestorInterface(ABC):
    """Abstract base class to define methods for ingesting files.

    IngestorInterface is an abstract base class that defines the required
    methods for ingesting and parsing files containing quotes and author
    information to create a list of QuoteModel instances.
    """

    @classmethod
    @abstractmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if the given file can be ingested.

        Args:
            path (str): The path to the file.

        Returns:
            bool: True if the file can be ingested, False otherwise.
        """
        pass

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the file and create a list of QuoteModel instances.

        Args:
            path (str): The path to the file.

        Returns:
            List[QuoteModel]: A list of QuoteModel instances
              created from the parsed data.
        """
        pass
