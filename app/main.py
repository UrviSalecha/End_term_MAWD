from fastapi import FastAPI,Form,HTTPException,Depends,Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy import Column,Integer,Boolean,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,session
from database import get_db,engine,Base
from sqlalchemy.orm import Session
from database import engine,Base,get_db
# from passlib.context import CryptContext
# import json could not import module 



app=FastAPI()
app.mount("/static",StaticFiles(directory="static"),name="static")
templates=Jinja2Templates(directory="templates")

class Book(Base):
    __tablename__="books"
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String,index=True)
    author=Column(String,index=True)
    year=Column(Integer,index=True)
    
Base.metadata.create_all(bind=engine)    

@app.get("/books")
def get_books(request:Request,db:Session=Depends(get_db)):
    books=db.query(Book).all()
    return templates.TemplateResponse("books.html",{"request":request,"books":books})

@app.get("/books/{id}")
def get_byid(id:int,request: Request,db:Session=Depends(get_db)):
    book=db.query(Book).filter(Book.id==id).first()
    if not book:
        raise HTTPException(status_code=404,detail="Book not found")
    return templates.TemplateResponse("book_detail.html",{"request":request,"book":book})

@app.post("/books") #Create
def create_book(title:str=Form(...),author:str=Form(...),year:int=Form(...),db:Session=Depends(get_db)):
    new_book=Book(title=title,author=author,year=year)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return RedirectResponse("/books",status_code=303)

@app.post("/books/{id}") #update
def update_book(id:int,title:str=Form(...),author:str=Form(...),year:int=Form(...),db:Session=Depends(get_db)):
    book=db.query(Book).filter(Book.id==id).first()
    if not book:
        raise HTTPException(status_code=404,detail="Book not found")
    book.title=title
    book.author=author
    book.year=year
    db.commit()
    db.refresh(book)
    return RedirectResponse("/books",status_code=303)

@app.post("/books/{id}/delete") #delete
def delete_book(id:int,db:Session=Depends(get_db)):
    book=db.query(Book).filter(Book.id==id).first()
    if not book:
        raise HTTPException(status_code=404,detail="Book not found")
    db.delete(book)
    db.commit()
    return RedirectResponse("/books",status_code=303)