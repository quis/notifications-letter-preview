import os
import subprocess
from datetime import datetime

now = datetime.utcnow()

html_file = os.path.abspath('./letter.html')
pdf_path = os.path.abspath('./output/example-{}.pdf'.format(now))

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

exit_code = subprocess.call([
    'pdftoppm',
    '-singlefile',
    '-png',
    pdf_path,
    'example-{}'.format(now),
])

exit_code = subprocess.call([
    'mv',
    'example-{}.png'.format(now),
    'output/',
])

if exit_code > 0:
    print("ERROR: {} on {}".format(exit_code, html_file))
