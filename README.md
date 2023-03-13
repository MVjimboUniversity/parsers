# Парсеры

## html парсер
- Реализован на основе BeatifulSoup4.
- Позволяет выбирать парсер:
    - `lxml` - по умолчанию;
    - `html5lib`;
    - `html.parser`.
- Не позволяет парсить диначеские сайты, к примеру https://dzen.ru/.
- Запустить тесты: `python -m pytest tests/test_html_parser.py`
## pdf парсер

### pdf_parser
- На основе PDFMiner.
- Позволяет парсить локальные файлы и файлы с удаленных серверов.
- Не сохраняет структуру документа. Удаляет все пробелы. Текст превращается в набор символов.
- Запустить тесты: `python -m pytest tests/test_pdf_parser.py`

### pdf_parser2
- На основе PyMuPDF(fitz).
- Позволяет парсить локальные файлы.
- Сохраняет струтуру документа.
- Запустить тесты: `python -m pytest tests/test_pdf_parser2.py`

### pdf_parser3
- На основе PyPDF2.
- Позволяет парсить локальные файлы и файлы с удаленных серверов.
- Сохраняет структуру документа.
- Запустить тесты: `python -m pytest tests/test_pdf_parser3.py`

## docx парсер
- На основе docx_parser
- Позволяет парсить локальные файлы.
- Позволяет получать информацию по параграфам, а также информацию из таблиц.
- Запустить тесты: `python -m pytest tests/test_docx_parser.py`

## doc парсер
- doc-файлы конвертируются в docx и далее используется docx парсер.
    - Для Windows используется пакет Python for Windows Extensions (pywin32) для конвертирования.
    - Для Linux и macOS используется LibreOffice CLI "Lowriter" для конвертирования.
