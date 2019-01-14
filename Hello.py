#print("Hello World")
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
Dict = {"Tim": 18, "Denise":5, "Catherine": 12, "Robert": 112}
print(Dict["Tim"])
Boys = {"Tim": 18, "Robert": 112}
Girls = {"Denise":5, "Catherine": 12}
studentY = Boys.copy()
studentX = Girls.copy()
print(studentX)
print(studentY)
Dict.update({"Sarah": 25})
print(Dict)
del Dict["Sarah"]
print(Dict)
print("Students Name: %s" % list(Dict.items()))
for key in list(Dict.keys()):
    if key in list(Boys.keys()):
        print(True)
    else:
        print(False)
students = list(Dict.keys())
students.sort()
print(students)
for a in students:
    print(": ".join((a,str(Dict[a]))))
print("Length: %d" % len(Dict))
print("Type: %s" % type(Dict))
print("Printable string: %s" % str(Dict))
print(Dict)

