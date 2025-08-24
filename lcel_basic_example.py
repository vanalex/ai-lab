import asyncio

from langchain_huggingface.llms import HuggingFacePipeline
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain_core.prompts import PromptTemplate

async def main():
    print("Hello World!")
    hf = HuggingFacePipeline.from_model_id(
        model_id="gpt2",
        task="text-generation",
        pipeline_kwargs={"max_new_tokens": 10},
    )

    template = """Question: {question}

    Answer: Let's think step by step."""
    prompt = PromptTemplate.from_template(template)

    chain = prompt | hf.bind(skip_prompt=False)

    question = "What is electroencephalography?"

    print(chain.invoke({"question": question}))

    for chunk in chain.stream(question):
        print(chunk, end="", flush=True)


if __name__ == '__main__':
    asyncio.run(main())
