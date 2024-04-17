from setup import *
import urllib.request
import json
import re
from Patient import Patient
from Mutation import Mutation
from Treatment import *
import bs4


f = open("./categories.txt","a")

radiation_cases = []
pharmatherapy_cases = []
patient_list = {}
mutation_list = []
patient_to_mutation={}
mutation_to_patients={}
radiation_treatment_list = {}
pharma_treatment_list = {}
final_pharma = ["TCGA-E2-A14Z",
"TCGA-AO-A03O",
"TCGA-B6-A409",
"TCGA-E9-A1RB",
"TCGA-E9-A1NF",
"TCGA-E9-A226",
"TCGA-AR-A0U2",
"TCGA-E9-A1RB"
"TCGA-E9-A1NF",
"TCGA-E9-A226",
"TCGA-E9-A1RB"]

for x, row in clinical.iterrows():
    patient_list[row["case_submitter_id"]]=(Patient(row["case_id"],
row["case_submitter_id"],
row["project_id"],
row["age_at_index"],
row["age_is_obfuscated"],
row["cause_of_death"],
row["cause_of_death_source"],
row["country_of_residence_at_enrollment"],
row["days_to_birth"],
row["days_to_death"],
row["ethnicity"],
row["gender"],
row["occupation_duration_years"],
row["premature_at_birth"],
row["race"],
row["vital_status"],
row["weeks_gestation_at_birth"],
row["year_of_birth"],
row["year_of_death"],
row["adrenal_hormone"],
row["age_at_diagnosis"],
row["ajcc_clinical_m"],
row["ajcc_clinical_n"],
row["ajcc_clinical_stage"],
row["ajcc_clinical_t"],
row["ajcc_pathologic_m"],
row["ajcc_pathologic_n"],
row["ajcc_pathologic_stage"],
row["ajcc_pathologic_t"],
row["ajcc_staging_system_edition"],
row["anaplasia_present"],
row["anaplasia_present_type"],
row["ann_arbor_b_symptoms"],
row["ann_arbor_b_symptoms_described"],
row["ann_arbor_clinical_stage"],
row["ann_arbor_extranodal_involvement"],
row["ann_arbor_pathologic_stage"],
row["best_overall_response"],
row["breslow_thickness"],
row["burkitt_lymphoma_clinical_variant"],
row["child_pugh_classification"],
row["circumferential_resection_margin"],
row["classification_of_tumor"],
row["cog_liver_stage"],
row["cog_neuroblastoma_risk_group"],
row["cog_renal_stage"],
row["cog_rhabdomyosarcoma_risk_group"],
row["days_to_best_overall_response"],
row["days_to_diagnosis"],
row["days_to_last_follow_up"],
row["days_to_last_known_disease_status"],
row["days_to_recurrence"],
row["eln_risk_classification"],
row["enneking_msts_grade"],
row["enneking_msts_metastasis"],
row["enneking_msts_stage"],
row["enneking_msts_tumor_site"],
row["esophageal_columnar_dysplasia_degree"],
row["esophageal_columnar_metaplasia_present"],
row["figo_stage"],
row["figo_staging_edition_year"],
row["first_symptom_prior_to_diagnosis"],
row["gastric_esophageal_junction_involvement"],
row["gleason_grade_group"],
row["gleason_grade_tertiary"],
row["gleason_patterns_percent"],
row["goblet_cells_columnar_mucosa_present"],
row["greatest_tumor_dimension"],
row["gross_tumor_weight"],
row["icd_10_code"],
row["igcccg_stage"],
row["inpc_grade"],
row["inpc_histologic_group"],
row["inrg_stage"],
row["inss_stage"],
row["international_prognostic_index"],
row["irs_group"],
row["irs_stage"],
row["ishak_fibrosis_score"],
row["iss_stage"],
row["largest_extrapelvic_peritoneal_focus"],
row["last_known_disease_status"],
row["laterality"],
row["lymph_node_involved_site"],
row["lymph_nodes_positive"],
row["lymph_nodes_tested"],
row["lymphatic_invasion_present"],
row["margin_distance"],
row["margins_involved_site"],
row["masaoka_stage"],
row["medulloblastoma_molecular_classification"],
row["metastasis_at_diagnosis"],
row["metastasis_at_diagnosis_site"],
row["method_of_diagnosis"],
row["micropapillary_features"],
row["mitosis_karyorrhexis_index"],
row["mitotic_count"],
row["morphology"],
row["non_nodal_regional_disease"],
row["non_nodal_tumor_deposits"],
row["ovarian_specimen_status"],
row["ovarian_surface_involvement"],
row["papillary_renal_cell_type"],
row["percent_tumor_invasion"],
row["perineural_invasion_present"],
row["peripancreatic_lymph_nodes_positive"],
row["peripancreatic_lymph_nodes_tested"],
row["peritoneal_fluid_cytological_status"],
row["pregnant_at_diagnosis"],
row["primary_diagnosis"],
row["primary_disease"],
row["primary_gleason_grade"],
row["prior_malignancy"],
row["prior_treatment"],
row["progression_or_recurrence"],
row["residual_disease"],
row["satellite_nodule_present"],
row["secondary_gleason_grade"],
row["site_of_resection_or_biopsy"],
row["sites_of_involvement"],
row["supratentorial_localization"],
row["synchronous_malignancy"],
row["tissue_or_organ_of_origin"],
row["transglottic_extension"],
row["tumor_confined_to_organ_of_origin"],
row["tumor_depth"],
row["tumor_focality"],
row["tumor_grade"],
row["tumor_largest_dimension_diameter"],
row["tumor_regression_grade"],
row["tumor_stage"],
row["vascular_invasion_present"],
row["vascular_invasion_type"],
row["weiss_assessment_score"],
row["who_cns_grade"],
row["who_nte_grade"],
row["wilms_tumor_histologic_subtype"],
row["year_of_diagnosis"],
row["chemo_concurrent_to_radiation"],
row["days_to_treatment_end"],
row["days_to_treatment_start"],
row["initial_disease_status"],
row["number_of_cycles"],
row["reason_treatment_ended"],
row["regimen_or_line_of_therapy"],
row["route_of_administration"],
row["therapeutic_agents"],
row["treatment_anatomic_site"],
row["treatment_arm"],
row["treatment_dose"],
row["treatment_dose_units"],
row["treatment_effect"],
row["treatment_effect_indicator"],
row["treatment_frequency"],
row["treatment_intent_type"],
row["treatment_or_therapy"],
row["treatment_outcome"],
row["treatment_type"],
))
for x, row in mutations.iterrows():
    mut_list = []
    mut = Mutation(row['DNA Change'],row['Type'],row['Consequences'],row['Impact'])
    mutation_list.append(mut)
    mutation_to_patients[mut] = [row['Associated Patients'].split('\n')]
    for y in row['Associated Patients'].split('\n'):
        patient_to_mutation[patient_list.get(y)]=mut
for x, row in radiation_treatment_data.iterrows():
    radiation_treatment_list[row["bcr_patient_barcode"]]=(Radiation(row["bcr_patient_barcode"],row["bcr_radiation_barcode"],row["form_completion_date"],row["bcr_radiation_uuid"],row["radiation_therapy_type"],row["radiation_therapy_site"],row["radiation_total_dose"],row["radiation_adjuvant_units"],row["radiation_adjuvant_fractions_total"],row["radiation_therapy_started_days_to"],row["radiation_therapy_ended_days_to"],row["treatment_best_response"],row["course_number"],row["therapy_regimen"]))
for x, row in pharmaceutical_treatment_data.iterrows():
        if(patient_list.get(row['bcr_patient_barcode']) is not None):
            pharma_treatment_list.setdefault(row["bcr_patient_barcode"],[])
            pharma_treatment_list[row["bcr_patient_barcode"]].append(Pharmaceutical(row["bcr_patient_barcode"],row["bcr_drug_barcode"],row["form_completion_date"],row["bcr_drug_uuid"],row["drug_name"],row["therapy_type"],row["days_to_drug_therapy_start"],row["days_to_drug_therapy_end"],row["measure_of_response"],row["number_cycles"],row["therapy_type_notes"],row["prescribed_dose_units"],row['total_dose_units'],row["prescribed_dose"],row["regimen_number"],row["route_of_administration"],row["regimen_indication"],row["total_dose"],row["tx_on_clinical_trial"]))
for patient in patient_list.values():
    if((getattr(patient,'treatment_type') == 'Radiation Therapy, NOS') & (getattr(patient,'treatment_or_therapy') == 'yes')):
        radiation_cases.append(patient)
    elif((getattr(patient,'treatment_type') == 'Pharmaceutical Therapy, NOS') &  (getattr(patient,'treatment_or_therapy') == 'yes')):
        pharmatherapy_cases.append(patient)

inner_list = []
outer_list = []
for patient in pharma_treatment_list.keys():
    bcr_patient_barcode = patient
    pat_obj = patient_list.get(patient)
    for drug in pharma_treatment_list.get(patient):
        if(getattr(drug,'total_dose') != '[Not Available]'):
            drug_name = getattr(drug,'drug_name')
            therapy_type = getattr(drug,'therapy_type')
            days_to_drug_therapy_start=getattr(drug,'days_to_drug_therapy_start')
            days_to_drug_therapy_end=getattr(drug,'days_to_drug_therapy_end')
            total_dose=getattr(drug,'total_dose')
            dose_units = getattr(drug, 'total_dose_units')
            consequence_type=getattr(patient_to_mutation.get(pat_obj),'consequence_type')
            if(getattr(pat_obj,'vital_status').lower() == 'dead'):
                deceased = 1
            else: 
                deceased = 0
            inner_list = [bcr_patient_barcode,drug_name,therapy_type,days_to_drug_therapy_start,days_to_drug_therapy_end,total_dose,dose_units,consequence_type,deceased]
            outer_list.append(inner_list)
        
        
pharma_df = pd.DataFrame(outer_list,columns=['bcr_patient_barcode','drug_name','therapy_type','days_to_drug_therapy_start', 'days_to_drug_therapy_end',	'total_dose','dose_units','consequence_type','deceased'])
pharma_df.to_excel('output.xlsx',index=False)
print(pharma_df.head())
#print("Number of radation cases: " + str(len(radiation_cases))+"\n")
#print("Number of pharmatherapy cases: " + str(len(pharmatherapy_cases))+"\n")
#print("Total cases: " + str(len(radiation_cases+pharmatherapy_cases))+"\n\n")

#for x,y in patient_to_mutation.items():
#    print("Patient: " + str(x) + ", " + "Mutation: " + str(y))
#for patient in radiation_cases:
#    print("Patient: " + str(patient) + " ->\n " + str(patient_to_mutation.get(patient))+"\n")
#print(mutations.columns)