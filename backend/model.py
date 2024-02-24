from filter import *
import matplotlib.pyplot as plt
import numpy as np

polyphen_radiation = []
polyphen_pharma = []
deceased_radiation_cases = []
deceased_radiation_case_ids= []
deceased_pharma_cases = []
deceased_pharma_case_ids = []
for x in radiation_cases:
    if(getattr(x,"days_to_death") != "'--"):
        #print(getattr(x,"days_to_death"))
        deceased_radiation_cases.append(x)
        deceased_radiation_case_ids.append(getattr(x,'case_submitter_id'))
for x in pharmatherapy_cases:
    if(getattr(x,"days_to_death") != "'--"):
        deceased_pharma_cases.append(x)
        deceased_pharma_case_ids.append(getattr(x,'case_submitter_id'))

for x in deceased_pharma_cases:
    print(getattr(x,'case_submitter_id'))

p = deceased_radiation_cases[0]
for x in dir(p):
    print("<p2>",x.replace("_"," "),": ","{","{","patient.",x,"}","}","</p2>","\n","<br></br>")
#for x in deceased_radiation_cases:
#    print(str(x))
#    print(radiation_treatment_list.get(getattr(x,"case_submitter_id")))