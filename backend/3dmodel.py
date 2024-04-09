import os
from model import *
from mpl_toolkits.mplot3d import Axes3D 
from matplotlib.pyplot import figure
import plotly.express as px

from lifelines import KaplanMeierFitter

from lifelines.utils import median_survival_times

from lifelines.statistics import pairwise_logrank_test

from lifelines import CoxPHFitter

from IPython.display import display

#Populate Radiation Total Dose 
def pharma_populate_x_y_z(drug_name, x_axis, y_axis, z_axis):
    x = []
    y = []
    z = []
    newpath = "backend\\models\\pharma_models\\scatterplots\\"
    for patient in deceased_pharma_case_ids:
        if(pharma_treatment_list.get(patient) is not None):    
         for treatment in pharma_treatment_list.get(patient):
            if(getattr(treatment,'drug_name') == drug_name):
                  print("here!")
                  newpath = "backend\\models\\pharma_models\\scatterplots\\"+getattr(treatment,'drug_name')
                  if not os.path.exists(newpath):
                      os.makedirs(newpath)
            if(getattr(treatment,x_axis).isdigit() and getattr(treatment,y_axis).isdigit() and getattr(treatment,z_axis).isdigit()):
                  x.append(float(getattr(treatment,x_axis)))
                  y.append(float(getattr(treatment,y_axis)))
                  z.append(float(getattr(treatment,z_axis)))
    print(str(x),'\n',str(y),'\n',str(z))
    df = pd.DataFrame(data={' '.join(x_axis.split("_")):x,' '.join(y_axis.split("_")):y,' '.join(z_axis.split("_")):z})
    ax = px.scatter_3d(df,x=' '.join(x_axis.split("_")),y=' '.join(y_axis.split("_")),z=' '.join(z_axis.split("_")))
    #plt.savefig("backend\\models\\radiation_models"+str(x_axis + "_to_" + y_axis + "_to_" + z_axis)+".png")
    ax.write_html(newpath+"\\"+str(x_axis + "_to_" + y_axis+"_to_"+z_axis)+".html")

def mut_pharma_populate_x_y_z(drug_name, x_axis, y_axis, z_axis):
    x = []
    y = []
    z = []
    newpath = "backend\\models\\pharma_models\\scatterplots\\"
    for patient in deceased_pharma_case_ids:
        pat_object = patient_list.get(patient)
        mut_object = patient_to_mutation.get(pat_object)
        if(pharma_treatment_list.get(patient) is not None):    
         for treatment in pharma_treatment_list.get(patient):
            if(getattr(treatment,'drug_name') == drug_name):
                  print("here!")
                  newpath = "backend\\models\\pharma_models\\scatterplots\\"+getattr(treatment,'drug_name')
                  if not os.path.exists(newpath):
                      os.makedirs(newpath)
            if(getattr(treatment,x_axis).isdigit() and getattr(treatment,y_axis).isdigit()):
                  x.append(float(getattr(treatment,x_axis)))
                  y.append(float(getattr(treatment,y_axis)))
                  z.append((getattr(mut_object,z_axis)))
    print(str(x),'\n',str(y),'\n',str(z))
    df = pd.DataFrame(data={' '.join(x_axis.split("_")):x,' '.join(y_axis.split("_")):y,' '.join(z_axis.split("_")):z})
    ax = px.scatter_3d(df,x=' '.join(x_axis.split("_")),y=' '.join(y_axis.split("_")),z=' '.join(z_axis.split("_")))
    #plt.savefig("backend\\models\\radiation_models"+str(x_axis + "_to_" + y_axis + "_to_" + z_axis)+".png")
    ax.write_html(newpath+"\\"+str(x_axis + "_to_" + y_axis+"_to_"+z_axis)+".html")
def rad_populate_x_y_z(x_axis,y_axis,z_axis):
    x = []
    y = []
    z = [] # Patient value
    #fig, axes = plt.subplots(3,3,subplot_kw={'projection':'3d'}, figsize=(9,6))
    #angles = [0,45,90,135,180]
    for patient in deceased_radiation_case_ids:
      if radiation_treatment_list.get(patient) is not None and getattr(radiation_treatment_list.get(patient),x_axis) != "[Not Available]":
        if(getattr(radiation_treatment_list.get(patient),x_axis) != "'--" and getattr(patient_list.get(patient),y_axis) != "'--" and getattr(patient_list.get(patient),z_axis) != "'--"):
            x.append(float(getattr(radiation_treatment_list.get(patient),x_axis)))
            y.append(float(getattr(patient_list.get(patient),y_axis)))
            z.append(float(getattr(patient_list.get(patient),z_axis)))
        #plt.rcParams.update({'font.size':5})
    df = pd.DataFrame(data={' '.join(x_axis.split("_")):x,' '.join(y_axis.split("_")):y,' '.join(z_axis.split("_")):z})
    ax = px.scatter_3d(df,x=' '.join(x_axis.split("_")),y=' '.join(y_axis.split("_")),z=' '.join(z_axis.split("_")))
    #plt.savefig("backend\\models\\radiation_models"+str(x_axis + "_to_" + y_axis + "_to_" + z_axis)+".png")
    ax.write_html("backend\\models\\radiation_models\\scatter_plots\\"+str(x_axis + "_to_" + y_axis+"_to_"+z_axis)+".html")

def mut_rad_populate_x_y_z(x_axis,y_axis,z_axis):
    x = []
    y = []
    z = [] # Patient value
    #fig, axes = plt.subplots(3,3,subplot_kw={'projection':'3d'}, figsize=(9,6))
    #angles = [0,45,90,135,180]
    for patient in deceased_radiation_case_ids:
      pat_object = patient_list.get(patient)
      mut_object = patient_to_mutation.get(pat_object)
      if radiation_treatment_list.get(patient) is not None and getattr(radiation_treatment_list.get(patient),x_axis) != "[Not Available]":
        if(getattr(radiation_treatment_list.get(patient),x_axis) != "'--" and getattr(patient_list.get(patient),z_axis) != "'--" and getattr(patient_list.get(patient),z_axis) != "'--"):
            x.append(float(getattr(radiation_treatment_list.get(patient),x_axis)))
            y.append((getattr(mut_object,y_axis)))
            z.append(float(getattr(patient_list.get(patient),z_axis)))
        #plt.rcParams.update({'font.size':5})
    df = pd.DataFrame(data={' '.join(x_axis.split("_")):x,' '.join(y_axis.split("_")):y,' '.join(z_axis.split("_")):z})
    ax = px.scatter_3d(df,x=' '.join(x_axis.split("_")),y=' '.join(y_axis.split("_")),z=' '.join(z_axis.split("_")))
    #plt.savefig("backend\\models\\radiation_models"+str(x_axis + "_to_" + y_axis + "_to_" + z_axis)+".png")
    ax.write_html("backend\\models\\radiation_models\\scatter_plots\\mutations\\"+y_axis+str(x_axis + "_to_" + y_axis+"_to_"+z_axis)+".html")

kmf = KaplanMeierFitter()
alk_time = []
alk_event = []
anti_time = []
anti_event = []
for patient in pharma_treatment_list.keys():
    treat_list = pharma_treatment_list.get(patient)
    for treatment in treat_list:
        if(getattr(treatment,'drug_name').lower() == 'carboplatin' or getattr(treatment,'drug_name').lower == 'cyclophosphamide' or getattr(treatment,'drug_name') == 'cytoxan'):
            patient_object = patient_list.get(patient)
            if(getattr(patient_object,'vital_status').lower() == 'dead'):
                alk_time.append(float(getattr(patient_object,'days_to_death')))
                alk_event.append(1)
            else:
                alk_time.append(float(getattr(patient_object,'days_to_last_follow_up')))
                alk_event.append(0)

for patient in pharma_treatment_list.keys():
    treat_list = pharma_treatment_list.get(patient)
    for treatment in treat_list:
        if(getattr(treatment,'drug_name').lower() == 'tamoxifen'):
            patient_object = patient_list.get(patient)
            if(getattr(patient_object,'vital_status').lower() == 'dead'):
                anti_time.append(float(getattr(patient_object,'days_to_death')))
                anti_event.append(1)
            else:
                anti_time.append(float(getattr(patient_object,'days_to_last_follow_up')))
                anti_event.append(0)

kmf.fit(anti_time,event_observed=anti_event,label="Antimetabolites")
kmf.plot()
kmf.fit(alk_time,event_observed=alk_event,label="Antiestrogen")
kmf.plot()
plt.title("Kaplan-Meier Survival Curve: Alkylating Agent and Antiestrogen Pharmaceutical Therapy")
plt.xlabel('Time')
plt.ylabel('Survival Probability')
plt.legend(loc='best')
plt.show()

cph = CoxPHFitter()
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
antimetabolites = pd.read_excel("C:\\Users\\Sai\\Documents\\GitHub\\TPBase\\backend\\clinical_data\\amtable.xlsx")
alkylatingagent = pd.read_excel("C:\\Users\\Sai\\Documents\\GitHub\\TPBase\\backend\\clinical_data\\aatable.xlsx")
data = pd.concat([alkylatingagent,antimetabolites])
cph.fit(data,duration_col='Time',event_col='Event',formula="Drug_Class")
print(data)
display(pd.DataFrame(cph.summary))
#print(anti_time)
#print(anti_event)

#drug_list = ['5-Fluorouracil','Arimidex', 'Carboplatin', 'Cyclophosphamide','Cytoxan','Docetaxel']

#for drug in drug_list:
#    mut_pharma_populate_x_y_z(drug,'number_cycles','prescribed_dose','consequences')
#for patient in deceased_pharma_case_ids:
#    if(pharma_treatment_list.get(patient) is not None):
#         for treatments in pharma_treatment_list.get(patient):
#             print(patient,": ",getattr(treatments,'drug_name'))

#Populate Days to Diagnosis

#for ax, angle in zip(axes.flat, angles):
    