'''
dictName.get(key,defaultValue/message)
dictionary er kuno key er value access korar jonno get() method use kora hoy.
dictionary er moddhye key exist na korle get() method er defaultValue return kore.
ar key exist korle value return kore.
get(keyName,defaultValue) method er maddhyome error exception handle kora zay.
'''
infoList=[('name','MSA'),('age',24),('institute','NSTU'),('salary','unkwon')]
infoDict=dict(infoList)
# print(infoDict) #{'name': 'MSA', 'age': 24, 'institute': 'NSTU', 'salary': 'unkwon'}
# name=infoDict.get('name','not found')
# print(name)

# versity=infoDict.get('versity','not found')
# print(versity) # not found : infoDict e versity exist kore na