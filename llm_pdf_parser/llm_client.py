import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def build_prompt(text, fields):
    return f"""
You are an intelligent document parser. From the following text, extract values for the specified fields.

Extract ONLY the values. Return as JSON in this format:
{{ "Field1": "value", "Field2": "value", ... }}

Text:
{text}

Fields to extract: {fields}
"""

def query_llm(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response['choices'][0]['message']['content']