import time
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, "posts/index.html")

def posts(request):
    # Get start and end points
    start = int(request.GET.get("start") or 0)
    end = int(request.GET.get("end") or (start + 9))
    # Generate list of posts
    data = []
    for i in range(start, end + 1):
        data.append(f"Post #{i}")
    #Artificially delay speed of responses
    time.sleep(1)

    return JsonResponse({
        "posts" : data
    })
