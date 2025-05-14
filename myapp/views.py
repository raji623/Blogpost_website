from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Post, Category, Comment, Contact
from django.contrib import messages







# In views.py

def category_posts(request, category_id):
    # Get the category object using category_id
    category = get_object_or_404(Category, id=category_id)
    
    # Fetch all posts related to the selected category
    posts = Post.objects.filter(category=category).order_by("-id")
    
    # Render the category posts page with the posts and category name
    return render(request, "category_posts.html", {
        'category': category,
        'posts': posts,
        'media_url': settings.MEDIA_URL
    })



def index(request):
    return render(request, "index.html", {
        'posts': Post.objects.filter(user_id=request.user.id).order_by("-id"),
        'top_posts': Post.objects.all().order_by("-likes"),
        'recent_posts': Post.objects.all().order_by("-id"),
        'categories': Category.objects.all(),
        'user': request.user,
        'media_url': settings.MEDIA_URL
    })


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect('signup')
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists")
                return redirect('signup')
            else:
                User.objects.create_user(username=username, email=email, password=password).save()
                return redirect('signin')
        else:
            messages.info(request, "Passwords do not match")
            return redirect('signup')
    return render(request, "signup.html")


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("index")
        else:
            messages.info(request, 'Username or Password is incorrect')
            return redirect("signin")
    return render(request, "signin.html")


def logout(request):
    auth.logout(request)
    return redirect('index')


def blog(request):
    return render(request, "blog.html", {
        'posts': Post.objects.filter(user_id=request.user.id).order_by("-id"),
        'top_posts': Post.objects.all().order_by("-likes"),
        'recent_posts': Post.objects.all().order_by("-id"),
        'categories': Category.objects.all(),
        'user': request.user,
        'media_url': settings.MEDIA_URL
    })


# def create(request):
#     if request.method == 'POST':
#         try:
#             postname = request.POST['postname']
#             content = request.POST['content']
#             category_id = request.POST['category']
#             image = request.FILES.get('image', None)
#             category = Category.objects.get(id=category_id)
#             Post(postname=postname, content=content, category=category, image=image, user=request.user).save()
#         except Exception as e:
#             print("Error creating post:", e)
#         return redirect('index')
#     else:
#         return render(request, "create.html", {
#             'categories': Category.objects.all()
#         })
    
    #this block is working without sucsess message
# def create(request):
#     if request.method == 'POST':
#         try:
#             postname = request.POST['postname']
#             content = request.POST['content']
#             category_id = request.POST['category']
#             image = request.FILES.get('image', None)
#             category = Category.objects.get(id=category_id)
#             Post(postname=postname, content=content, category=category, image=image, user=request.user).save()
#         except Exception as e:
#             print("Error creating post:", e)
#         return redirect('index')
#     else:
#         return render(request, "create.html", {
#             'categories': Category.objects.all()
#         })
    


def create(request):
    if request.method == 'POST':
        try:
            postname = request.POST['postname']
            content = request.POST['content']
            category_id = request.POST['category']
            image = request.FILES.get('image', None)
            category = Category.objects.get(id=category_id)
            Post(postname=postname, content=content, category=category, image=image, user=request.user).save()

            # Add a success message
            messages.success(request, "Your blog post has been created successfully!")
            print("Blog post created successfully.")
        except Exception as e:
            print("Error creating post:", e)
            messages.error(request, "There was an error creating your blog post.")
        return redirect('index')
    else:
        return render(request, "create.html", {
            'categories': Category.objects.all()
        })




def profile(request, id):
    return render(request, 'profile.html', {
        'user': User.objects.get(id=id),
        'posts': Post.objects.all(),
        'media_url': settings.MEDIA_URL,
    })


def profileedit(request, id):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']

        user = User.objects.get(id=id)
        user.first_name = firstname
        user.email = email
        user.last_name = lastname
        user.save()
        return profile(request, id)

    return render(request, "profileedit.html", {
        'user': User.objects.get(id=id),
    })


def increaselikes(request, id):
    if request.method == 'POST':
        post = Post.objects.get(id=id)
        post.likes += 1
        post.save()
    return redirect("index")


def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, "post-details.html", {
        "user": request.user,
        'post': post,
        'recent_posts': Post.objects.all().order_by("-id"),
        'media_url': settings.MEDIA_URL,
        'comments': Comment.objects.filter(post_id=post.id),
        'total_comments': Comment.objects.filter(post_id=post.id).count(),
        'categories': Category.objects.all()
    })


def savecomment(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        content = request.POST['message']
        Comment(post=post, user=request.user, content=content).save()
        return redirect("index")


def deletecomment(request, id):
    comment = Comment.objects.get(id=id)
    postid = comment.post.id
    comment.delete()
    return post(request, postid)


def editpost(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        try:
            postname = request.POST['postname']
            content = request.POST['content']
            category_id = request.POST['category']
            category = Category.objects.get(id=category_id)

            post.postname = postname
            post.content = content
            post.category = category
            post.save()
        except Exception as e:
            print("Error editing post:", e)
        return profile(request, request.user.id)

    return render(request, "postedit.html", {
        'post': post,
        'categories': Category.objects.all()
    })


def deletepost(request, id):
    Post.objects.get(id=id).delete()
    return profile(request, request.user.id)


def contact_us(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name')    
        email = request.POST.get('email')  
        subject = request.POST.get('subject')  
        message = request.POST.get('message')  

        Contact(name=name, email=email, subject=subject, message=message).save()
        context['message'] = f"Dear {name}, Thanks for your time!"
    return render(request, "contact.html", context)
  # write for us view 

def write_for_us(request):
    return render(request, 'myapp/write-for-us.html')

def write_for_us(request, email):
    return render(request, 'myapp/write-for-us.html', {'email': email})


from django.shortcuts import render
from .forms import ArticleSubmissionForm

def write_for_us(request):
    if request.method == 'POST':
        form = ArticleSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #return redirect('thank_you')  # Redirect to the URL pattern name
            return render(request, 'myapp/thank_you.html')  # ✅ correct template path
        
    else:
        form = ArticleSubmissionForm()
    return render(request, 'myapp/write-for-us.html', {'form': form})

def thank_you(request):
    return render(request, 'myapp/thank_you.html')



# def advertise(request):

# from django.core.mail import send_mail
# from django.contrib import messages

# def advertise(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
        
#         # (Optional) You can send yourself an email here, or save to DB
#         print(f"New ad inquiry from {name} ({email}): {message}")
        
#         messages.success(request, "Thanks for contacting us! We'll get back to you soon.")
    
#     return render(request, 'advertise.html')

from django.contrib import messages
from .models import AdvertiseInquiry

def advertise(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save to DB
        AdvertiseInquiry.objects.create(
            name=name,
            email=email,
            message=message
        )

        messages.success(request, "Thanks for contacting us! We'll respond shortly.")

    return render(request, 'advertise.html')


# def terms(request):
def terms(request):
    return render(request, 'terms.html')



# privacy policy
def privacy(request):
    return render(request, 'privacy.html')


# blog guidelines
def blog_guidelines(request):
    return render(request, 'blog_guidelines.html')

# our story
from .models import TravelStory

def story_detail(request, pk):
    story = get_object_or_404(TravelStory, pk=pk)
    return render(request, 'travel/story_detail.html', {'story': story})


# team view
from .models import TeamMember

def meet_the_team(request):
    team_members = TeamMember.objects.all()
    return render(request, 'meet_the_team.html', {'team_members': team_members})


# careers view
from .models import JobOpening
from .forms import JobApplicationForm

def careers_view(request):
    jobs = JobOpening.objects.all()
    form = JobApplicationForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('careers')  # or show a success message

    return render(request, 'careers.html', {'jobs': jobs, 'form': form})






