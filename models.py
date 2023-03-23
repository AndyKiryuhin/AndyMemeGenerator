from typing import List

class QuoteModel:
    def __init__(self, quote: str, author: str):
        self.quote = quote
        self.author = author

    def __repr__(self):
        return f'"{self.quote}" - {self.author}'