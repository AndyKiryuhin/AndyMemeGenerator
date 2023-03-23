import csv
from typing import List
from QuoteEngine.IngestorInterface import IngestorInterface
from models import QuoteModel
class CSVIngestor(IngestorInterface):
    @classmethod
    def can_ingest(cls, path: str) -> bool:
        return path.endswith('.csv')

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
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