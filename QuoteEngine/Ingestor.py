from .CSVIngestor import CSVIngestor
from .DOCXIngestor import DOCXIngestor
from .IngestorInterface import IngestorInterface
from .PDFIngestor import PDFIngestor
from .TXTIngestor import TXTIngestor
from models import QuoteModel
from typing import List

class Ingestor(IngestorInterface):
    ingestors = [CSVIngestor, DOCXIngestor, PDFIngestor, TXTIngestor]

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return True
        return False

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        print(f'Called patse method in Ingestor for path: {path}')
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
        raise ValueError(f'Cannot parse file: {path}')
