print("Content-Type: text/html\n")
from flask import *
from model import *
app = Flask(__name__)

@app.route("/")
#def show_patmut():
#    return render_template('table.html',tables=[patmut.to_html(classes='patients')],titles=patmut.columns.values)
def show_home():
    return render_template('home.html',dec_pharma_patnames=final_pharma)
@app.route("/pharma/<pharmapat>")
def create_profile(pharmapat=None):
    patient = patient_list[pharmapat]
    return render_template('patient.html',pharmapat=pharmapat,patient=patient,info=str(patient))
    