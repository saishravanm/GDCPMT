
class Mutation:
    def __init__(self,dna_change,type,consequences,impact):
        self.dna_change = dna_change
        self.type = type
        self.consequences = consequences
        self.consequence_type = self.consequences.split(" ")[0]
        self.impact = impact
        temp = impact.split(",")
        self.vep = temp[0]
        self.sift = None
        self.sift_score = None
        self.polyphen_score = None
        self.polyphen = None
        if len(temp) >= 2:
            self.sift = temp[1]
            self.sift_score = float(self.sift.split(" ")[5])
            self.polyphen = temp[2].split(' ')[2]
            self.polyphen_score = float(temp[2].split(" ")[5])
    def __str__(self):
        #return self.dna_change
        return("DNA Change: " + self.dna_change + "\nType: " + self.type + "\nConsequences: " + self.consequences+"\nImpact: " + self.impact + "\n\n")