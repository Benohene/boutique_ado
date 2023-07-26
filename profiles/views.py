from django.shortcuts import render, get_object_or_404
from .models import UserProfile

# Create your views here.
def profile(request):
    """ Display the user's profile. """
    # Get the user's profile
    profile = get_object_or_404(UserProfile, user=request.user)
    # Render the template
    
    
    template = 'profiles/profile.html'
    context = {
        # 'on_profile_page': True
        'profile': profile
    }
    
    return render(request, template, context)
