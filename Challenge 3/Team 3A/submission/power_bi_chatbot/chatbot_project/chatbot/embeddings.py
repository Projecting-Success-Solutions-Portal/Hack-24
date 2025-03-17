import os
import re
import chromadb
from chromadb.config import Settings
from tqdm import tqdm 

persist_directory = "chatbot/embedded_data"

client = chromadb.PersistentClient(path=persist_directory)

collection_name = "vector_storage"  
collection = client.get_or_create_collection(name=collection_name)

folder_path = 'chatbot/exported_txt'

txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

for filename in tqdm(txt_files, desc="Processing TXT Files"):

    file_path = os.path.join(folder_path, filename)

    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()
    
  
    file_content = file_content.strip() 
    file_content = re.sub(r'\s+', ' ', file_content) 

    full_content = f"Filename: {filename}\n\n{file_content}"

    try:
        collection.add(
            ids=[filename],
            documents=[full_content], 
            metadatas=[{"filename": filename}] 
        )
    except Exception as e:
        print(f"Failed to insert document from {filename}: {e}")

print("Processing complete! Data is now stored persistently.")


query_text = "risk management in January 2018"  
results = collection.query(
    query_texts=[query_text],  
    n_results=5  
)

""" 
print("\nSearch Results:")
for i, (doc, meta) in enumerate(zip(results["documents"][0], results["metadatas"][0])):
    print(f"{i+1}. {meta['filename']}: {doc[:200]}...")  
 """
