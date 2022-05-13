from flask_restful import Resource
import logging as logger

class Task(Resource):

    def get(self):
        logger.debug("Inside get method")
        return{"message":"inside the get method"},200

    def post(self):
        logger.debug("Inside post method")
        return{"message":"inside the get method"},200

    def put(self):
        logger.debug("Inside put method")
        return{"message":"inside the get method"},200


    def delete(self):
        logger.debug("inside delete method")
        return{"message":"inside the get method"},200
    