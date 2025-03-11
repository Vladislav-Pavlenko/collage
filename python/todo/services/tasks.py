from bson import ObjectId
from ..db.initialMongoDBConnection import tasks_collection

def getTasks():
    return list(tasks_collection.find())

def getTaskById(id):
    task = tasks_collection.find_one({"_id":ObjectId(id)})
    if task == None:
        raise Exception("Not found Task")
    return task

def addTask(data):
    tasks_collection.insert_one(data)

def markTaskIsComplete(id):
    task = tasks_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": {"is_complete": True}})
    if task == None:
        raise Exception("Not found Task")

def updateTaskById(task, id):
    def validate_and_clean_data(data):
        return {key: value for key, value in data.items() if value}
    valid_task = validate_and_clean_data(task)
    task = tasks_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": valid_task})
    if task == None:
        raise Exception("Not found Task")

def deleteTaskById(id):
    task = tasks_collection.find_one_and_delete({"_id": ObjectId(id)})
    if task == None:
        raise Exception("Not found Task")
    return task