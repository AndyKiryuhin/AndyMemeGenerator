"""QuoteModel module for representing quotes with author information.

This module provides a QuoteModel class that represents a quote along
with its author, and allows for a string representation of the quote
and author.
"""

from typing import List


class QuoteModel:
    """Represents a quote along with its author.

    The QuoteModel class stores a quote and its author, and provides
    a string representation of the quote and author.

    Attributes:
        quote (str): The quote text.
        author (str): The author of the quote.
    """

    def __init__(self, quote: str, author: str):
        """Create a new QuoteModel.

        Args:
            quote (str): The quote text.
            author (str): The author of the quote.
        """
        self.quote = quote
        self.author = author

    def __repr__(self):
        """Return a string representation of the quote and author.

        Returns:
            str: A string representation of the quote and author.
        """
        return f'"{self.quote}" - {self.author}'
