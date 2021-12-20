from flask import Flask, render_template, session, request
from flask.helpers import make_response
app=Flask(__name__)

app.config["SECRET_KEY"]="aditi2849"
user_details = {"prakruthi": "ihturkarp", "user" : "abc123" , "aditi":"itida"}
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/prakruthi")
def prakruthi():
    return "<h1> Hi me </h1>"

@app.route("/babysister")
def aditi():
    return "<h1> Hi little aditi </h1>"

@app.route("/mywebsite")
def website():
    return "<h1> Welcome to Prakruthi's Website </h1>"

@app.route("/art")
def art():
    return render_template("MyArtCreations.html")

@app.route("/craft")
def craft():
    return render_template("MyCraftCreations.html")

@app.route("/recipes")
def recipes():
    return render_template("GridRecipes.html")

@app.route("/quiz")
def quiz():
    return render_template("startquiz.html")

@app.route("/Login",methods=["get","POST"])
def login():
    if session .get("authenticated")== True:
        return render_template("loginsuccess.html")
    else: 
        return render_template("Login.html")

@app.route("/user_validation",methods=["POST"])
def user_validation():
    username=request.form.get("username")
    password=request.form.get("password")
    returnvalue=loginsuccess(user_details,username,password)
    if returnvalue==True:
        session["authenticated"]=True
        return render_template("loginsuccess.html",username=username)
    else:
        return render_template("loginfailure.html")

def loginsuccess(dictionary,username,password):
    if dictionary .get(username,"User not found")==password:
        return True
    else:
        return False

@app.route("/Register")
def register():
    return render_template("Registration.html")

@app.route("/register_verify",methods=["post"])
def register_verify():
    username=request.form.get("username")
    password=request.form.get("password")
    user_details[username]=password
    print(user_details)
    return render_template("registersuccess.html", username=username)


@app.route("/R1")
def R1():
    return render_template("R1.html")

@app.route("/R2")
def R2():
    return render_template("R2.html")

@app.route("/R3")
def R3():
    return render_template("R3.html")

@app.route("/R4")
def R4():
    return render_template("R4.html")

@app.route("/R5")
def R5():
    return render_template("R5.html")

@app.route("/R7")
def R7():
    return render_template("R7.html")


@app.route("/gemq1")
def gemq1():
    return render_template("gemq1.html",score=0)

@app.route("/gemq2",methods=["POST"])
def gemq2():
    p_score=session.get("score",0)
    c_score=p_score
    s_answer=request.form.get("question")
    c_answer=request.form.get("ca")
    print(s_answer,c_answer)
    print(c_score, p_score)
    q_attempted_dict=session.get("q_attempted",{})
    if s_answer==c_answer:
        marks=20
        if q_attempted_dict.get("1",False)==False:
            c_score=p_score+marks
            session["score"]=c_score
    q_attempted_dict["1"]=True
    return render_template("gemq2.html",score=c_score)

@app.route("/gemq3",methods=["POST"])
def gemq3():
    p_score=session.get("score",0)
    c_score=p_score
    s_answer=request.form.get("question")
    c_answer=request.form.get("ca")
    q_attempted_dict=session.get("q_attempted",{})
    if s_answer==c_answer:
        marks=20
        if q_attempted_dict.get("2",False)==False:
            c_score=p_score+marks
            session["score"]=c_score
    q_attempted_dict["2"]=True
    return render_template("gemq3.html", score=c_score)

@app.route("/gemq4",methods=["POST"])
def gemq4():
    p_score=session.get("score",0)
    c_score=p_score
    s_answer=request.form.get("question")
    c_answer=request.form.get("ca")
    q_attempted_dict=session.get("q_attempted",{})
    if s_answer==c_answer:
        marks=20
        if q_attempted_dict.get("3",False)==False:
            c_score=p_score+marks
            session["score"]=c_score
        q_attempted_dict["3"]=True
    return render_template("gemq4.html", score=c_score)

@app.route("/gemq5",methods=["POST"])
def gemq5():
    p_score=session.get("score",0)
    c_score=p_score
    s_answer=request.form.get("question")
    c_answer=request.form.get("ca")
    q_attempted_dict=session.get("q_attempted",{})
    if s_answer==c_answer:
        marks=20
        if q_attempted_dict.get("4",False)==False:
            c_score=p_score+marks
            session["score"]=c_score
    q_attempted_dict["4"]=True
    return render_template("gemq5.html", score=c_score)

@app.route("/gemresult",methods=["POST"])
def gemresult():
    p_score=session.get("score",0)
    c_score=p_score
    return render_template("gemresult.html",score=c_score)

@app.route("/fantasyq1")
def fantasyq1():
    return render_template("fantasyq1.html",score1=0)
    
@app.route("/fantasyq2", methods=["POST"])
def fantasyq2():
    p_score1=session.get("score1",0)
    c_score1=p_score1
    s_answer1=request.form.get("question")
    c_answer1=request.form.get("ca")
    q_attempted_dict=session.get("q_attempted",{})
    print(c_score1, p_score1)
    print(s_answer1,c_answer1)
    if s_answer1==c_answer1:
        marks=20
        if q_attempted_dict.get("1",False)==False:
            c_score1=p_score1+marks
            session["score1"]=c_score1
        q_attempted_dict["1"]=True
    return render_template("fantasyq2.html", score1=c_score1)


@app.route("/fantasyq3", methods=["POST"])
def fantasyq3():
    p_score1=session.get("score1",0)
    c_score1=p_score1
    s_answer=request.form.get("question")
    c_answer=request.form.get("ca")
    q_attempted_dict=session.get("q_attempted",{})
    if s_answer==c_answer:
        marks=20
        if q_attempted_dict.get("2",False)==False:
            c_score1=p_score1+marks
            session["score1"]=c_score1
        q_attempted_dict["2"]=True
    return render_template("fantasyq3.html", score1=c_score1)


@app.route("/fantasyq4", methods=["POST"])
def fantasyq4():
    p_score1=session.get("score1",0)
    c_score1=p_score1
    s_answer=request.form.get("question")
    c_answer=request.form.get("ca")
    q_attempted_dict=session.get("q_attempted",{})
    if s_answer==c_answer:
        marks=20
        if q_attempted_dict.get("3",False)==False:
            c_score1=p_score1+marks
            session["score1"]=c_score1
        q_attempted_dict["3"]=True
    return render_template("fantasyq4.html", score1=c_score1)

@app.route("/fantasyq5", methods=["POST"])
def fantasyq5():
    p_score1=session.get("score1",0)
    c_score1=p_score1
    s_answer=request.form.get("question")
    c_answer=request.form.get("ca")
    q_attempted_dict=session.get("q_attempted",{})
    if s_answer==c_answer:
        marks=20
        if q_attempted_dict.get("4",False)==False:
            c_score1=p_score1+marks
            session["score1"]=c_score1
        q_attempted_dict["4"]=True
    return render_template("fantasyq5.html", score1=c_score1)

@app.route("/fantasyresult", methods=["POST"])
def fantasyresult():
    p_score1=session.get("score1",0)
    c_score1=p_score1
    s_answer=request.form.get("question")
    c_answer=request.form.get("ca")
    q_attempted_dict=session.get("q_attempted",{})
    if s_answer==c_answer:
        marks=20
        if q_attempted_dict.get("5",False)==False:
            c_score1=p_score1+marks
            session["score1"]=c_score1
        q_attempted_dict["5"]=True
    return render_template("fantasyresult.html")

@app.route("/petq1")
def petq1():
    return render_template("petq1.html")

@app.route("/petq2")
def petq2():
    return render_template("petq2.html")

@app.route("/petq3")
def petq3():
    return render_template("petq3.html")

@app.route("/petq4")
def petq4():
    return render_template("petq4.html")

@app.route("/petresult")
def petresult():
    return render_template("petresult.html")

@app.route("/youq1")
def youq1():
    return render_template("youq1.html")

@app.route("/youq2")
def youq2():
    return render_template("youq2.html")

@app.route("/youq3")
def youq3():
    return render_template("youq3.html")
    















if __name__=="__main__":
    app.run(debug=True)  