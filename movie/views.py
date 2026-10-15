from django.shortcuts import render, HttpResponse
from .models import Movie
from story.models import Story
from asgiref.sync import sync_to_async
import time
import asyncio

# Create your views here.

#sync
def movie():
    print("preparing to fetch movies..")
    time.sleep(5)
    movies = Movie.objects.all()
    print(movies)
    print("got all the movies")

#sync
def story():
    print("preparing to fetch stories..")
    time.sleep(10)
    stories = Story.objects.all()
    print(stories)
    print("got all the stories")

#async

@sync_to_async(thread_sensitive=False)
def movie_async():
    print("preparing to fetch movies..")
    time.sleep(5)
    movies = Movie.objects.all()
    print(movies)
    print("got all the movies")


#async
@sync_to_async(thread_sensitive=False)
def story_async():
    print("preparing to fetch stories..")
    time.sleep(10)
    stories = Story.objects.all()
    print(stories)
    print("got all the stories")



def hello_world(request):
    return HttpResponse("Hello World")


#sync
def sync_view(request):
    start_time = time.time()
    movie()
    story()
    end_time = time.time()
    result = end_time - start_time
    print("total time", result)
    return HttpResponse("Sync request done")



async def async_view(request):
    start_time = time.time()
    # task1= asyncio.ensure_future(movie_async())
    # task2= asyncio.ensure_future(story_async())
    # await asyncio.wait([task1, task2])
    await asyncio.gather(movie_async(), story_async())
    end_time = time.time()
    result = end_time - start_time
    print("total time", result)
    return HttpResponse("Async request done")




    
    
