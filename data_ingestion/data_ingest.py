from langchain_astradb import AstraDBVectorStore
from dotenv import load_dotenv
import os
import pandas as pd 
from data_ingestion.data_transfer import DataConverter
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT")
ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_KEYSPACE = os.getenv("ASTRA_DB_KEYSPACE")

os.environ["GROQ_API_KEY"] = GROQ_API_KEY
os.environ["ASTRA_DB_API_ENDPOINT"] = ASTRA_DB_API_ENDPOINT
os.environ["ASTRA_DB_APPLICATION_TOKEN"] = ASTRA_DB_APPLICATION_TOKEN
os.environ["ASTRA_DB_KEYSPACE"] = ASTRA_DB_KEYSPACE

class IngestData:
    def __init__(self):
        print("Ready")
        self.embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001",output_dimensionality=1536)
        self.data_converter = DataConverter()
    
    def data_ingestion(self, status):
        vec_store = AstraDBVectorStore(
            embedding=self.embeddings,
            collection_name="e_com_chatbot",
            api_endpoint=ASTRA_DB_API_ENDPOINT,
            token=ASTRA_DB_APPLICATION_TOKEN,
            namespace=ASTRA_DB_KEYSPACE,
        )
        
        # storage = status
        
        if status==None:
            docs = self.data_converter.data_transformation()
            inserted_ids = vec_store.add_documents(docs)
            
        else:
            return vec_store
        
        return vec_store, inserted_ids
    
    
if __name__=="__main__":
    IngestData()