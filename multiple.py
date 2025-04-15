class A:
    def welcome(self):
        print("welcome")
class B:
    def greet(self):
        print("prinsta")

class c(A,B):
    def hello(self):
        print("lobo")

obj=c()
obj.welcome()

obj.greet()
obj.hello()



