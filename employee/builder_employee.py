class BuildEmployeeJson(object):

    @staticmethod
    def build(self, name, email, department):
        return {
            "name": name,
            "email": email,
            "department": department
        }
