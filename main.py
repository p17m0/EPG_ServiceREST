from fastapi import FastAPI, HTTPException, Query, Response
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from calculator import calculate

app = FastAPI()

class Phrase(BaseModel):
    """
    Класс выражения.
    """
    phrase: str

@app.get("/")
async def read_root():
    """
    Главная страница /.
    """
    return "Hello World"

@app.get("/index")
async def read_root():
    """
    Главная страница index.
    """
    return "Hello World from Index"


@app.get("/eval/{stroka:path}")
async def read_item(stroka: str = Query(min_length=5, max_length=100)):
    """
    Получает строку, выполняет выражение, возвращает рeзультат.
    """
    eval = calculate(stroka)
    if eval == -1:
        raise HTTPException(status_code=400, detail="Неправильное выражение")
    return Response(content = f'{stroka} = {eval}', status_code=200)

@app.post("/eval/")
async def read_item(phr: Phrase):
    """
    Получает строку, создаёт объект модели, возвращает json.
    """
    eq = calculate(phr.phrase)
    if eq == -1:
        exception = jsonable_encoder({'message': "Неправильноe выражение"})
        raise HTTPException(status_code=400, detail=exception)
    phr.phrase = eq
    data = jsonable_encoder(phr)
    return JSONResponse(content=data, status_code=201)
