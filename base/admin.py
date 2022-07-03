from django.contrib import admin
from .models import *

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
	list_display = ['name', 'description', 'add_date', 'url', 'github']
	search_fields = ('name', 'url', 'github',)

class TechnologyAdmin(admin.ModelAdmin):
	list_display = ['name']
	search_fields = ('name',)

class ContributorAdmin(admin.ModelAdmin):
	list_display = ['name', 'link']
	search_fields = ('name',)

class ContributionAdmin(admin.ModelAdmin):
	list_display = ['contributor', 'project', 'contribution']
	search_fields = ('contribution',)

class ScreenshotAdmin(admin.ModelAdmin):
	list_display = ['screenshot']
	search_fields = ('screenshot',)

class PostAdmin(admin.ModelAdmin):
	list_display = ['name', 'author', 'add_date', 'post']
	search_fields = ('name', 'author', )

admin.site.register(Project, ProjectAdmin)
admin.site.register(Technology, TechnologyAdmin)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Contribution, ContributionAdmin)
admin.site.register(Screensot, ScreenshotAdmin)
admin.site.register(Post, PostAdmin)