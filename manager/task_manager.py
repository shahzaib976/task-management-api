from typing import Union 
from pydantic import BaseModel
from fastapi import FastAPI 
from utils.utils import generate_id
from utils.utils import get_current_date
from models.task import Task



class TaskManager():
    def __init__(self):
     self.__tasks=[]

    def read_tasks(self,query :str | None=None):
        if query:
           tasks = [task for task in self.__tasks if query==task["title"]]  
           return tasks
        return self.__tasks
    


    def read_task(self,task_id: str):
        task = self.find_task(task_id)
        return task
    
    def create_task(self, task:Task):
        new_task = {
            "id": generate_id(),
            "title": task.title,
            "description": task.description,
            "completed": False,
            "created_at": get_current_date(),
            "updated_at": get_current_date(),
    }
        self.__tasks.append(new_task)
        return new_task
    
    def update_task(self,task_id: str, task:Task):
        updated_task = self.find_task(task_id)
        if updated_task:
         updated_task["title"] = task.title
         updated_task["description"] = task.description
         return updated_task
        return None
    
    def delete_task(self,task_id: str):
        task = self.find_task(task_id)
        if task:
         self.__tasks.remove(task)
         return task
        return None
    
    def markCompleted(self,task_id:str):
        task = self.find_task(task_id)
        task["completed"]=True
        return task
    
    def find_task(self,id:str):
       task = None
       for t in self.__tasks:
          if t["id"]==id:
             task = t
             return task
       return None

