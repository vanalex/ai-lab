# AI Lab

This repository contains tools for AI experimentation and document processing.

## Requirements

### Python Dependencies
Python 3.12 or higher is required. All Python dependencies are listed in `pyproject.toml`.

### System Dependencies

#### Poppler
The PDF processing functionality requires [Poppler](https://poppler.freedesktop.org/) to be installed and available in your system PATH.

Installation instructions:
- **macOS**: `brew install poppler`
- **Ubuntu/Debian**: `apt-get install poppler-utils`
- **Windows**: Download from [poppler-windows](https://github.com/oschwartz10612/poppler-windows/releases) and add the bin directory to your PATH

## Usage

### PDF Processing
To process PDF files, run:

```bash
python file_parser.py
```

This will parse the PDF file and generate a JSON output with the extracted content.