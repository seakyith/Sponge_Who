from flask import Flask, request, render_template
from . import app


# Home Page
@app.route('/', methods=["GET","POST"])
@app.route('/home', methods=["GET","POST"])
def qoute_generator():
    if request.method=="POST":# Catch Post Form
        query=request.form['query']
        if query:# if Non-empty query
            
            return render_template('home.html')## might need to change html name
        else:
            return render_template('home.html',message="No query detected") #might need to change
    else:  ## get method 
        return render_template('home.html',message="Search for a qoute",query_results='') #might need to change html name

# Future Pages