from filter import *
import matplotlib.pyplot as plt
import numpy as np

polyphen_radiation = []
polyphen_pharma = []
deceased_radiation_cases = []
deceased_pharma_cases = []
for x in radiation_cases:
    if(getattr(x,"days_to_death") != "'--"):
        #print(getattr(x,"days_to_death"))
        deceased_radiation_cases.append(x)
for x in pharmatherapy_cases:
    if(getattr(x,"days_to_death") != "'--"):
        deceased_pharma_cases.append(x)

for x in deceased_pharma_cases:
    print(getattr(x,'case_submitter_id'))
for x in deceased_radiation_cases:
    print(str(x))
    print(radiation_treatment_list.get(getattr(x,"case_submitter_id")))