from flask import Flask, request, send_file, render_template
from flask_qrcode import QRcode

app = Flask(__name__)
QRcode(app)

print('123')

@app.route('/')
def home():
	return 'This is a suite of tools for Ando Living'


@app.route('/qrcode')
def make_qr():
	url = request.args.get('url')
	print(url)
	if not url:
		return "Please provide a link like /qrcode?url=https://google.com"
	return render_template('qr.html', url=url)
	


if __name__ == '__main__':
	print(app)
	app.run()