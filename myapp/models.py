from django.db import models
from django.contrib.auth.models import User
from datetime import datetime  

now = datetime.now()
time = now.strftime("%d %B %Y")

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Post Model
class Post(models.Model):
    postname = models.CharField(max_length=600)
    category = models.CharField(max_length=100)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts', null=True, blank=True)
    image = models.ImageField(upload_to='images/posts', blank=True, null=True)
    content = models.CharField(max_length=100000)
    time = models.CharField(default=time, max_length=100, blank=True)
    likes = models.IntegerField(null=True, blank=True, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.postname)

# Comment Model
class Comment(models.Model):
    content = models.CharField(max_length=200)
    time = models.CharField(default=time, max_length=100, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}.{self.content[:20]}..."

# Contact Model
class Contact(models.Model):
    name = models.CharField(max_length=600)
    email = models.EmailField(max_length=600)
    subject = models.CharField(max_length=1000)
    message = models.CharField(max_length=10000, blank=True)


 #  artical model
 



class ArticleSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    title = models.CharField(max_length=200)
    document = models.FileField(upload_to='submissions/')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

 #  advertisement model
class AdvertiseInquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry from {self.name} ({self.email})"
    

    # our story model
    # models.py


class TravelStory(models.Model):
    title = models.CharField(max_length=200)
    author_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    chapter_0 = models.TextField(verbose_name="Planning Ki Hungama")
    chapter_1 = models.TextField(verbose_name="Safar Ka Shuruaat")
    chapter_2 = models.TextField(verbose_name="Pahaadon Ki Goanj")
    chapter_3 = models.TextField(verbose_name="Adventure Mode ON")
    chapter_4 = models.TextField(verbose_name="Yaadein Jo Hamesha Saath Rahengi")
    chapter_5 = models.TextField(verbose_name="Photo Session Aur Reels Ki Duniya", blank=True)
    chapter_6 = models.TextField(verbose_name="Khaane Peene Ka Connection", blank=True)
    chapter_7 = models.TextField(verbose_name="Souvenir Shopping & Tofe Wale Moments", blank=True)

    def __str__(self):
        return f"{self.title} by {self.author_name}"
    

    # team model
    from django.db import models

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='team/', blank=True, null=True)

    def __str__(self):
        return self.name


# careers model
# from django.db import models

class JobOpening(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class JobApplication(models.Model):
    job = models.ForeignKey(JobOpening, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    message = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.job.title}"
        


   
