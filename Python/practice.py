# class employee:
#  company = "microsoft"
#  def __init__(self, name, age, salary):
#    self.name = name
#    self.age = age
#    self.salary = salary

# c = employee ("yamin",25,"12 lack")
# print(c.company,c.name,c.age,c.salary)



class calculator:
    def __init__(self, n):
        self.n = n
    def square(self):
        print(f"square of the number 4 {self.n * self.n}")
    def cube(self):
        print(f"square of the number 4 {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"square of the number 4 {self.n** 1/3}")
a = calculator(4)
a.square()
a.cube()
a.squareroot()