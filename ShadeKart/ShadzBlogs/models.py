from django.db import models


# Create your models here.
class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    writer = models.CharField(max_length=60, default="Anonymous")
    email = models.EmailField(max_length=80, default="")
    title = models.CharField(max_length=50, default="")
    thumbnail = models.ImageField(upload_to='ShadzBlogs/images')
    head0 = models.CharField(max_length=500, default="")
    content_head0 = models.CharField(max_length=5000, default="")
    head1 = models.CharField(max_length=500, default="")
    content_head1 = models.CharField(max_length=5000, default="")
    head2 = models.CharField(max_length=500, default="")
    content_head2 = models.CharField(max_length=5000, default="")
    published_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
