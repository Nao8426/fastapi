import datetime
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI()


class Document(BaseModel):
    id: str = Field(..., title='文書のID', example='1')
    title: str = Field(..., title='文書のタイトル', example='Sample Title')
    date: datetime.date = Field(..., title='日付', example='2021-01-01')

@app.get(
    '/document/{document_id}',
    response_model=Document,
    description='Read a document'
    )
def main(document_id: str):
    document = Document(
        id=document_id,
        title='Sample Title',
        date=datetime.date(2021, 1, 1)
    )
    
    return document


def calc(x: int, y: int):
    return x + y

@app.get(
    '/test/calc',
    description='Calculation Simple Test'
)
def main(a: int, b: int):
    ans = calc(a, b)

    return ans


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
