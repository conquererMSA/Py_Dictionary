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

#removing dictionary item
'''
kuno dictionary er specific item remove/delete korar jonno del, del item, clear, pop, 
popitem use kora zay.
puro dict computer memmory theke elete korar jonno "del" key word use kora zete pare. 
del infoDict.
dict theke kuno specified item delete korar jonno del dectName[keyName] use kora hoy
kuno dict ke empty korar jonno dictName.clear() method use kora zay. clear() method 
empty/None dict return kore.
kuno dict theke specified specified item remove korar jonn dictName.pop('keyName') use kora zay.
dictName.pop(keyName) method pop kora key er value return kore.
kuno dict theke randomly kuno key:value remove korar jonno dictName.pop() method use 
kora zay.
'''
# del dict and dict specified item
# del infoDict['salary'] infoDict theke salary delete hobe.
# print(infoDict) #{'name': 'MSA', 'age': 24, 'institute': 'NSTU'}

# del infoDict
# print(infoDict) # showing name error.

# clear() method
# print(infoDict.clear()) #None


