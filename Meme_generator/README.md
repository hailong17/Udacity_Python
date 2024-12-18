# meme_generator
Meme generator dynamically generates memes, including an image with an overlaid quote.

## Structure
```
├── Makefile
├── Exceptions
│   ├── __init__.py
│   └── exception.py
├── QuoteEngine
│   ├── __init__.py
│   ├── IngestorInterface.py
│   ├── CSVImporter.py
│   ├── DocxImporter.py
│   ├── Ingestor.py
│   ├── PDFImporter.py
│   ├── QuoteModel.py
│   └── TextImporter.py
├── README.md
├── _data
│   ├── arial.ttf
│   ├── DogQuotes
│   │   ├── DogQuotesCSV.csv
│   │   ├── DogQuotesDOCX.docx
│   │   ├── DogQuotesPDF.pdf
│   │   └── DogQuotesTXT.txt
│   ├── SimpleLines
│   │   ├── SimpleLines.csv
│   │   ├── SimpleLines.docx
│   │   ├── SimpleLines.pdf
│   │   └── SimpleLines.txt
│   └── photos
│       └── dog
│           ├── xander_1.jpg
│           ├── xander_2.jpg
│           ├── xander_3.jpg
│           └── xander_4.jpg
├── app.py
├── meme.py
├── output
├── MemeEngine.py
├── requirements.txt
├── templates
    ├── base.html
    ├── meme.html
    └── meme_form.html
```
## Technologies
| No | Name | Description |
| --- | --- | --- |
| 1 | Python | Programming language |
| 2 | Pandas | Read csv file |
| 3 | Xpdf | Read pdf file |
| 4 | Pillow | Python Imaging Library |
| 5 | Flask | Web framework |

## Installation
if make can run on your machine, using this command (optional)
```
make install
```
or
```
pip install -r requirements.txt
```

## Usage
### Quote Engine
Using base class `IngestorInterface` to ingest different types of files.
With:
- @classmethod `can_ingest` method to check if the file can be ingested.
- @classmethod `parse` method to parse the file.
- @classmethod `_parse` method to raise error if occurd.

Subclasses with single inheritance: `IngestorCSV`, `IngestorDOC`, `IngestorPDF`, `IngestorText`

Multiple inheritance: `Ingestor`


### Meme Engine
Using `Pillow` to manipulate images.

## Usage

### Generate a random meme
```
make meme
```
or
```
python meme.py
```
Result
```
Meme generated in at './output/777.png'
```

### Run web service
```
make app
```
or
```
python app.py
```

and open http://127.0.0.1:5000/

Result
```
* Serving Flask app 'app'
* Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
* Running on http://127.0.0.1:5000
```
