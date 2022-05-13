from flask_restful import Api
from app import app
from .Task import Task
from .TaskBYID import TaskBYID

restServer = Api(app)

restServer.add_resource(Task,"/api/v1.0/task")
restServer.add_resource(TaskBYID,"/api/v1.0/task/id/<string:taskId>")