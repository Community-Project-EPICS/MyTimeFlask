from flask import Flask, render_template


app = Flask(__name__)

'''@app.route('/')
def hello_world():
    return 'Hello, World!' '''

@app.route("/")


@app.route("/results")
def results():
    return render_template("result.html")

@app.route("/PredictedResults")
def predictionresult():
    return render_template("predictionresult.html")

@app.route("/index")
def index():
    return render_template("index.html")






#navbar elements

@app.route("/about")
def home():
    return render_template("about.html")

@app.route("/blogs")
def blog():
    return render_template("blog.html")

@app.route("/Achievements")
def Achievements():
    return render_template("Achievements.html")

@app.route("/contact_us")
def contact_us():
    return render_template("contact.html")


#start button - index.html-> Activities

@app.route("/ActivitiesForYou")
def secondpage():
    return render_template("Secondpage.html")


# Medical checkup
@app.route("/DiseaseDescription")
def DiseaseDescription():
    return render_template("DiseaseDescription.html")


@app.route("/CancerForm")
def cancerForm():
    return render_template("cancerForm.html")

@app.route("/DiabetesForm")
def DiabetesForm():
    return render_template("diabetesForm.html")


@app.route("/HeartForm")
def heartForm():
    return render_template("heartForm.html")

@app.route("/LiverForm")
def LiverForm():
    return render_template("liverForm.html")


@app.route("/KidneyForm")
def KidneyForm():
    return render_template("kidneyForm.html")

@app.route("/MalariaForm")
def malariaForm():
    return render_template("malariaForm.html")

@app.route("/PneumoniaForm")
def pneumoniaForm():
    return render_template("pneumoniaForm.html")




if __name__ == "__main__":
    app.run(debug='True')
    
