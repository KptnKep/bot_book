import os
import sys

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book = {}
def _get_part_text(text, start, size):
    end_signs = ',.!:;?'
    counter = 0
    if len(text) < start + size:
        size = len(text) - start
        text = text[start:start + size]
    else:
        if text[start + size] == '.' and text[start + size - 1] in end_signs:
            text = text[start:start + size - 2]
            size -= 2
        else:
            text = text[start:start + size]
        for i in range(size - 1, 0, -1):
            if text[i] in end_signs:
                break
            counter = size - i
    page_text = text[:size - counter]
    page_size = size - counter
    return page_text, page_size

def prepare_book(path):
    with open(file=path, mode='r', encoding='UTF-8') as book_text:
        text = book_text.read()
    start = 0
    p = 1
    for i in range(1, ((len(text) // PAGE_SIZE) + 2)):
        page, next_page = _get_part_text(text, start, PAGE_SIZE)
        book[p] = page.lstrip()
        p += 1
        start += next_page

prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))