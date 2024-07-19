from flask import Flask, render_template
from post import Post
import requests

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
all_posts = requests.get(blog_url).json()
post_objs = []

for post in all_posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objs.append(post_obj)


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", posts=post_objs)

@app.route("/blog/<int:num>")
def get_post(num):
    target_post = None
    for blog_post in post_objs:
        if blog_post.id == num:
            target_post = blog_post
    return render_template("post.html", post=target_post)

if __name__ == "__main__":
    app.run(debug=True)