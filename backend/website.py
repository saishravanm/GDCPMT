print("Content-Type: text/html\n")
from flask import *
from model import *
app = Flask(__name__)

@app.route("/")
#def show_patmut():
#    return render_template('table.html',tables=[patmut.to_html(classes='patients')],titles=patmut.columns.values)
def show_home():
    return render_template('home.html',dec_rad_patnames=deceased_radiation_case_ids)
@app.route("/radiation/<radpat>")
def create_profile(radpat=None):
    patient = patient_list[radpat]
    return render_template('patient.html',radpat=radpat,patient=patient,info=str(patient))
    