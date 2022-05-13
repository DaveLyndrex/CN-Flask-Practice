from flask_restful import Resource
import logging as logger

class TaskBYID(Resource):

    def get(self,taskId):
        logger.debug("Inside get method of task by id")
        return{"message":"inside the get method of task by id. TASK-ID = {}".format(taskId) },200

    def post(self,taskId):
        logger.debug("Inside post method of TaskBYID")
        return{"message":"inside the post method of task by id. TASK-ID = {}".format(taskId) },200

    def put(self,taskId):
        logger.debug("Inside put method of TaskBYID")
        return{"message":"inside the put method of task by id. TASK-ID = {}".format(taskId) },200


    def delete(self,taskId):
        logger.debug("inside delete method of TaskBYID")
        return{"message":"inside the delete method of task by id. TASK-ID = {}".format(taskId) },200
    