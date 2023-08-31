'''
In that file I explored some dict methods:
dict.keys(): kuno ekti dictionary er sob gulu keys ke ektiti list er moddye return kore.
ei list ti <class 'dict_keys'> theke ase
'''
#keys method
students={'MSA':223,'PVS':342,'MHD':432}
studentKeys=list(students.keys())
#dict_keys(['MSA', 'PVS', 'MHD'])
# print(studentKeys) #['MSA', 'PVS', 'MHD']
discountFees=100
for student in studentKeys:
    afterDiscount=students[student]-discountFees
    print(f"{student} fees after discount: {afterDiscount}") #MSA fees after discount: 123

#values method
studentValue=students.values()
# print(studentValues) #dict_values([223, 342, 432])
studentValues=list(students.values())
totalValues=0
for value in studentValues:
    totalValues+=value
# print('total fees is: ',totalValues) # total fees is:  997

#items method:
