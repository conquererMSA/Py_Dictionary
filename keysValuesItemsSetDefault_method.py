'''
In that file I explored some dict methods:
dict.keys(): kuno ekti dictionary er sob gulu keys ke ektiti list er moddye return kore.
ei list ti <class 'dict_keys'> theke ase

dict.setdefault(key,defaultValue): setdefault method e kuno dict er kuno ekti key dile
tar value return kore, zodi sei key dict e exist na kore tobe tobe default value diey
sei name e dict e ekti key:value pairs insert kore. Zodi setdefault method e
defaultValue na thake thobe key er value None hoy.
'''
#keys method
students={'MSA':223,'PVS':342,'MHD':432}
studentKeys=list(students.keys())
#dict_keys(['MSA', 'PVS', 'MHD'])
# print(studentKeys) #['MSA', 'PVS', 'MHD']
discountFees=100
for student in studentKeys:
    afterDiscount=students[student]-discountFees
    pass
    # print(f"{student} fees after discount: {afterDiscount}") #MSA fees after discount: 123

#values method
studentValue=students.values()
# print(studentValues) #dict_values([223, 342, 432])
studentValues=list(students.values())
totalValues=0
for value in studentValues:
    totalValues+=value
# print('total fees is: ',totalValues) # total fees is:  997

#items method: key:value pairs ke tuple e vore return kore.
listOfTupleOfKeyValuesPair=students.items()
# print(listOfTupleOfKeyValuesPair) #dict_items([('MSA', 223), ('PVS', 342), ('MHD', 432)])
listOfTupleOfKeyValuesPairs=list(students.items())
# print(listOfTupleOfKeyValuesPairs) #[('MSA', 223), ('PVS', 342), ('MHD', 432)]
for keyValueTuple in listOfTupleOfKeyValuesPairs:
    infoString=F"{keyValueTuple[0]} has {keyValueTuple[1]} fees"
    # print(infoString)

#setdefault method:
newStudents=students.setdefault('ALD',456)
# print(newStudents)
# print(students)
students.setdefault('SMD',234)
# print(students) #{'MSA': 223, 'PVS': 342, 'MHD': 432, 'ALD': 456, 'SMD': 234}