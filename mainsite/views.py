from django.shortcuts import get_object_or_404, render
#from django.views import generic

from .models import Profile, Skills, SocialMedia, Accomplishment

'''Generic views below, not used in this project'''
# class IndexView(generic.ListView):
#     template_name = 'mainsite/index.html'
#     context_object_name = 'profile'

#     def get_queryset(self):
#         return Profile.objects.filter(first_name='Tucker')

'''Render views'''
def index(request):
    profile = get_object_or_404(Profile, pk=1)
    skills_list = Skills.objects.filter(user=profile).order_by('-skill_level')
    accomplishments_list = Accomplishment.objects.filter(user=profile).order_by('ranking')[:2]
    social_media_list = SocialMedia.objects.filter(user=profile)
    context = {
        'profile':profile,
        'skills_list':skills_list,
        'accomplishments_list':accomplishments_list,
        'social_media_list':social_media_list
    }
    return render(request,'mainsite/index.html',context)
