import os
import subprocess

import pdfkit
import platform
from flask import render_template, make_response


def create_pdf(title, offer, type_o, size, size_l, year, price, short, long, images_array_base64):
    if 'DYNO' in os.environ:
        print('loading wkhtmltopdf path on heroku')
        WKHTMLTOPDF_CMD = subprocess.Popen(
            ['which', os.environ.get('WKHTMLTOPDF_BINARY', 'wkhtmltopdf-pack')],
            # Note we default to 'wkhtmltopdf' as the binary name
            stdout=subprocess.PIPE).communicate()[0].strip()
    else:
        print('loading wkhtmltopdf path on localhost')
        WKHTMLTOPDF_CMD = 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_CMD)
    options = {
        'page-size': 'A4',
        'encoding': "UTF-8",
    }
    render = render_template('pdf_template.html', title=title, offer=offer, type_o=type_o, size=size, size_l=size_l, year=year, price=price, short=short, long=long, images_array_base64=images_array_base64)
    pdf = pdfkit.from_string(render, False, options=options, configuration=config)
    # create response from rendered PDF
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename='+title+'.pdf'
    return response
