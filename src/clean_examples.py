import asyncio

from unstructured.cleaners import core
from unstructured.cleaners.core import clean_extra_whitespace, clean_bullets, clean_ordered_bullets, clean_dashes, \
    replace_unicode_quotes, clean_non_ascii_chars, clean_trailing_punctuation
from unstructured.documents.elements import Text
from unstructured.partition.pdf import partition_pdf


def clean_text(text) -> str:
    # Step-by-step cleaning
    text = clean_extra_whitespace(text)
    text = clean_bullets(text)
    text = clean_ordered_bullets(text)
    text = clean_dashes(text)
    text = replace_unicode_quotes(text)
    text = clean_non_ascii_chars(text)
    text = clean_trailing_punctuation(text)
    return text