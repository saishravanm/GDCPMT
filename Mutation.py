
from Patient import Patient
class Mutation:
    def __init__(self,dna_change,type,consequences,impact,associated_patient_list):
        self.dna_change = dna_change
        self.type = type
        self.consequences = consequences
        self.impact = impact
        self.associated_patient_list = associated_patient_list
    def __str__(self):
        self.associated_patient_list = Patient(self.associated_patient_list)
        print("DNA Change: " + self.dna_change + "\nType: " + self.type + "\nConsequences: " + self.consequences+"\nImpact: " + self.impact + "\nPatient List: " + self.associated_patient_list)
    def print_patient_list(self):
        return (str(self.associated_patient_list))