from flask import Flask, render_template, request, redirect, url_for, make_response
from flask_weasyprint import render_pdf

from get_listing_data import get_listing_data
from weasyprint import HTML

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/pregled", methods=["POST", "GET"])
def pregled():
    if request.method == "POST":
        try:
            # get listing url
            print(request.form["listingURL"])
            listing = get_listing_data(request.form["listingURL"])
            return render_template("pregled.html", listing=listing)
        except:
            # redirect to home page
            print("Error pregled")
            return redirect("/")

@app.route("/pdf", methods=["POST", "GET"])
def pdf():
    if request.method == "POST":
        #try:
            # Get the info
        title = request.form["title"]
        offer = request.form["offer"]
        type_o = request.form["type_o"]
        size = request.form["size"]
        size_l = request.form["size_l"]
        year = request.form["year"]
        price = request.form["price"]
        short = request.form["short"]
        long = request.form["long"]
        images_array = request.form.getlist("image")
        # render the PDF
        html = render_template('pdf_template.html', title=title, offer=offer, type_o=type_o, size=size, size_l=size_l, year=year, price=price, short=short, long=long, images_array=images_array)
        #html = render_template('report.html')
        return render_pdf(HTML(string=html))
        #return create_pdf(title=title, offer=offer, type_o=type_o, size=size, size_l=size_l, year=year, price=price, short=short, long=long, images_array_base64=images_array_base64)
        '''except:
            # redirect to home page
            print("Error pdf")
            return redirect("/")'''
# ta vrstica preveri, da klicemo neposredno
if __name__ == '__main__':
    app.run(debug=True)
