import os
from model import *
from mpl_toolkits.mplot3d import Axes3D 
from matplotlib.pyplot import figure
import plotly.express as px

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

mut_rad_populate_x_y_z('radiation_total_dose','consequences','days_to_diagnosis')
mut_rad_populate_x_y_z('radiation_total_dose','consequences','days_to_best_overall_response')
mut_rad_populate_x_y_z('radiation_total_dose','consequences','days_to_last_follow_up')
mut_rad_populate_x_y_z('radiation_total_dose','consequences','days_to_last_known_disease_status')
mut_rad_populate_x_y_z('radiation_total_dose','consequences','days_to_recurrence')
mut_rad_populate_x_y_z('radiation_total_dose','consequences','days_to_diagnosis')
mut_rad_populate_x_y_z('radiation_total_dose','consequences','days_to_best_overall_response')
mut_rad_populate_x_y_z('radiation_total_dose','consequences','days_to_last_follow_up')
mut_rad_populate_x_y_z('radiation_total_dose','consequences','days_to_last_known_disease_status')
mut_rad_populate_x_y_z('radiation_total_dose','consequences','days_to_recurrence')
mut_rad_populate_x_y_z('radiation_adjuvant_fractions_total','consequences','days_to_diagnosis')
mut_rad_populate_x_y_z('radiation_adjuvant_fractions_total','consequences','days_to_diagnosis')
mut_rad_populate_x_y_z('radiation_total_dose','consequences','number_of_cycles')
mut_rad_populate_x_y_z('radiation_total_dose','consequences','number_of_cycles')
mut_rad_populate_x_y_z('radiation_adjuvant_fractions_total','consequences','number_of_cycles')
mut_rad_populate_x_y_z('radiation_adjuvant_fractions_total','consequences','number_of_cycles')

#drug_list = ['5-Fluorouracil','Arimidex', 'Carboplatin', 'Cyclophosphamide','Cytoxan','Docetaxel']

#for drug in drug_list:
#    mut_pharma_populate_x_y_z(drug,'number_cycles','prescribed_dose','consequences')
#for patient in deceased_pharma_case_ids:
#    if(pharma_treatment_list.get(patient) is not None):
#         for treatments in pharma_treatment_list.get(patient):
#             print(patient,": ",getattr(treatments,'drug_name'))

#Populate Days to Diagnosis

#for ax, angle in zip(axes.flat, angles):
    