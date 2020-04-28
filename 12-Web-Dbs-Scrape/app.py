from flask import Flask, render_template
import pymongo

app = Flask(__name__)

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.mars_db

# Next, create a route called /scrape that will import your scrape_mars.py
# script and call your scrape function.
@app.route('/scrape')
def scrape():
    import scrape_mars
    # Store the return value in Mongo as a Python dictionary.
    mars_data = scrape_mars.scrape()
    db.data.drop()
    print(mars_data)
    db.data.insert(mars_data)
    return "<script>window.onload=location.replace('/..')</script>"

# Create a root route / that will query your Mongo database and pass the mars
# data into an HTML template to display the data.
@app.route('/')
def index():
    return render_template('index.html', data=db.data.find_one())

# Create a template HTML file called index.html that will take the mars data
# dictionary and display all of the data in the appropriate HTML elements. Use
# the following as a guide for what the final product should look like, but
# feel free to create your own design.

if __name__ == "__main__":
    app.run(debug=True)