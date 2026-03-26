from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title='Request Body bilan ishlash')

class Data(BaseModel):
    a: float
    b: float
    operator: str

@app.post('/api/products')
async def create_product(
    data: dict
):
    return data

# POST /api/calculate {"a": 3, "b": 4, "operator": "+"} -> {"result": 7}


@app.post('/api/calculate')
async def calculate(data: Data):
    if data.operator == '+':
        result = data.a + data.b
    elif data.operator == '-':
        result = data.a - data.b
    elif data.operator == '*':
        result = data.a * data.b
    elif data.operator == '/':
        result = data.a / data.b
    else:
        return {"error": "Notogri operator"}
    
    return {"result": result}
