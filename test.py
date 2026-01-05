from utils.config_loader import load_config

v = load_config()


print(f"Collection name is {v["astra_db"]["collection_name"]}")
print(v["embedding_model"]["model_name"])
print(v["llm"]["model_name"])

