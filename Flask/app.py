from flask import Flask, render_template 

app = Flask (__name__)

headings = ("Name","Address","Age", "Position", "Salary", "Company")
data =(
    ("Dave Lyndrex Millan","Dalaguete,Cebu", 20, "Quality Assurance", 15000, "Trust Arc"),
    ("Kerwein Bengil","Ginatilan, Cebu", 20, "Software Engineer", 15000, "Cloud Ninja"),
    ("Junmar Layaog","Bantayan, Cebu", 20, "Dev Ops", 15000, "Accenture"),
    ("April Grace Diez","Medillin, Cebu", 21, "Project Manager", 20000, "Chronostep"),
    ("Christine Rubio","Medillin, Cebu", 21, "Backend Developer", 15000, "DNA Micro"),
    ("Eleasar Patot","Dalaguete, Cebu", 20, "Frontend Developer", 15000, "Datwords")
    

)

@app.route("/")
def component():
    return render_template("table.html", headings= headings, data=data)

