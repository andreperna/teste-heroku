from dotenv import load_dotenv
from os import getenv
from enum import Enum
from fastapi import FastAPI

load_dotenv()


app = FastAPI()

class CategoriaIdade(str, Enum):
    crianca1 = 'crianca2'
    adulto1 = 'adulto2'
    idoso1 = 'idoso2'

@app.get('/')
def root():
    return {'msg':'Hello World2'}

@app.get('/items/{item}')
def root(item:int):
    return {'msg':item}

@app.get('/cat-idade/{cat_idade}')
def idade(cat_idade:CategoriaIdade):
    return {'categoria idade':cat_idade.capitalize(), 'name':cat_idade.name}

@app.get('/query/')
def query(cidade:str=None, limit:int=10):
    return {
        'cidade': cidade,
        'limite': limit
    }

@app.get('/env')
def env():
    return {'SERVER':getenv('SERVER')}

