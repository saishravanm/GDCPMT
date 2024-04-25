import pandas as pd

#URL="https://portal.gdc.cancer.gov/exploration?facetTab=genes&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.available_variation_data%22%2C%22value%22%3A%5B%22ssm%22%5D%7D%7D%2C%7B%22content%22%3A%7B%22field%22%3A%22cases.project.project_id%22%2C%22value%22%3A%5B%22TCGA-BRCA%22%5D%7D%2C%22op%22%3A%22in%22%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22genes.gene_id%22%2C%22value%22%3A%5B%22ENSG00000141510%22%5D%7D%7D%2C%7B%22op%22%3A%22NOT%22%2C%22content%22%3A%7B%22field%22%3A%22ssms.ssm_id%22%2C%22value%22%3A%22MISSING%22%7D%7D%5D%7D&searchTableTab=cases"
clinical=pd.read_csv('C:\\Users\\Sai\\Desktop\\CS4v98_Final_Submission_Saishravan_Muthukrishnan\\GDCPMT\\backend\\EXAMPLE_DATA\\clinical_data\\clinical.tsv',sep='\t')
clinical.columns.name = 'clinical'

#mutations1 = pd.read_csv('C:\\Users\\Sai\\Documents\\GitHub\\TPBase\\backend\\mutations_data\\mutations_1.csv',sep='\t')
#mutations1.columns.name = 'mutations1'

#mutations2 = pd.read_csv('C:\\Users\\Sai\\Documents\\GitHub\\TPBase\\backend\\mutations_data\\mutations_2.csv')
#mutations2.columns.name = 'mutations2'

#mutations3 = pd.read_csv('C:\\Users\\Sai\\Documents\\GitHub\\TPBase\\backend\\mutations_data\\mutations_3.csv')
#mutations3.columns.name = 'mutations3'

mutations = pd.read_excel('C:\\Users\\Sai\\Desktop\\CS4v98_Final_Submission_Saishravan_Muthukrishnan\\GDCPMT\\backend\\EXAMPLE_DATA\\mutations_data\\mutations1.xlsx')
#mutations.columns.name = mutations

#radiationinfo = pd.read_csv('./clinical_data/radiationinfo.tsv',delimiter='/t')

treatment_data = pd.ExcelFile('C:\\Users\\Sai\\Desktop\\CS4v98_Final_Submission_Saishravan_Muthukrishnan\\GDCPMT\\backend\\EXAMPLE_DATA\\clinical_data\\all_clinical_drug_info.xlsx')
pharmaceutical_treatment_data = pd.read_excel("C:\\Users\\Sai\\Desktop\\CS4v98_Final_Submission_Saishravan_Muthukrishnan\\GDCPMT\\backend\\EXAMPLE_DATA\\clinical_data\\all_clinicaL_drug_info.xlsx")

with open('C:\\Users\\Sai\\Desktop\\CS4v98_Final_Submission_Saishravan_Muthukrishnan\\GDCPMT\\backend\\EXAMPLE_DATA\\mutations_data\\patmut.csv','r',encoding='utf-8',newline='') as patmutcsv:
    patmut = pd.read_csv(patmutcsv)
#print(str(patmut))
print(type(patmut))