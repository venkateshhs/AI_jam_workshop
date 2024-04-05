import openai
import json
import os
import time

# Set your OpenAI API key here
openai.api_key = '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'


def extract_text_from_json(json_path):
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    texts = [item["text"] for item in data["0"]["ocr"]]

    combined_text = " ".join(texts)
    return combined_text


def generate_embeddings_with_retries(texts, model="text-embedding-ada-002", retries=10, base_delay=10.0):
    for attempt in range(retries):
        try:
            response = openai.Embedding.create(
                model=model,
                input=texts
            )
            return [item['embedding'] for item in response['data']]
        except openai.error.ServiceUnavailableError:
            if attempt < retries - 1:
                # Calculate sleep time with exponential backoff
                sleep_time = base_delay * (2 ** attempt)
                print(f"Service unavailable. Retrying in {sleep_time} seconds.")
                time.sleep(sleep_time)
            else:
                raise  # Reraise the last exception if all retries fail
    return None


json_file_path = "C:/Users/Vishwas/Desktop/Projects/large_language_models/AI_jam_workshop/train_parsed.json"

embeddings = {}
counter = 1
with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)
    for key, value in data.items():
        time.sleep(1)
        doc_embeddings = generate_embeddings_with_retries(value)
        embeddings[key] = doc_embeddings
        print(counter)
        counter += 1
