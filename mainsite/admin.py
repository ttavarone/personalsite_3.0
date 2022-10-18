from django.contrib import admin

from .models import *

#Development admin site variables
admin.site.site_header = "Personal Site Administration"
admin.site.site_url = "http://127.0.0.1:8000/"

class ProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name', {'fields':['first_name','last_name','active']}),
        ('Contact Info', {'fields':['email_address','phone_number',]}),
        ('Alternate Contact Info',{'fields':['alternate_email','alternate_phone','show_alternate_contact']}),
        ('Biography',{'fields':['biography']}),
        ('Photos',{'fields':['image_dir']}),
        ('Profile Updates',{'fields':['last_update']})
    ]
    list_display = ('first_name','last_name','email_address','phone_number','last_update','active')
    list_filter = ['first_name','last_name','email_address','phone_number','last_update','active']
    search_fields = ['first_name','last_name','email_address','phone_number','email_address','biography']

class SkillsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Skill Info',{'fields':['skill_name','skill_level','show']}),
        ('Meta',{'fields':['skill_icon_name']}),
        ('Users',{'fields':['user']})
    ]
    list_display = ('skill_name','skill_level','user','show')
    list_filter = ['skill_name','skill_level','user','show']
    search_fields = ['skill_name','skill_level','user']

class SocialMediaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Social Media Info',{'fields':['site_name','site_url','username','show']}),
        ('Users',{'fields':['user']})
    ]
    list_display = ('site_name','site_url','user','show')
    list_filter = ['site_name','site_url','user','show']
    search_fields = ['site_name','site_url','user']

class AccomplishmentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Accomplishments Info',{'fields':['accomplishment_name','accomplishment_description','ranking','show']}),
        ('Photos',{'fields':['image_dir']}),
        ('Users',{'fields':['user']})
    ]
    list_display = ('accomplishment_name','ranking','show','user')
    list_filter = ['accomplishment_name','ranking','show','user']
    search_fields = ['accomplishment_name','accomplishment_description','user']

class MessageAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Message Information',{'fields':['name','email','date_received']}),
        ('Message Content',{'fields':['message']})
    ]
    list_display = ('name','email','message','date_received')
    list_filter = ['name','email','date_received']
    search_fields = ['name','email','date_received']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Skills, SkillsAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)
admin.site.register(Accomplishment, AccomplishmentAdmin)
admin.site.register(Message,MessageAdmin)
