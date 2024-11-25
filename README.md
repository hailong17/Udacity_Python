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
│   ├──arial.ttf
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
├── output
├── meme.py
├── output
├── MemeEngine.py
├── requirements.txt
├── templates
    ├── base.html
    ├── meme.html
    └── meme_form.html
```


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

### Generate a random meme
```
make meme
```
or
```
python meme.py
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
