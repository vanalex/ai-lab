import os
import asyncio
import json

from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint
from openai import AsyncOpenAI
from pydantic import BaseModel, Field, TypeAdapter
from transformers import pipeline


async def main():
    print("Hello from ai-lab!")

    model_id = "openai/gpt-oss-120b"

    from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

    llm = HuggingFaceEndpoint(
        repo_id=model_id,
        task="text-generation",
        max_new_tokens=512,
        do_sample=False,
        repetition_penalty=1.03,
        provider="auto",  # let Hugging Face choose the best provider for you
    )

    chat_model = ChatHuggingFace(llm=llm)
    response = chat_model.invoke("please tell me a joke")
    print(response)

if __name__ == "__main__":
    asyncio.run(main())
