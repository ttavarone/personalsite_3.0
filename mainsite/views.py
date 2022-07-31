#from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Profile, Skills, SocialMedia

class IndexView(generic.ListView):
    template_name = 'mainsite/index.html'
    context_object_name = 'profile'

    def get_queryset(self):
        return Profile.objects.all()
