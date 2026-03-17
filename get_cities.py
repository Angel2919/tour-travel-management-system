from flask import Flask, request, render_template_string
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# Database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="traveldb"
)
mycursor = mydb.cursor()

@app.route('/get_cities_form', methods=['POST'])
def get_cities_form():
    state = request.form['state']
    mycursor.execute("SELECT city_name FROM state_city WHERE state_name = %s", (state,))
    cities = [row[0] for row in mycursor.fetchall()]
    html = """
    <h2>Cities in {{state}}</h2>
    <form>
        <select>
            {% for city in cities %}
            <option>{{ city }}</option>
            {% endfor %}
        </select>
    </form>
    """
    return render_template_string(html, state=state, cities=cities)

if __name__ == '__main__':
    app.run(debug=True)
