import pdfkit
from flask import render_template, make_response


def create_pdf(title, offer, type_o, size, size_l, year, price, short, long, images_array_base64):
    #config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
    config = pdfkit.configuration(wkhtmltopdf='./bin/wkhtmltopdf')
    options = {
        'page-size': 'A4',
        'encoding': "UTF-8",
    }
    render = render_template('pdf_template.html', title=title, offer=offer, type_o=type_o, size=size, size_l=size_l, year=year, price=price, short=short, long=long, images_array_base64=images_array_base64)
    pdf = pdfkit.from_string(render, False, options=None, configuration=config)
    # create response from rendered PDF
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename='+title+'.pdf'
    return response
