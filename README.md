# Парсеры

## html парсер
- Реализован на основе BeatifulSoup4.
- Позволяет выбирать парсер:
    - `lxml` - по умолчанию;
    - `html5lib`;
    - `html.parser`.
- Позволяет парсить диначеские сайты, к примеру https://dzen.ru/.

## pdf парсер

### pdf_parser
- На основе PDFMiner.
- Позволяет парсить локальные файлы и файлы с удаленных серверов.
- Не сохраняет структуру документа. Удаляет все пробелы. Текст превращается в набор символов.

### pdf_parser2
- На основе PyMuPDF(fitz).
- Позволяет парсить локальные файлы.
- Сохраняет струтуру документа.

### pdf_parser3
- На основе PyPDF2.
- Позволяет парсить локальные файлы и файлы с удаленных серверов.
- -Сохраняет структуру документа.

## docx parser
- На основе docx_parser
- Позволяет парсить локальные файлы.
- Позволяет получать информацию по параграфам, а также информацию из таблиц.
