from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

#-------------------------GET------------------------------

@app.get('/')
def index():
    return {'data' : {'name':'Shazil'}}

@app.get('/blog')
def blog(limit=10, published:bool=True, sort:Optional[str]=None):
    if published==True:
        return {'data' : f'Returned {limit} published blogs from db.'} 
    else:
        return {'data' : f'Returned {limit} unpublished blogs from db.'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data':'unpublished'}


@app.get('/blog/{id}/comments')
def comments(id: int, limit=10):
    return {'data' : {id}}

#-------------------------POST------------------------------

class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]


@app.post('/blog')
def create_blog(blog: Blog):
    return {'data' : f"Blog with title: {blog.title} created."}


if __name__=="__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)