from filter import *
import matplotlib.pyplot as plt
import numpy as np

polyphen_radiation = []
polyphen_pharma = []
deceased_radiation_cases = []
for x in radiation_cases:
    if(getattr(x,"days_to_death") != "'--"):
        #print(getattr(x,"days_to_death"))
        print(getattr(x,'case_submitter_id'))