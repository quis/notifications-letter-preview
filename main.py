import os
import subprocess
from datetime import datetime

html_file = os.path.abspath('./letter.html')
pdf_path = os.path.abspath('./output/example-{}.pdf'.format(datetime.utcnow()))

exit_code = subprocess.call([
    'wkhtmltopdf',
    '--print-media-type',
    '-T',
    '5mm',
    '-R',
    '10mm',
    '-B',
    '40mm',
    '-L',
    '10mm',
    'file://{}'.format(html_file),
    pdf_path,
])

if exit_code > 0:
    print("ERROR: {} on {}".format(exit_code, html_file))
