from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
#from django.views import generic

from .models import Profile, Skills, SocialMedia, Accomplishment, Message

'''Generic views below, not used in this project'''
# class IndexView(generic.ListView):
#     template_name = 'mainsite/index.html'
#     context_object_name = 'profile'

#     def get_queryset(self):
#         return Profile.objects.filter(first_name='Tucker')

'''Render views'''
def index(request):
    profile_query = Profile.objects.filter(active='True')
    profile = get_object_or_404(profile_query)
    skills_list = Skills.objects.filter(user=profile,show=True).order_by('-skill_level')
    accomplishments_list = Accomplishment.objects.filter(user=profile,show=True).order_by('ranking')
    social_media_list = SocialMedia.objects.filter(user=profile)
    context = {
        'profile':profile,
        'skills_list':skills_list,
        'accomplishments_list':accomplishments_list,
        'social_media_list':social_media_list
    }
    return render(request,'mainsite/index.html',context)

def send_message(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        messageObj = Message.objects.create(name=name, email=email, message=message,date_received=timezone.now())
        print(messageObj)
    else:
        print("No post")
    return HttpResponseRedirect(reverse('mainsite:index'))
