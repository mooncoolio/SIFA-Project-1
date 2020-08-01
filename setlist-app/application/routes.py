# import render_template function from the flask module
from flask import render_template
# import the app object from the ./application/__init__.py
from application import app


#test data for app
testData = [
    {  
        "song": {"name":"Running (Disclosure Remix)", "album":"Settle", "artist": "Jessie Ware", "key": "Em", "bpm": "125" },
        "set_list":"One for the boyos",
    },
    {   
        "song": {"name":"Your Love Will Set You Free", "album":"Our Love", "artist": "Caribou", "key": "Cm", "bpm": "125" },
        "set_list":"One for the boyos",     
    },
    {   
        "song": {"name":"Darko (Booka's Funk da Funk mix)", "album":"Azuli Presents: Space: Ibiza 2007", "artist": "Booka Shade", "key": "Fm", "bpm": "125" },
        "set_list":"One for the boyos",     
    }

]




# define routes for /,  /home, /create, /view & /edit  this function will be called when these are accessed
@app.route('/')
@app.route('/home')
def home():
 return render_template('home.html', title='Home')

@app.route('/create')
def create():
 return render_template('create.html', title='Create')

@app.route('/view')
def view():
 return render_template('view.html', title='View', posts=testData)

@app.route('/edit')
def edit():
 return render_template('edit.html', title='Edit')
