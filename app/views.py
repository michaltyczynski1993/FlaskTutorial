from urllib import response
from app import app
from flask import render_template, request, redirect, jsonify, make_response

@app.route("/")
def index():
    return render_template('public/index.html')

@app.route("/jinja")
def jinja():

    my_name = "Michal"
    age = 30
    
    langs = ['Python', 'Java', 'JavaScript', 'Bash', 'HTML', 'C', 'Ruby']

    friends = {
        'Tomek': 25,
        'Maja': 30,
        'Iza': 29,
        'Grzegorz': 20
    }

    colours = ('Red', 'Green')

    cool = True

    class GitRemote():
        def __init__(self, name, description, url):
            self.name = name
            self.description = description
            self.url = url
        
        def pull(self):
            return f'Pulling repo {self.name}'
        
        def clone(self):
            return f'Cloning repo {self.url}'
    
    my_remote = GitRemote(
        name= 'Flask Tutorial', 
        description='Template design tutorial', 
        url='https://github.com/julian-nash/jinja.git')
        
    
    def repeat(x, qty):
        return x * qty

    my_html = '<h1>This is my html</h1>'
    
    return render_template(
        "public/jinja.html", my_name=my_name, age=age, 
        langs=langs, friends=friends, colours=colours, 
        cool=cool, GitRemote=GitRemote, repeat=repeat, 
        my_remote=my_remote, my_html=my_html)

@app.route("/about")
def about():
    return "It is about Page"

@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    
    if request.method == "POST":

        req = request.form
        
        username = req["username"]
        email = req["email"]
        password = req["password"]
        
        print(username, email, password)
        print(request.url)
        
        return redirect(request.url)

    return render_template("public/sign_up.html")


users = {
    "mitsuhiko":{
        "name": "Armin Ronaher",
        "bio": "Creator of the flask freamwork",
        "twitter_handle": "@mitsuhiko"
    },
    "gvanrossum":{
        "name": "Guido Van Rossum",
        "bio": "Creator of Python programming language",
        "twitter_handle": "@gvanrossum"
    },
    "elonmusk":{
        "name": "Elon Musk",
        "bio": "tehnology entrepreneur, investor and engineer",
        "twitter_handle": "@elonmusk"
    }
}
@app.route("/profile/<username>")
def profile(username):

    user = None
    if username in users:
        user = users[username]

    return render_template("/public/profile.html", user=user, username=username)

@app.route("/json", methods=['POST'])
def json():
    
    if request.is_json:
        req = request.get_json()
        response = {
            "message": "JSON received",
            "name": req.get("name")
        }
        res = make_response(jsonify(response), 200)
        return res
    else:
        res = make_response(jsonify({"message": "No JSON received"}), 400)
        return res