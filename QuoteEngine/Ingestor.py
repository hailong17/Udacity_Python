"""
Project: Meme Generator
Author: LongNH63
Date: 24/11/2024
"""

"""Module that Encapsulate moduels for ingest differnt types of files."""
from QuoteEngine.QuoteModel import QuoteModel, InvalidFileFormat
from .IngestorInterface import IngestorInterface
from .CSVImporter import CSVImporter
from .DocxImporter import DocxImporter
from .PDFImporter import PDFImporter
from .TextImporter import TextImporter
from typing import List


class Ingestor(IngestorInterface):
    """Class encapsulating each impoter modules."""

    ingestors = [CSVImporter,
                 DocxImporter,
                 PDFImporter,
                 TextImporter]

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        """Pasre paths(files) by appropriate ingestor."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
        raise InvalidFileFormat

