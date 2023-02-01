from flask import Flask, render_template
from post import Post
import requests

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
post_objects = []

for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])  #data from API values will assigned to class objects by the order of the class cretion .
    
    post_objects.append(post_obj)
    total_posts = len(post_objects)

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=post_objects,quantity=total_posts) #rendering index.html and passing to it all posts as params


@app.route("/post/<int:index>")  #Dynamic URL, index sent to func from index.html as param in the href, the relevant post data will be rendered in a different URL depends on index
def show_post(index): #func will get the same index as the url from index.html 
    requested_post = None   #creation of an empty varaible that will get value 
    for blog_post in post_objects:   #looping through post_objects list which is already list of objects from Post class
        if blog_post.id == index:    #blog_post is a Post class object, we will refer to the id as: blog_post.id , **Not as blog_post.post_id as we can think in the beginning*** 
            requested_post = blog_post      #requested_post will get the value of blog_post (Post class object)
    return render_template("post.html", post=requested_post)    #rendering post.html **With relevant post data by it index!!!**


if __name__ == "__main__":
    app.run(debug=True)


