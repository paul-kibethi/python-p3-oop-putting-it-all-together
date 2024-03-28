#!/usr/bin/env python3

import sys

class Book:
    def __init__(self, title, page_count):
        self.title = title
        if not isinstance(page_count, int):
            print("page_count must be an integer", file=sys.stderr)
            sys.exit(1)
        self.page_count = page_count
        self.read = False

    def __str__(self):
        return f"{self.title} ({self.page_count} pages)"

    def read_book(self):
        self.read = True

    @property
    def is_read(self):
        return self.read
    
        