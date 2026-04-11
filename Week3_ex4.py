#Class con cho
from turtle import color


class Dog:
    def __init__(self, name, age, color, weight):
        self.name = name 
        self.age = age
        self.color = color
        self.weight = weight
    
    def bark(self):
        print(f"{self.name} is barking")
    def eat(self, food):
        print(f"{self.name} is eating")
    def sleep(self, hours):
        print(f"{self.name} is sleeping")

dog1 = Dog("Buddy", 3, "Brown", 23)
dog1.bark()
dog1.sleep(8)


#Class o to
class Car:
    def __init__(self, brand, color, speed, seats):
        self.brand = brand
        self.color = color
        self.speed = speed
        self.seats = seats

    def drive(self):
        print(f"{self.brand} is driving")

    def accelerate(self):
        self.speed += 10
        print(f"{self.speed} is accelerating to {self.speed} km/h")

    def brake(self):
        self.speed -= 10
        print(f"{self.speed} is braking to {self.speed} km/h")

    def stop(self):
        self.speed = 0
        print(f"{self.brand} has stopped")

car_1 = Car("Toyota", "Black", 70, 5)
car_1.drive()
car_1.accelerate()
car_1.brake()


#Class tai khoan 
class Account:
    def __init__(self, owner, account_number, balance):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print("Nap tien thanh cong. So du hien tai: ", self.balance)
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Rut tien thanh cong. So du hien tai: ", self.balance)
        else:
            print("So du khong du de rut tien!")
    def check_balance(self):
        print("So du hien tai: ", self.balance)
    def transfer(self, other_account, amount):
        if amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print("Chuyen tien thanh cong")
        else:
            print("So du hien tai khong du de chuyen tien!")


account1 = Account("MP", 123456789, 10000000000) 
account2 = Account("MP2", 987654321, 59000000000)
account1.deposit(5000000000)                           
account1.withdraw(3000000000)
account1.check_balance()