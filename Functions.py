#a function is a named reusable block of code
def say_hello():
    print("Hello!")
say_hello()
say_hello()

def greet(name):
    print("Hello, ",name)
greet("Brian")





def add_print(a,b):
    print(a+b)

def add_return(a,b):
    return a+b
result=add_return(7,8)

add_print(3,4)
print(result)


def double(n):
    return n*2
result=double(5)
print(result)



def square(n):
    return n*n
result=square(4)
print (result)
print(square(4)+1)




def square_print(n):
    print(n*n)
x=square_print(4)
print(x)





def a(n):
    print(n+1)

def b(n):
    return n+1

a(5)
b(5)
print(b(5))
y=a(5)
print(y)


def c(n):
    return n * 2

z = c(3)
print(z)
print(c(z))
c(10)



def get_grade(score):
    if score>=80:
        return "A"
    elif score>=70:
        return "B"
    elif score>=60:
        return "C"
    else:
        return "F"
print(get_grade(89))
print(get_grade(59))




def multiply(a,b):
    return a*b

print(multiply(3,4))
print(multiply(2,multiply(3,4)))

def is_positive(n):
    return n>0
print(is_positive(5))
print(is_positive(-2))