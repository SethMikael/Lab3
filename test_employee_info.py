import employee_info

def test_get_employees_by_age_range():
    result = employee_info.get_employees_by_age_range(20, 30)
    assert (result == [{"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
                       {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}])

def test_calculate_average_salary():
    result = employee_info.calculate_average_salary()
    assert (result == 60166.666666666664)


def test_get_employees_by_dept():
    result = employee_info.get_employees_by_dept("Sales")
    assert (result == [{"name": "John", "age": 30, "department": "Sales", "salary": 50000},
                       {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}])