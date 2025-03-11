from ..services.tasks import getTasks, addTask, getTaskById, markTaskIsComplete, updateTaskById, deleteTaskById


class Task:
    def __init__(self):
        pass

    def getTasks(self):
        task = getTasks()
        print("Task found successfully")
        return task
    def getTaskById(self, id):
        try:
            task = getTaskById(id)
            print("Task found successfully")
            return task
        except Exception as error:
            print(error)
    def addTask(self, data):
        addTask(data)

    def markTaskIsComplete(self, id):
        try:
            task = markTaskIsComplete(id)
            print("Task completed")
            return task
        except Exception as error:
            print(error)
    def updateTaskById(self, task, id):
        try:
            updateTaskById(task, id)
            print("Task updated")
        except Exception as error:
            print(error)
    def deleteTaskById(self, id):
        try:
            deleteTaskById(id)
            print("Task deleted")
        except Exception as error:
            print(error)
#title, folder, description, is_complete
# Go to school, School, I go to school, 