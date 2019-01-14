# print("Hello World")
# def main():
#     print("Hello world!")
# print("Guru99")
# main()
# a = 9
# print(a)
# b = "guru99"
# print(b)
# print(str(a) + b)
# f = 101
# print(f)
# def my_func():
#     f = "I am learning Python"
#     print(f)
# my_func()
# print(f)
# def newVar():
#     global f
#     print(f)
#     f = "new f"
# newVar()
# print(f)
# del f
# var1 = "Guru99"
# var2 = "Software Testing"
# print(var1[0])
# print(var2[1:5])
# print(var2[:])
# print(var1 * 2)
# x = "u" not in var1
# print(x)
# print("hi"r"\nbye")
# name = "guru"
# number = 99
# print("%s %d" % (name, number))
# print(str(number)*5)
# x = "Hello World!"
# print(x[:6])
# print(x[0:6] + "Guru99")
# print(x[0:6])
# oldstring = "I like chocolate"
# newstring = oldstring.replace("like", "love")
# print(newstring)
# print(oldstring)
# print(newstring.upper())
# print(oldstring.lower())
# # print(":".join("Python"))
# var = "12345"
# print("".join(reversed(var)))
# mystring = "dword1 dword2 dword3"
# print(mystring.split("d"))
# tup1 = ("Robert", "Carlos", "1965", "Terminator 1995", "Actor", "Florida");
# tup2 = (1, 2, 3, 4, 5, 6, 7);
# print(tup1[0])
# print(tup2[1:4])
# x = ("Guru99", "20", "Education")
# (company, emp, profile) = x
# print(company)
# print(emp)
# print(profile)
# print(x)
# a = (5, 6)
# b = (6, 4)
# if (a>b): print("a")
# else: print("b")
# Dict = {"Tim": 18, "Denise":5, "Catherine": 12, "Robert": 112}
# print(Dict["Tim"])
# Boys = {"Tim": 18, "Robert": 112}
# Girls = {"Denise":5, "Catherine": 12}
# studentY = Boys.copy()
# studentX = Girls.copy()
# print(studentX)
# print(studentY)
# Dict.update({"Sarah": 25})
# print(Dict)
# del Dict["Sarah"]
# print(Dict)
# print("Students Name: %s" % list(Dict.items()))
# for key in list(Dict.keys()):
#     if key in list(Boys.keys()):
#         print(True)
#     else:
#         print(False)
# students = list(Dict.keys())
# students.sort()
# print(students)
# for a in students:
#     print(": ".join((a,str(Dict[a]))))
# print("Length: %d" % len(Dict))
# print("Type: %s" % type(Dict))
# print("Printable string: %s" % str(Dict))
# print(Dict)
# x = 4
# x += 4
# y = 5
# print("the value of x>y is", x>y)
# print("Line 1 - Value of x: ", x)
# print("Line 2 - Value of y: ", y)
# a = True
# b = False
# print("a and b is", a and b)
# print("a or b is", a or b)
# b = a
# print("new a or b is", a or b)
# print("not a is", not a)
# x = 4
# y = 8
# list = [1, 2, 3, 4, 5,]
# if (x in list):
#     print("Line 1 - x is available in the given list")
# else: 
#     print("Line 1 - x is not available in the given list")
# if (y not in list):
#     print("Line 2 - y is not available in the given list")
# else:
#     print("Line 2 - y is available in the given list")
# def func1():
#     print("I am learning Python Functions!!!")
#     x = 5
#     return(x)
# func1()
# myVar = func1()
# print(myVar)
# def square(x):
#     var = x * x
#     return(var)
# print(square(4))
# def bigNumber(a, b, c, d, e, f, g):
#     ans = a * b * c * d * e *f *g * a **2
#     return(ans)
# print(bigNumber(10, 20, 30, 40, 50, 60, 70))
# def multiply(x, y = 0):
#     ans = x * y
#     return(ans)
# print("only x:", multiply(5))
# print("x and y:", multiply(5, 1))
# def guru99(args):
#     print(args)
#     return
# myArray = (1, 2, 4, 5)
# guru99(myArray)
# def guru992(*args):
#     print(args)
#     return
# guru992(1,2, 4, 5)

## Note: Why is there a pointer necessary when the function is being 
## called by directly inputting values, but when passing a predefined 
## tuple the pointer is not required and slightly changes the output? 
## (Lines 138 - 146)

# def main():
#     x, y = 2, 2
#     st = "x is smaller" if (x < y) else "x >= y"
#     print(st)
# main()
# def switch(arg):
#     switcher = {
#         0: "Zero",
#         1: "One",
#         2: "Two"
#     }
#     return(switcher.get(arg, "nothing"))
# print(switch(3))