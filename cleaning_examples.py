import asyncio

from unstructured.cleaners.core import replace_unicode_quotes
from unstructured.documents.elements import Text

async def clean_data(data):
    element = Text(data)
    element.apply(replace_unicode_quotes)
    print(element)

if __name__ == '__main__':
    data = "Philadelphia Eaglesâ\x80\x99 victory"
    asyncio.run(clean_data(data))