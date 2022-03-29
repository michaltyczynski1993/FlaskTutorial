from app import app
from flask import render_template

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

    
    return render_template(
        "public/jinja.html", my_name=my_name, age=age, 
        langs=langs, friends=friends, colours=colours, 
        cool=cool, GitRemote=GitRemote, repeat=repeat, 
        my_remote=my_remote)

@app.route("/about")
def about():
    return "It is about Page"