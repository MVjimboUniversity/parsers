from sys import platform
import os

from win32com import client as cl
from .docx__parser import parser


def windows_converter(path: str) -> None:
    w = cl.Dispatch("Word.Application")
    doc = w.Documents.Open(path)
    doc.SaveAs(path + 'x', 16)
    doc.Close()
    w.Quit()


def linux_converter(path: str) -> None:
    command = f"lowriter --convert-to docx {path}"
    os.system(command)


def doc_to_docx(path: str) -> str:
    """Converts doc file to docx.

    Args:
        path (str): Path to doc file.

    Returns:
        str: New path to docx file.
    """
    if platform == "win32":
        windows_converter(path)
    elif platform == "linux" or platform == "linux2":
        linux_converter(path)
    return path + 'x'


def parser(path: str) -> list[str]:
    new_path = doc_to_docx(path)
    return parser(new_path)


def main():
    # Для Windows путь необходимо вводить полностью начиная с корня диска
    # Для Linux проверить наличие lowriter с помощью команды lowriter --version
    text = parser(r"D:\Code\University\Mag_2sem\Automatic_systems\parsers\test.doc")
    for paragraph in text:
        print(paragraph)


if __name__ == "__main__":
    main()