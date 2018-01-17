import requests
from luizalabCodingTest import config
import json

class EmployeeApi(object):

    def list(self, page):
        employees_list = requests.get( "{0}/?page={1}".format( config.API["url_employee"], page ) )
        employees_json = EmployeeApi.serialize_list_to_json(employees_list)
        return employees_json

    def delete(self, id):
        requests.delete("{0}/{1}".format(config.API["url_employee"],id))

    def create(self, employee_paylod):
        requests.post(config.API["url_employee"], data=employee_paylod)

    def update(self, id, employee_paylod):
        requests.put("{0}/{1}".format(config.API["url_employee"],id), data=employee_paylod)

    def serialize_list_to_json(data):
        employees_list = data.json()
        return employees_list
