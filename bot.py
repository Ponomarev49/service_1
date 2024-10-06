from pydantic import BaseModel
from typing import List, Dict

class Product(BaseModel):
    name : str
    producer : str
    id : str

class Bot(BaseModel):
    products: Dict[int, Product] = {}
    addresses: Dict[str, str] = {}
