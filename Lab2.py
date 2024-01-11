class Employee:
    def __init__(self, first_name, last_name, base_salary, experience):
        self.first_name = first_name
        self.last_name = last_name
        self.base_salary = base_salary
        self.experience = experience

    def counted_salary(self):
        if self.experience > 5:
            return self.base_salary * 1.2 + 500
        elif self.experience > 2:
            return self.base_salary + 200
        else:
            return self.base_salary


class Designer(Employee):
    def __init__(self, first_name, last_name, base_salary, experience, eff_coeff):
        super().__init__(first_name, last_name, base_salary, experience)
        self.eff_coeff = eff_coeff

    def counted_salary(self):
        base_salary = super().counted_salary()
        return base_salary * self.eff_coeff


class Manager(Employee):
    def __init__(self, first_name, last_name, base_salary, experience, team=None):
        super().__init__(first_name, last_name, base_salary, experience)
        self.team = team if team else []

    def counted_salary(self):
        base_salary = super().counted_salary()
        bonus = 0

        if len(self.team) > 10:
            bonus += 300
        elif len(self.team) > 5:
            bonus += 200

        developers_count = sum(isinstance(emp, Developer) for emp in self.team)
        if developers_count > len(self.team) / 2:
            bonus += base_salary * 0.1

        return base_salary + bonus


class Department:
    def __init__(self, managers=None):
        self.managers = managers if managers else []

    def give_salary(self):
        for manager in self.managers:
            for employee in manager.team:
                salary = employee.counted_salary()
                print(f"{employee.first_name} {employee.last_name} received {salary} shekels")


# Creating objects
developer1 = Employee("Alisson", "Becker", 5000, 6)
designer1 = Designer("Mohamed", "Salah", 6000, 3, 0.8)
developer2 = Employee("Trent", "Alexander-Arnold", 5500, 4)

manager1 = Manager("Jurgen", "Klopp", 8000, 8, [developer1, designer1])
manager2 = Manager("Jordan", "Henderson", 9000, 10, [developer2])

# Adding employees to manager's team
manager1.team.append(developer2)

# Creating a department
department = Department([manager1, manager2])

# Providing salaries
department.give_salary()
