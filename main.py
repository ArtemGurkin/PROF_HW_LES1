import application.salary
import application.db.people
import datetime

class Employee:
    def __init__(self, name):
        self.name = name

print('__name__', __name__)
if __name__ == "__main__":
    print(datetime.datetime.now())
    application.salary.calculate_salary()
    application.db.people.get_emp()

