from flask import Flask, render_template, url_for

app = Flask(__name__)

# Home page (index.html)
@app.route('/')
def home():
    bg_imgs = [url_for('static', filename=f'images/img{i}.jpg') for i in range(1, 13)]
    return render_template("index.html", bg_imgs=bg_imgs)

# Services page
@app.route('/services')
def services():
    return render_template("services.html")

# Destination page
@app.route('/destination')
def destination():
    return render_template("destination.html")

# Booking page
@app.route('/booking')
def booking():
    return render_template("booking.html")

# Testimonial page
@app.route('/testimonial')
def testimonial():
    return render_template("testimonial.html")

# Contact page
@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/temple-tours')
def temple_tours():
    return render_template('temple_tours.html')


@app.route('/wildlife-trips')
def wildlife_trips():
    return render_template('wildlife-trips.html')

@app.route('/beach-holidays')
def beach_holidays():
    return render_template('beach-holidays.html')

@app.route('/cultural')
def cultural():
    return render_template('cultural.html')

@app.route("/bihar")
def bihar():
    return render_template("bihar.html")

@app.route("/andhra-pradesh")
def andhra_pradesh():
    return render_template("Andhra-Pradesh.html")

@app.route("/assam")
def Assam():
    return render_template("Assam.html")


@app.route("/chhattisgarh")
def chhattisgarh():
    return render_template("chhattisgarh.html")

@app.route("/delhi")
def delhi():
    return render_template("delhi.html")

@app.route("/goa")
def goa():
    return render_template("goa.html")

@app.route("/gujarat")
def gujarat():
    return render_template("gujarat.html")

if __name__ == "__main__":
    app.run(debug=True)
