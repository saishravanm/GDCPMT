class Treatment:
    def __init__(self, case_submitter_id,barcode,form_completion):
        self.case_submitter_id = case_submitter_id
        self.barcode = barcode 
        self.form_completion = form_completion

class Radiation(Treatment):
    def __init__(self, case_submitter_id, barcode, radiation_uuid, form_completion,radiation_therapy_type,radiation_therapy_site,radiation_total_dose,radiation_adjuvant_units,radiation_adjuvant_fractions_total,radiation_therapy_started_days_to,radiation_therapy_ended_days_to,treatment_best_response,course_number,therapy_regimen):
        super().__init__(case_submitter_id, barcode, form_completion)
        self.radiation_uuid = radiation_uuid
        self.radiation_therapy_type = radiation_therapy_type
        self.radiation_therapy_site = radiation_therapy_site
        self.radiation_total_dose = radiation_total_dose
        self.radiation_adjuvant_units = radiation_adjuvant_units
        self.radiation_adjuvant_fractions_total = radiation_adjuvant_fractions_total
        self.radiation_therapy_started_days_to = radiation_therapy_started_days_to
        self.radiation_therapy_ended_days_to = radiation_therapy_ended_days_to
        self.treatment_best_response = treatment_best_response
        self.course_number = course_number
        self.form_completion = form_completion
        self.therapy_regimen = therapy_regimen

class Pharmaceutical(Treatment):
    def __init__(self, case_submitter_id,barcode, drug_uuid, form_completion,drug_name,clinical_trial_drug_classification,therapy_type,days_to_drug_therapy_start,days_to_drug_therapy_end,measure_of_response,number_cycles,therapy_type_notes,prescribed_dose_units,total_dose_units,prescribed_dose,regimen_number,route_of_administration,regimen_indication,total_dose,tx_on_clinical_trial):
        super().__init__(case_submitter_id, barcode, form_completion)
        self.drug_uuid = drug_uuid 
        self.form_completion = form_completion
        self.drug_name = drug_name 
        self.clinical_trial_drug_classification = clinical_trial_drug_classification
        self.therapy_type = therapy_type
        self.days_to_drug_therapy_start = days_to_drug_therapy_start
        self.days_to_drug_therapy_end = days_to_drug_therapy_end
        self.measure_of_response = measure_of_response
        self.number_cycles = number_cycles
        self.therapy_type_notes = therapy_type_notes
        self.prescribed_dose_units = prescribed_dose_units
        self.total_dose_units = total_dose_units
        self.prescribed_dose = prescribed_dose
        self.regimen_number = regimen_number
        self.route_of_administration = route_of_administration
        self.regimen_indication = regimen_indication
        self.total_dose = total_dose
        self.tx_on_clinical_trial = tx_on_clinical_trial

