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

def gen_radtreatment_bar(x_n, y_n):
    y_axis = []
    x_axis = []
    y_name = x_n
    x_name = y_n
    for x in radiation_treatment_list.values(): 
     if(getattr(x,y_name) != "[Not Available]"):
         y_axis.append(getattr(x,y_name))
         x_axis.append(getattr(x,x_name))
    #else:
    #    deceased_radiation_case_ids.remove(deceased_radiation_case_ids.index(x))
    fig, pat_to_rad_dose = plt.subplots()
    x_name.sort()
    y_name.sort()
    pat_to_rad_dose.bar(x_axis,y_axis)
    pat_to_rad_dose.set_ylabel(y_name.replace('_'," "))
    pat_to_rad_dose.set_xlabel(x_name.replace('_'," "))
###################################################################################################

    plt.savefig("./models"+str(x_name + "_to_" + y_name)+".png")
    plt.show()

#p = deceased_radiation_cases[0]
#for x in dir(p):
#    print("<p2>",x.replace("_"," "),": ","{","{","patient.",x,"}","}","</p2>","\n","<br></br>")
#for x in deceased_radiation_cases:
#    print(str(x))
#    print(radiation_treatment_list.get(getattr(x,"case_submitter_id")))