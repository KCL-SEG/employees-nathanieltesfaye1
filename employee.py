"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salaryType, salaryPerTime, hoursWorked, commission, numberOfContracts, commissionPrice):
        self.name = name
        self.salaryType = salaryType
        self.salaryPerTime = salaryPerTime
        self.hoursWorked = hoursWorked
        self.commission = commission
        self.numberOfContracts = numberOfContracts
        self.commissionPrice = commissionPrice

    def get_pay(self):
        if self.salaryType == 'monthly' and self.commission == 'fixed':
            return self.salaryPerTime + (self.numberOfContracts * self.commissionPrice)
        elif self.salaryType == 'monthly' and self.commission == 'bonus':
            return self.salaryPerTime + self.commissionPrice
        elif self.salaryType == 'monthly':
            return self.salaryPerTime
        elif self.salaryType == 'hourly' and self.commission == 'fixed':
            return (self.salaryPerTime * self.hoursWorked) + (self.numberOfContracts * self.commissionPrice)
        elif self.salaryType == 'hourly' and self.commission == 'bonus':
            return (self.salaryPerTime * self.hoursWorked) + self.commissionPrice
        elif self.salaryType == 'hourly':
            return self.salaryPerTime * self.hoursWorked


    def __str__(self):                                               #check to see if syntax here for 'self.get_pay()' is correct...
        if self.salaryType == 'monthly' and self.commission == 'fixed':
            return (f'{self.name} works on a {self.salaryType} salary of {self.salaryPerTime} and receives a commission for {self.numberOfContracts} contract(s) at {self.commissionPrice}/contract.  Their total pay is {self.get_pay()}.')

        elif self.salaryType == 'monthly' and self.commission == 'bonus':
            return (f'{self.name} works on a {self.salaryType} salary of {self.salaryPerTime} and receives a bonus commission of {self.commissionPrice}.  Their total pay is {self.get_pay()}.')

        elif self.salaryType == 'monthly':
            return (f'{self.name} works on a monthly salary of {self.salaryPerTime}.  Their total pay is {self.get_pay()}.')

        elif self.salaryType == 'hourly' and self.commission == 'fixed':
            return (f'{self.name} works on a contract of {self.hoursWorked} hours at {self.salaryPerTime}/hour and receives a commission for {self.numberOfContracts} contract(s) at {self.commissionPrice}/contract.  Their total pay is {self.get_pay()}.')

        elif self.salaryType == 'hourly' and self.commission == 'bonus':
            return (f'{self.name} works on a contract of {self.hoursWorked} hours at {self.salaryPerTime}/hour and receives a bonus commission of {self.commissionPrice}.  Their total pay is {self.get_pay()}.')

        elif self.salaryType == 'hourly':
            return (f'{self.name} works on a contract of {self.hoursWorked} hours at {self.salaryPerTime}/hour.  Their total pay is {self.get_pay()}.')




# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 'monthly', 4000, 0, "", 1, 0)
print(str(billie))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 'hourly', 25, 100, "", 1, 0)
print(str(charlie))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 'monthly', 3000, 0, 'fixed', 4, 200)
print(str(renee))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 'hourly', 25, 150, 'fixed', 3, 220)
print(str(jan))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 'monthly', 2000, 0, 'bonus', 1, 1500)
print(str(robbie))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 'hourly', 30, 120, 'bonus', 1, 600)
print(str(ariel))
