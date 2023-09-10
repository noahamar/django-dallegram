from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from .models import Profile, Post
from dotenv import load_dotenv
import openai, os, requests

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY', None)
openai.api_key = openai_api_key

# Create your views here.
def index(request):
    user = get_user_model().objects.get(username="noahamar")
    profile = Profile.objects.get(user=user)
    if openai_api_key is not None and request.method == 'POST':
        prompt = request.POST.get('prompt')
        if prompt is None:
            return redirect('/')
        openai_response = openai.Image.create(
            prompt=prompt,
            size='256x256'
        )
        image_url = openai_response["data"][0]["url"]
        image_response = requests.get(image_url)
        image_file = ContentFile(image_response.content)
        count = Post.objects.count() + 1
        post = Post(profile=profile, caption=prompt)
        post.image.save(f'post-{count}.jpg', image_file)
        post.save()
        return redirect('/')
    posts = Post.objects.all().order_by('-date')
    suggested_profiles = Profile.objects.exclude(user=user).order_by('?')[:4]
    return render(request, 'index.html', {
        "posts": posts, 
        "suggested_profiles": suggested_profiles 
    })