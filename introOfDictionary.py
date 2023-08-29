'''
What is dictionary in python: Dictionary is a unordered key:value collective data type.
In a dictionary:
dict are iterable.
keys are case-sensative.
key must be a immutable data type like string.
value can be hold any type of data.
duplicate key is not allowed. Py hold last duplicate value in pairs
we can create a dictionary by useing dict function and curly braces
student=dict(list[tuple,tuple])
student=dict([('name','MSA'),('age',24)])
student={"name":"MSA","age":24}
'''
student=dict([("name","MSA"),("age",24),("institute","NSTU")])
# print(student) # {'name': 'MSA', 'age': 24, 'institute': 'NSTU'}
# type_of_student=type(student)
# print(type_of_student) #<class 'dict'>

#count length of a dictionary
# dict_length=0
# for key in student:
#     dict_length+=1
# print(dict_length) # 3 item in student dict
# print(len(student))

#accessing single keys
#syntex dict_name['keyName']
# msaName=student["name"]
# msaSalary=student['salary'] error occur
# student['salary']=100
# msaSalary=student['salary']
# print(msaName,msaSalary) # MSA 100
# msaSalary=student['salary']-80
# print(msaSalary) #20