import asyncio

from unstructured.partition.pdf import partition_pdf
from unstructured.staging.base import elements_to_json

file_path = "files/"
base_file_name = "layout-parser-paper"

async def main():
    elements = partition_pdf(filename=f"{file_path}/{base_file_name}.pdf")
    elements_to_json(elements=elements, filename=f"{file_path}/{base_file_name}-output.json")
    print("\n\n".join([str(el) for el in elements][:10]))

if __name__ == "__main__":
    asyncio.run(main())