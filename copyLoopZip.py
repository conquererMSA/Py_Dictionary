'''
I explore dictionary copy, loop, and zip method

#dict.copy():
copy() method shallow copy kore new dictionary create kore zar refference and
id/memmory location alada hoy.

Tobe assignment operator/ = diye copy create korle copy kora dict old dict ke reffer
kore. Alada vabe id/memmory location create hoy na.


'''
fees={'MSA':100,'PVS':120,'MHD':130}
copyFees=fees.copy()
# Ekhane copyFees dict er id and refrence fees dict theke alada.
# print(copyFees)
# print(id(fees))
# print(id(copyFees))

#assignment operator
assignCopy=fees
# print(assignCopy)
# print(id(fees)) #3003438877120
# print(id(assignCopy)) #3003438877120
# ekhane dict assignCopy dict fees theke create hoyeche. Notun create holeo assignCopy
# er alada kuno id ba reference memmory te toiree hoy ni. Dict fees er memmory referene
# dict assignCopy er memmory reference same.
assignCopy.clear()
# print(fees) # {}
#ekhane duplicate dict assignCopy.clear() korle ekoi sathe mani dict fees clear
# hoyezay.Karo dutir reference ekoi.

#loop and findout average subjet marks and put that on a list.
msa={"Python":85,"Java":60,"JS":70}
pvs={"Python":89,"Java":80,"JS":90}
mhd={"Python":80,"Java":55,"JS":90}
students=[msa,pvs,mhd]
marks=[]
for student in students:
    studentTotalMarks=0
    for subject in student:
        # print(subject)
        studentTotalMarks=studentTotalMarks+student[subject]
        # findout average marks
    averageMarks=studentTotalMarks/len(student)
    marks.append(averageMarks)
# print(marks)

#zip method:
'''
ekadik list ke ekti single dict/list/tuple e convert korar jonno zip function use kora 
hoy.
# zip function zip obj/<zip object at 0x00000156B1ECE940> return kore
Zip function ekekta argument ke tuple convert kore, ekekta tuple comma diye separate 
thake.
***Zodi zip function er moddhye shudhu matro duiti list deya hoy, tobe sei zip object 
ke dictionary te convert kora zay.

Zodi dui er odhik list deya hoy tobe setake list e convert korte hoy.
Dui er odhik list takle sei zip obj ke list na hoy set e convert kora zay.

Zodi kuno zip obj ke use kora hoy tobe seti empty hoye zay. zip obj empty hoye gele 
setike ar unzip ba use kora zay na
'''
chatro=['MSA','SMD','ALD']
sub=['Python','Java','JS']
subMarks=[12,23,34]
infoObj=list(zip(chatro,sub,subMarks))
# print(infoObj) # [('MSA', 'Python', 12), ('SMD', 'Java', 23), ('ALD', 'JS', 34)]
infoSet=set(zip(chatro,sub,subMarks))
# print(infoSet) #{('MSA', 'Python', 12), ('SMD', 'Java', 23), ('ALD', 'JS', 34)}
# infoObj2=dict(zip(chatro,sub,subMarks))
# print(infoObj2) # through error, karo zip function e 3ti list ache.

studentList=[]
for studentInf0 in infoObj:
     # print(studentInf0) # ('ALD', 'JS', 34)
     for info in studentInf0:
         # print(info)
         studentList.append(info)
# print(studentList) #['ALD', 'JS', 34, 'SMD', 'Java', 23, 'MSA', 'Python', 12]



