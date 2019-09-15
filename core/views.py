from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from core.models import Profile

import facebook

# Create your views here.
def login(request):
    return render(request, 'login.html')

@login_required
def home(request):
    token = 'EAArs9bPdU9IBALyEhNcpUcTudkZCi9yHkQBH1UCOqLf1LI2AzpN07ZAMYMsKhD6WjmYtZCdJJ9kFzBJxArHotrJbz6NvZClyJvrZABMy81AvBBaYcfbN74UTiZCzDfB1hdGE73Py8tUuFuY1U5aZAMD0B4dFE7Pw7KvRpU3aCNcaQZDZD'
    graph = facebook.GraphAPI(token)
    profile = graph.get_object("me")

    friends = graph.get_connections("me", "friends")
    friend_count = int(friends['summary']['total_count'])

    likes = graph.get_connections("me", "likes")
    like_count = len(likes['data'])

    events = graph.get_connections("me", "events")
    event_count = len(events['data'])

    previousProfile = Profile.objects.order_by('-pk')[0]
    currentProfile = Profile(friends = friend_count, likes = like_count, events = event_count)
    currentProfile.save()

    changeInLikes = getattr(previousProfile, 'likes') - getattr(currentProfile, 'likes')
    changeInFriends = getattr(previousProfile, 'friends') - getattr(currentProfile, 'friends')
    changeInEvents = getattr(previousProfile, 'events') - getattr(currentProfile, 'events')

    return render(request, 'home.html', {'friendCount' : friend_count, 'likeCount' : like_count, 'eventCount' : event_count,
    'changeInLikes' : changeInLikes, 'changeInFriends' : changeInFriends, 'changeInEvents' : changeInEvents })
