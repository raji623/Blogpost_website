from django.contrib import admin
from .models import Post,Comment,Contact, Category
from .models import ArticleSubmission
from .models import AdvertiseInquiry

@admin.register(AdvertiseInquiry)
class AdvertiseInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')
    search_fields = ('name', 'email')

admin.site.register(ArticleSubmission)


# our story admin register
from .models import TravelStory

@admin.register(TravelStory)
class TravelStoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'author_name', 'created_at']
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'author_name')
        }),
        ('Story Chapters', {
            'fields': (
                'chapter_0', 'chapter_1', 'chapter_2', 'chapter_3',
                'chapter_4', 'chapter_5', 'chapter_6', 'chapter_7',
            )
        }),
    )

    # team register
from .models import TeamMember

admin.site.register(TeamMember)

# careers register
from .models import JobOpening, JobApplication

admin.site.register(JobOpening)
admin.site.register(JobApplication)



# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Contact)
# myapp/admin.py

admin.site.register(Category)



admin.site.site_header = 'BLOGSPOT | ADMIN PANEL'
admin.site.site_title = 'BLOGSPOT | BLOGGING WEBSITE'
admin.site.index_title= 'BlogSpot Site Administration'
