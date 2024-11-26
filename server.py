from flask import Flask, render_template, url_for, request, redirect
import csv


# Create an instance of the Flask class, which is the core of a Flask application.
app = Flask(__name__)

# This will print the name of the module or script being executed, typically "__main__" if run directly.
print(__name__)

# To run the Flask app, you need to set the environment variable FLASK_APP to the name of the Python 
#file (e.g., 'server.py'), and use the command `flask run` to start the server.

# The following command enables debugging. When enabled, changes to your code will automatically reflect in the browser 
# without needing to restart the server, and you will see detailed error messages (stack traces) in the terminal.
# To run in debug mode, use: `flask --app server.py run --debug`.

# Routes in Flask map URLs to functions. Each route corresponds to a specific URL pattern.
# The functions determine what content is returned when that URL is accessed.
# For example, visiting '/' will invoke the hello_world function, while visiting '/about.html' will invoke the about function.

# Define a route for the root URL ("/") with dynamic URL parameters.
# When a URL like "/<username>/<int:post_id>" is visited, it triggers the hello_world function and passes
# the 'username' and 'post_id' from the URL as arguments.
# @app.route("/<username>/<int:post_id>")
# def hello_world(username=None, post_id=None):
#     # Render the 'index.html' template, passing the username and post_id to it for dynamic content rendering.
#     return render_template('index.html', name=username, post_id=post_id)

# Define a route for "/about.html" that renders the 'about.html' template when accessed.
# @app.route("/works")
# def works():
#     return render_template('works.html')


@app.route("/")
def my_home():
    # Render the 'index.html' template, passing the username and post_id to it for dynamic content rendering.
    return render_template('index.html')


# Render pages dynamically
@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    # error = None
    if request.method == 'POST':
        try:
            data = request.form.to_dict()  # gets the information in dictionary form
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong'

def write_to_file(data):
    with open('database.txt', mode='a') as dbase:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = dbase.write(f"\n{email}, {subject}, {message}")

def write_to_csv(data):
    with open('database.csv', mode='a', newline='',) as dbase2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(dbase2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message]) # provide the variable of what we want, declared above


# Example of another route (commented out) for serving a favicon (icon displayed in the browser tab).
# If you choose to implement it, the favicon.ico file should be placed in the static folder, and the route will serve it.
# @app.route("/favicon.ico")
# def favico():
#     return render_template('favico.html')

# Define a route for a specific blog post ("/blog/2024/dogs"). 
# This route returns a simple HTML string instead of rendering a template.
# @app.route("/blog/2024/dogs")
# def blogdog():
#     return "<p>Blog on dogs!</p>"

# The app.run() method would be used here if you were running the app directly from the Python script.
