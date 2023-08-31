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
print(marks)





