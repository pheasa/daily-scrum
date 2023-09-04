import datetime
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship, Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date as datetime_date
from typing import List

app = FastAPI()

Base = declarative_base()

class Task(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(String(500))
    create_on = Column(Date, default="now()")

class Recorder(Base):
    __tablename__ = "recorder"
    id = Column(Integer, primary_key=True)
    task_id = Column(Integer, ForeignKey("task.id"))
    create_on = Column(Date, default="now()")
    task = relationship("Task")

class TaskStatus(Base):
    __tablename__ = "task_status"
    id = Column(Integer, primary_key=True)
    recorder_id = Column(Integer, ForeignKey("recorder.id"))
    status = Column(Boolean)
    recorder = relationship("Recorder")

engine = create_engine("sqlite:///database.db")
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class PreviousTaskModel(BaseModel):
    id: int
    title: str
    description: str

class TaskModel(BaseModel):
    title: str
    description: str

class RecorderModel(BaseModel):
    task_id: int

class TaskStatusModel(BaseModel):
    recorder_id: int
    status: bool

@app.get("/get-previous")
def get_previous(db: Session = Depends(get_db)):
    # Get today's date
    today_date = datetime_date.today()
    # query  = Task.__table__.select()
    # .where(Task.create_on == today_date)
    previous_day = db.query(Task).all()
    return previous_day
    # return {"name":"pheasa"}

# create task
@app.post("/tasks")
def create_task(task: TaskModel, db: Session = Depends(get_db)):
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    new_task = Task(title=task.title, description=task.description, create_on=yesterday)
    db.add(new_task)
    db.commit()
    return new_task

# @app.post("/recorders")
# def create_recorder(recorder: RecorderModel, db: Session = Depends(get_db)):
#     new_recorder = Recorder(task_id=recorder.task_id)
#     db.add(new_recorder)
#     db.commit()
#     return new_recorder

# @app.post("/task_statuses")
# def create_task_status(task_status: TaskStatusModel, db: Session = Depends(get_db)):
#     new_task_status = TaskStatus(recorder_id=task_status.recorder_id, status=task_status.status)
#     db.add(new_task_status)
#     db.commit()
#     return new_task_status