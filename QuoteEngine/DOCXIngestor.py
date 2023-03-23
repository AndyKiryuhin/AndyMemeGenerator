import docx
from typing import List
from .IngestorInterface import IngestorInterface
from models import QuoteModel

class DOCXIngestor(IngestorInterface):
    @classmethod
    def can_ingest(cls, path: str) -> bool:
        return path.endswith('.docx')

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
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