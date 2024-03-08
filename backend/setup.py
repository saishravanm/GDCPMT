import pandas as pd

#URL="https://portal.gdc.cancer.gov/exploration?facetTab=genes&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.available_variation_data%22%2C%22value%22%3A%5B%22ssm%22%5D%7D%7D%2C%7B%22content%22%3A%7B%22field%22%3A%22cases.project.project_id%22%2C%22value%22%3A%5B%22TCGA-BRCA%22%5D%7D%2C%22op%22%3A%22in%22%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22genes.gene_id%22%2C%22value%22%3A%5B%22ENSG00000141510%22%5D%7D%7D%2C%7B%22op%22%3A%22NOT%22%2C%22content%22%3A%7B%22field%22%3A%22ssms.ssm_id%22%2C%22value%22%3A%22MISSING%22%7D%7D%5D%7D&searchTableTab=cases"
clinical=pd.read_csv('C:\\Users\\Sai\\Documents\\GitHub\\TPBase\\backend\\clinical_data\\clinical.tsv',sep='\t')
clinical.columns.name = 'clinical'

exposure=pd.read_csv('C:\\Users\\Sai\\Documents\\GitHub\\TPBase\\backend\\misc_data\\exposure.tsv',sep='\t')
exposure.columns.name = 'exposure'

family_history=pd.read_csv('C:\\Users\\Sai\\Documents\\GitHub\\TPBase\\backend\\misc_data\\family_history.tsv',sep='\t')
family_history.columns.name = 'family history'

follow_up = pd.read_csv('C:\\Users\\Sai\\Documents\\GitHub\\TPBase\\backend\\clinical_data\\follow_up.tsv',sep='\t')
follow_up.columns.name = 'follow up'

pathology_detail = pd.read_csv('C:\\Users\\Sai\\Documents\\GitHub\\TPBase\\backend\\clinical_data\\pathology_detail.tsv',sep='\t')
pathology_detail.columns.name = 'pathology detail'

##initalize variables to view biospecimen data
aliquot=pd.read_csv('C:\\Users\\Sai\\Documents\\GitHub\\TPBase\\backend\\misc_data\\aliquot.tsv',sep='\t')
aliquot.columns.name = 'aliquot'

analyte=pd.read_csv('C:\\Users\\Sai\\Documents\\GitHub\\TPBase\\backend\\biospecimen_data\\analyte.tsv',sep='\t')
analyte.columns.name = 'analyte'

portion=pd.read_csv('C:\\Users\\Sai\\Documents\\GitHub\\TPBase\\backend\\clinical_data\\portion.tsv')
portion.columns.name = 'portion'

sample=pd.read_csv('C:\\Users\\Sai\\Documents\\GitHub\\TPBase\\backend\\biospecimen_data\\sample.tsv')
sample.columns.name = 'sample'

slide=pd.read_csv('C:\\Users\\Sai\\Documents\\GitHub\\TPBase\\backend\\biospecimen_data\\slide.tsv')
slide.columns.name = 'slide'

mutations1 = pd.read_csv('C:\\Users\\Sai\\Documents\\GitHub\\TPBase\\backend\\mutations_data\\mutations_1.csv',sep='\t')
#mutations1.columns.name = 'mutations1'

mutations2 = pd.read_csv('C:\\Users\\Sai\\Documents\\GitHub\\TPBase\\backend\\mutations_data\\mutations_2.csv')
mutations2.columns.name = 'mutations2'

mutations3 = pd.read_csv('C:\\Users\\Sai\\Documents\\GitHub\\TPBase\\backend\\mutations_data\\mutations_3.csv')
mutations3.columns.name = 'mutations3'

mutations = pd.read_excel('C:\\Users\\Sai\\Documents\\GitHub\\TPBase\\backend\\mutations_data\\mutations1.xlsx')
#mutations.columns.name = mutations

#radiationinfo = pd.read_csv('./clinical_data/radiationinfo.tsv',delimiter='/t')

treatment_data = pd.ExcelFile('C:\\Users\\Sai\\Documents\\GitHub\\TPBase\\backend\\clinical_data\\treatment_data.xlsx')
radiation_treatment_data = pd.read_excel(treatment_data,'radiation_info')
pharmaceutical_treatment_data = pd.read_excel(treatment_data,'pharma_info')

with open('C:\\Users\\Sai\\Documents\\GitHub\\TPBase\\backend\\mutations_data\\patmut.csv','r',encoding='utf-8',newline='') as patmutcsv:
    patmut = pd.read_csv(patmutcsv)
#print(str(patmut))
print(type(patmut))