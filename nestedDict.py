'''
nested dictionary: nested dict e mutable type data key hisabe takte pare na.
Key hisabe sob somoy immutable type data dite hobe. Abar key er value hisabe zekuno type
data takte hobe.

'''
students={'msa':{'name':'MSA','age':24,'institute':{'school':'Mugolgoan Primary '
                                                             'School',
                                                    'ssc':'SCHOOLARSHOME',
                                                    'college': {'secondery':'Govt Science '
                                                                 'College',
                                                                'versity':'NSTU'}}},
          'smd':{'name':'SAMAD','age':24,'college':'Shah Kurrum College','roll':2452,
          'subjects':['Bangla','English','Philosophy']},
          'subjects':['Bangla','English','Philosophy']}

#accessing dict property:
msaCollege=students['msa']['institute']['college']['secondery']
# print(msaCollege)
msaVersity=students['msa']['institute']['college']['versity']
# print(msaVersity)
smdCollege=students['smd']['college']
# print(smdCollege)
smdSub3=students['smd']['subjects'][2]
# print(smdSub3)
smdBangla=students['smd']['subjects'][0]
# print(smdBangla)

# problem 1: findout the last value from a dictionary:
subject={'Python':234,'Java':384,'JS':422,'Ruby':345}
#get all keys from subject dictionary
allKeys=list(subject.keys())
# print(allKeys)
#get last keys by negative indexing from the list allkeys
lastKey=allKeys[-1]
# print(lastKey) Ruby
#get keys value
lastValue=subject[lastKey]
# print(lastValue) #345
