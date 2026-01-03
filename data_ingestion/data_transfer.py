import pandas as pd
from langchain_core.documents import Document


class DataConverter:
    def __init__(self):
        self.product_data = pd.read_csv("data/flipkart_product_review.csv")
        
            
    def data_transformation(self):
        required_columns = list(self.product_data.columns[1:])
        
        product_list = []
        
        for index, row in self.product_data.iterrows():
            obj = {
                "product_name" : row["product_title"],
                "product_rating": row["rating"],
                "product_summary": row["summary"],
                "product_review": row["review"]
            }
            
            product_list.append(obj)
        
        docs =[]
        for items in product_list:
            metadata = {
                "product_name":items["product_name"],
                "product_rating":items["product_rating"],
                "product_summary":items["product_summary"],
            }
            doc = Document(page_content=items["product_review"],metadata = metadata)
            docs.append(doc)
        
        return docs
    
    
    
    
if __name__=="__main__":
    DataConverter().data_transformation()
    