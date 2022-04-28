def find_employees_role(name):
    for employee in employees:
        first_name, last_name, role = None, None, None
        for i in employee.keys():
            if i == 'first_name':
                first_name = employee[i]
            elif i == 'last_name':
                last_name = employee[i]
            elif i == 'role':
                role = employee[i]
        if name == " ".join([first_name, last_name]):
            return role
    return "Does not work here!"


print(find_employees_role("Dipper Pines"), "Does not work here!")
print(find_employees_role("Morty Smith"), "Truck Driver")
print(find_employees_role("Anna Bell"), "Admin")