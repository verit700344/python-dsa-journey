from flask import Flask, request, redirect
import hashlib

app = Flask(__name__)
url_map = {}

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form['url']
    code = hashlib.md5(long_url.encode()).hexdigest()[:6]
    url_map[code] = long_url
    return f"Short URL: /{code}"

@app.route('/<code>')
def redirect_url(code):
    return redirect(url_map.get(code, '/'))

if __name__ == '__main__':
    app.run(debug=True)
