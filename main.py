from flask import Flask, render_template, request
import requests

url = 'https://api.npoint.io/26c825f61288fbbd5782'
response = requests.get(url=url)
post_data = response.json()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('./index.html', posts=post_data)


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'GET':
        return render_template('./contact.html')
    elif request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return (f'<h1> Form for {name} {email} successfully submitted </h1>')


@app.route('/about')
def about():
    return render_template('./about.html')


@app.route('/post/<int:post_id>')
def post(post_id):
    for post in post_data:
        if post_id == post['id']:
            requested_post = post
    return render_template('./post.html', post=requested_post)


if __name__ == '__main__':
    app.run(debug=True)
