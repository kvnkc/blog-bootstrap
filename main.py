from flask import Flask, render_template
import requests

url = 'https://api.npoint.io/26c825f61288fbbd5782'
response = requests.get(url=url)
post_data = response.json()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('./index.html', posts=post_data)


@ app.route('/contact')
def contact():
    return render_template('./contact.html')


@ app.route('/about')
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
