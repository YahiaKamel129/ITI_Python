class Person:
    def __init__(self, name, money, mood, healthRate):
        self.__name = name
        self.__money = money
        self.__mood = mood
        self.__healthRate = healthRate

    def get_name(self):
        return self.__name
    def get_money(self):
        return self.__money
    def get_mood(self):
        return self.__money
    def get_mood(self):
        return self.__mood
    def get_healthRate(self):
        return self.__healthRate


    def sleep(hours):
        if hours == 7:
            return "Happy"
        elif hours < 7:
            return "Tired"
        elif hours > 7:
            return "Lazy"
        else:
            return "Error Result"
    def eat(meals):
        if meals == 3:
            return "100%"
        elif meals == 2:
            return "75%"
        elif meals == 1:
            return "50%"
        else:
            return "Error Result"
        
    def buy(items):
        item = 1
        if items == 1:
            return "decrease money 10L.E"
        elif items >1:
            items*=item
            return f"decrease money {items*10}"


class Employee(Person):
    def __init__(self, name, money, mood, healthRate, id, car, email, salary, distanceToWork):
        super().__init__(name, money, mood, healthRate)
        self.__id = id
        self.__car = car  
        self.__email = email
        self.__salary = salary
        self.__distanceToWork = distanceToWork

    def drive(self, distance, velocity):
        print(f"Employee is driving the car for {distance} km at {velocity} km/h.")
        self.__car.run(velocity, distance)

    def refuel(self, gasAmount=100):
        current_fuel = self.__car.get_fuelRate()
        new_fuel = current_fuel + gasAmount
        if new_fuel > 100:
            new_fuel = 100
        self.__car.set_fuelRate(new_fuel)
        print(f"Car refueled. Current fuel rate: {self.__car.get_fuelRate()}%.")

    def get_id(self):
        return self.__id 
    def get_car(self):
        return self.__car
    def get_email(self):
        return self.__email
    def get_salary(self):
        return self.__salary
    def get_distanceToWork(self):
        return self.__distanceToWork

    def work(Hours):
        if Hours == 8:
            return " Happy:) "
        elif Hours > 8:
            return " Tired "
        elif Hours < 8:
            return " Lazy "
        pass
    def send_email(self):
        pass



class Office:
    employeesNum = 0

    def __init__(self, name, employees=None):
        self.__name = name
        self.__employees = employees if employees is not None else []
        Office.employeesNum += len(self.__employees)

    def get_all_employees(self):
        return self.__employees

    def get_employee(self, empId):
        for emp in self.__employees:
            if emp.get_id() == empId:
                return emp
        print(f"No employee with ID {empId}")
        return None

    def hire(self, employee):
        self.__employees.append(employee)
        Office.employeesNum += 1
        print(f"Employee {employee.get_id()} hired. Total employees: {Office.employeesNum}")

    def fire(self, empId):
        emp = self.get_employee(empId)
        if emp:
            self.__employees.remove(emp)
            Office.employeesNum -= 1
            print(f"Employee {empId} fired. Total employees: {Office.employeesNum}")

    def deduct(self, empId, deduction):
        emp = self.get_employee(empId)
        if emp:
            new_salary = emp.get_salary() - deduction
            emp._Employee__salary = max(new_salary, 0)  # Protect from negative salary
            print(f"{deduction} deducted from Employee {empId}. New salary: {emp.get_salary()}")

    def reward(self, empId, reward):
        emp = self.get_employee(empId)
        if emp:
            emp._Employee__salary += reward
            print(f"{reward} added to Employee {empId}. New salary: {emp.get_salary()}")

    def check_lateness(self, empId, moveHour):
        emp = self.get_employee(empId)
        if emp:
            distance = emp.get_distanceToWork()
            velocity = emp.get_car().get_velocity()
            targetHour = 9  # For example, work starts at 9 AM
            is_late = Office.calculate_lateness(targetHour, moveHour, distance, velocity)
            if is_late:
                self.deduct(empId, 10)
            else:
                self.reward(empId, 10)

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        time_needed = distance / velocity if velocity != 0 else float('inf')
        arrival_time = moveHour + time_needed
        return arrival_time > targetHour

    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNum = num
        print(f"Employees number changed to {cls.employeesNum}")



class Car:
    def __init__(self, fuelRate, velocity):
        self.__fuelRate = fuelRate  
        self.__velocity = velocity 

    def get_fuelRate(self):
        return self.__fuelRate

    def set_fuelRate(self, fuel):
        if 0 <= fuel <= 100:
            self.__fuelRate = fuel

    def get_velocity(self):
        return self.__velocity

    def set_velocity(self, velocity):
        if 0 <= velocity <= 200:
            self.__velocity = velocity
        else:
            print("Velocity must be between 0 and 200.")

    def run(self, velocity, distance):
        self.set_velocity(velocity)
        fuel_needed = (distance / 10) * 10

        if fuel_needed > self.__fuelRate:
            distance_covered = (self.__fuelRate / 10) * 10
            remaining_distance = distance - distance_covered
            print(f"The car couldn't reach the destination. Drove {distance_covered} km before fuel ran out.")
            self.__fuelRate = 0
            self.stop(remaining_distance)
        else:
            self.__fuelRate -= fuel_needed
            print(f"The car is running at {velocity} km/h for {distance} km.")
            self.stop(0)

    def stop(self, remaining_distance=0):
        self.__velocity = 0
        if remaining_distance > 0:
            print(f"The car stopped. Remaining distance: {remaining_distance} km.")
        else:
            print("The car has arrived at the destination.")    


'''

'''
# Create Cars
car1 = Car(100, 60)
car2 = Car(80, 80)

# Create Employees
emp1 = Employee("Yahia", 1000, "Happy", 90, 1, car1, "yahia2256@gmail.com", 3000, 30)
emp2 = Employee("Sara", 1200, "Good", 85, 2, car2, "sara@gmail.com", 3200, 40)

# Option 1: Create Office and hire later
office1 = Office("Google")
office1.hire(emp1)
office1.hire(emp2)

# Option 2: Create Office with employees
office2 = Office("Microsoft", [emp1, emp2])

# Check lateness
office1.check_lateness(1, 7)  # Employee 1 moves at 7 AM

# Fire an employee
office1.fire(2)

# Reward and Deduct
office1.reward(1, 500)
office1.deduct(1, 200)

# Employee drives to work
emp1.drive(30, 60)  # Distance and speed
emp1.refuel(50)     # Refuel car