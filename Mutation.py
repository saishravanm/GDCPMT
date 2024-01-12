
from Patient import Patient
class Mutation:
    def __init__(self,dna_change,type,consequences,impact):
        self.dna_change = dna_change
        self.type = type
        self.consequences = consequences
        self.impact = impact
    def __str__(self):
        return self.dna_change
        #print("DNA Change: " + self.dna_change + "\nType: " + self.type + "\nConsequences: " + self.consequences+"\nImpact: " + self.impact + "\nPatient List: ")