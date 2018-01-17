
from django.http import HttpResponseForbidden, HttpResponse
import json
from employee.api import EmployeeApi
from employee.builder_employee import BuildEmployeeJson
from django.contrib.auth.decorators import  login_required


@login_required
def manage(request, employee_id):
    if request.method == "PUT":
        return put(request, employee_id)
    elif request.method == "DELETE":
        return delete(request, employee_id)


def delete(request, employee_id):
    self = None
    res = EmployeeApi.delete(self, employee_id)
    response = HttpResponse(res, content_type="text/plain")
    return response

def put(request, employee_id):
    self = None

    employee_json = json.loads( request.body.decode('utf8').replace("'", '"') )

    employee = BuildEmployeeJson.build( self, name = employee_json["name"], email = employee_json["email"], department = employee_json["department"] )


    res = EmployeeApi.update(self, employee_id, employee)

    response = HttpResponse(res, content_type="text/plain")
    return response
