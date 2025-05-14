from . import views
from django.urls import path



urlpatterns = [
    path("",views.index,name="index"),
    path("blog",views.blog,name="blog"),
    path("signin",views.signin,name="signin"),
    path("signup",views.signup,name="signup"),
    path("logout",views.logout,name="logout"),
    path("create",views.create,name="create"),
    path("increaselikes/<int:id>",views.increaselikes,name='increaselikes'),
    path("profile/<int:id>",views.profile,name='profile'),
    path("profile/edit/<int:id>",views.profileedit,name='profileedit'),
    path("post/<int:id>",views.post,name="post"),
    path("post/comment/<int:id>",views.savecomment,name="savecomment"),
    path("post/comment/delete/<int:id>",views.deletecomment,name="deletecomment"),
    path("post/edit/<int:id>",views.editpost,name="editpost"),
    path("post/delete/<int:id>",views.deletepost,name="deletepost"),
    path("contact",views.contact_us,name="contact"),
    path('category/<int:category_id>/', views.category_posts, name='category_posts'),
    path('write-for-us/', views.write_for_us, name='write-for-us'),
    path('advertise/', views.advertise, name='advertise'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    path('blog-guidelines/', views.blog_guidelines, name='blog_guidelines'),
    path('story/<int:pk>/', views.story_detail, name='story_detail'),
    path('meet-the-team/', views.meet_the_team, name='meet_the_team'),
    path('careers/', views.careers_view, name='careers'),
    #path('story/<int:story_id>/download/', views.download_story_pdf, name='download_story_pdf'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('write-for-us/<str:email>/', views.write_for_us, name='write-for-us-email'),
    

    

    

]
