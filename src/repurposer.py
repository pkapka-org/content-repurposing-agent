from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field


class RepurposedContent(BaseModel):
    summary: str = Field(description="2-3 sentence plain-language summary of the content")
    linkedin_post: str = Field(description="Professional LinkedIn post, 150-250 words, with a hook opening and 3-4 key insights")
    twitter_thread: list[str] = Field(description="Twitter/X thread of 5-7 tweets, each under 280 characters, numbered 1/ 2/ etc.")
    email_blurb: str = Field(description="Email newsletter blurb, 80-120 words, conversational tone with a clear CTA at the end")
    instagram_caption: str = Field(description="Instagram caption with a punchy opening line, 2-3 short paragraphs, 3-5 relevant hashtags at the end")


def repurpose(content: str) -> dict:
    llm = ChatOllama(model="qwen2.5:1.5b", temperature=0.4)
    parser = JsonOutputParser(pydantic_object=RepurposedContent)

    prompt = ChatPromptTemplate.from_messages([
        ("system", (
            "You are an expert content strategist and copywriter. "
            "Given a piece of long-form content, you repurpose it into multiple formats "
            "optimised for each platform. Return valid JSON only."
        )),
        ("human", "Content to repurpose:\n\n{content}\n\n{format_instructions}")
    ])

    chain = prompt | llm | parser

    return chain.invoke({
        "content": content,
        "format_instructions": parser.get_format_instructions()
    })
