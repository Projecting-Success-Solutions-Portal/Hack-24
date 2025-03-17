import os
import openai
import chromadb
from chromadb.utils.embedding_functions import EmbeddingFunction
from sentence_transformers import SentenceTransformer
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

class ChromaEmbedFunction(EmbeddingFunction):
    def __init__(self, model_path):
        self.model = SentenceTransformer(model_path)

    def __call__(self, input):
        embeddings = self.model.encode(input, convert_to_tensor=False, show_progress_bar=False)
        return embeddings

embedding_model = ChromaEmbedFunction("sentence-transformers/all-MiniLM-L6-v2")


def prompt_formatter(query: str, context_items: list) -> str:
    context = "- " + "\n- ".join([item for item in context_items if item]) 
    
    base_prompt = """ You are an AI assistant that will answer the question of the user.
    Based on the following context:
    {context}
    Please answer the query.
    Give yourself room to think by extracting relevant passages from the context before answering the query.
    Don't return the thinking, only return the answer.
    Follow simple writing style in communications.
    Be as informative as you can, but also concise.
    Make sure the content is understandable for people without a background in engineering.
    If there is no context or they do not relate, just interact with the user like a chatbot.
    If you do not know the answer to the query, say you do not know the answer.
    """
    base_prompt = base_prompt.format(context=context)
    
    prompt = f"{base_prompt}\nUser Query: {query}\nAnswer:"
    return prompt

def retrieval(question, persist_dir):
    client = chromadb.PersistentClient(path=persist_dir)
    collection = client.get_or_create_collection(
        name="vector_storage",
        embedding_function=embedding_model,
        metadata={"hnsw:space": "cosine"}
    )
    
    results = collection.query(query_texts=[question], n_results=5)

    if results and "documents" in results and results["documents"]:
        return [doc for sublist in results["documents"] for doc in sublist] 
    
    return []

def ask_question(question, persist_dir = "chatbot/embedded_data", temperature=0.7, max_tokens=500):
    print(f"Question: {question}")
    

    context = retrieval(question, persist_dir)

    if not context:
        print("No relevant documents found!")
        return "Sorry, I couldn't find relevant information."
    
    print("Retrieved context:", context)
    
    prompt = prompt_formatter(query=question, context_items=context)
    

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an AI assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=max_tokens,
        )
        answer = response['choices'][0]['message']['content'].strip()
        return answer
    except Exception as e:
        print(f"Error with OpenAI API: {str(e)}")
        return "Sorry, I couldn't generate a response."

    