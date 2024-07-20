#def student_info(name, age=24,city="Tehran"):
#    return f"name={name}, age={age}, city={city}"

#s1 = ("Kiyan", 16, "Tehran")
#print(student_info(s1[0],s1[1], s1[2]))
#print(student_info(*s1))
# dictionary
 #s1 = {"name":"Kiyan", "age": 16, "city":"Tehran"}
 #print(student_info(**s1))

# def student_info(name,*args): #لیست نمرات دانشجو = *args
#     sum_ = sum(args)
#     return f"name={name}, avg={sum_/len(args)}"
# print(student_info("Kiyan", 18, 19, 20))
# print(student_info("Kiyan", 20, 18, 16, 17, 15, 19))

def student_info(name, **kwargs):
    print(name)
    for key, value in kwargs.items():
        print(f"{key} = {value}")

student_info(name="Kiyan", city="Tehran", age=16, avg=19.5)

# *args, **kwargs