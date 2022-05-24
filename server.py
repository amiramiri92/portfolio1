from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__) #create app flask (flask application)
#print(__name__)

#different route for URL
"""
@app.route('/')    #decorator  #home route
def hello_world():
    #print(url_for('static', filename='favicon.ico'))
    #return 'Hello, World I\'m amir it\'s really great we have ya, we love ya, we hope we can see you soon and you have great moments :) :) :) ID:1234567890 !'
    return render_template('./index.html')  #for opening the html file

@app.route('/about')    #decorator  #home route
def about():
    return render_template('./about.html')

@app.route('/blog')    #blog route
def blog():
    return 'these are my thoughts on blogs'

#using two above decorators we have now multiple routes

@app.route('/blog/2022/dogs')    #another blog route
def blog2():
    return 'this is my dog'


@app.route('/favicon.ico')    #favicon.ico route
def favicon():
    return 'these are my thoughts on blogs'

"""

"""
@app.route('/<username>/<int:post_id>')    
def hello_world(username=None, post_id=None):  #None is default value for username
    return render_template('./index.html', name=username, post_id=post_id)
"""

#for our ready html file
@app.route('/')    #decorator  #home route
def my_home():
    return render_template('./index.html')

"""
@app.route('/index.html')    #decorator  #home route
def home():
    return render_template('./index.html')

@app.route('/works.html')    #decorator  #work route
def works():
    return render_template('./works.html')

@app.route('/about.html')    #decorator  #about route
def about():
    return render_template('./about.html')

@app.route('/contact.html')    #decorator  #contact route
def contact():
    return render_template('./contact.html')

@app.route('/components.html')    #decorator  #components route
def components():
    return render_template('./components.html')
""" 
# dynamic diffrent routs ddd
@app.route('/<string:page_name>')    #decorator  #home route
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):  #this is our database
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n {email},{subject},{message}')

def write_to_csv(data):  #this is our database
    with open('database.csv', mode='a', newline='') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter= ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET']) 
def submit_form():
    #return render_template('login.html', error=error)
    #return 'form submitted hooray'
    if request.method == 'POST':
        try:
            #data = request.form[email]
            data = request.form.to_dict()
            #print (data)
            #write_to_file(data)
            write_to_csv(data)
            #return 'form submitted'
            return redirect('/thankyou.html') #this is for answering back a recieving message
        except:
            return 'did not save to database'
    else:
        return 'something went wrong, try again'