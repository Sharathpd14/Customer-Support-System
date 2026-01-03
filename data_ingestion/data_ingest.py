from langchain_astradb import AstraDBVectorStore
from dotenv import load_dotenv
import os
import pandas as pd 
from data_ingestion.data_transfer import DataConverter

load_dotenv()


class IngestData:
    def __init__(self):
        print("Ready")
        self.product_data = pd.read_csv("data/flipkart_product_review.csv")
        # print(self.product_data.head())
    
    def data_ingestion(self):
        pass
    
    
if __name__=="__main__":
    IngestData()