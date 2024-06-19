import filter
import pandas as pd
from filter import pharma_treatment_list
import matplotlib.pyplot as plt
import lifelines

filter.create_patient_list()
filter.create_mutation()
filter.create_pharma_treatment_list()
sample = pd.read_csv("C:\\Users\\Sai\\Desktop\\GDCPMT\\backend\\biospecimen\\sample.tsv", delimiter='\t')
slide = pd.read_csv("C:\\Users\\Sai\\Desktop\\GDCPMT\\backend\\biospecimen\\slide.tsv", delimiter='\t')
#print(sample)
#print(slide)

selected_samples = pd.DataFrame()
selected_slides = pd.DataFrame()
for x, row in sample.iterrows():
    if(pharma_treatment_list.get(row['case_submitter_id']) is not None):
        selected_samples = selected_samples._append(row)
for x, row in slide.iterrows():
    if(pharma_treatment_list.get(row['case_submitter_id']) is not None):
        selected_slides = selected_slides._append(row)


selected_samples.to_excel('./samples.xlsx')
selected_slides.to_excel('./samples.xlsx')