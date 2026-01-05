from utils.config_loader import load_config

v = load_config()


print(f"Collection name is {v["astra_db"]["collection_name"]}")
print(v["embedding_model"]["model_name"])
print(v["llm"]["model_name"])

from langchain_ollama import OllamaEmbeddings

emb = OllamaEmbeddings(model="nomic-embed-text:137m-v1.5-fp16")  # or your model name
vec = emb.embed_query("test")

print(len(vec))
