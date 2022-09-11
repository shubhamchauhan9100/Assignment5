"""
Write a Python class to implement pow(x, n)
Explanation:
Use should be able to find the nth power of the x.(i.e x*x*x*x...n times)
You must implement it using Class
Sample Input:
x: 10
n: 2
Sample Output:
100
"""
class Power():
    number=None
    power=None
    def __init__(self):
        self.number=int(input("enter number and its power:"))
        self.power=int(input())
    def calculate(self):
        sum=1
        for i in range(self.power):
            sum*=self.number
        return sum
    def __str__(self):
        print("output:",power_obj.calculate())
if __name__ == "__main__":
    while True:
        power_obj=Power()
        power_obj.__str__()
        choice=input("do you want to continue y/n:")
        if choice != 'y':
            break
    
