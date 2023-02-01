#Our API consist JSON that have 4 pairs of keys-values objects.
#we will create a class named Post which will have same atributes as the API 

class Post:
    def __init__(self, post_id, title, subtitle, body):  #class init func
        self.id = post_id
        self.title = title
        self.subtitle = subtitle
        self.body = body

#from now we can assaign values to an  property of object from the Post class like this:
# blog_post.id = index (we will see it in main)
