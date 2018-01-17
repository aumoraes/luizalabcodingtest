from django import forms
from employee.models.employee import Employee

class RegisterUserForm(forms.Form):
  name = forms.CharField(required=True)
  email = forms.EmailField(required=True)
  department = forms.CharField(required=True)

  def is_valid(self):
    valid = True
    if not super(RegisterUserForm, self).is_valid():
      self.add_error("Please, verify informed data")
      valid = False

    valid = self.checkUserAlreadyExists()

    return valid

  def add_error(self, message):
    errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
    errors.append(message)

  def checkUserAlreadyExists(self):
    valid = True

    user_exists = Employee.objects.filter(name=self.data['name']).exists()

    if user_exists:
      self.add_error("User with name {} already exists".format(self.data['name']))
      valid = False

    return valid
