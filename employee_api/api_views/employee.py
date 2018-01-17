from employee.models.employee import Employee
from rest_framework import viewsets
from employee_api.api_views.serializer import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows employee to be viewed, registered and deleted.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


    # @detail_route()
    # def group_names(self, request, pk=None):
    #     """
    #     Returns a list of all the group names that the given
    #     user belongs to.
    #     """
    #     #user = self.get_object()
    #     #groups = Employee.objects.all()
    #     #return Response([group.name for group in groups])
    #     return Response("aaeee")

