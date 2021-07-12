from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *

def index(request):
    context = {
        'all_courses' : Course.objects.all()
    }
    return render(request, "index.html", context)


def create(request):
    # gets validation dictionary and holds it in request.post
    errors = Course.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/courses')

    else:
        course = Course.objects.create(
        course_name = request.POST['course_name'],
        description = request.POST['description'],
    )
    print(request.POST)
    return redirect('/courses') 

 
def delete(request, course_id):
    # WHEN RETURNING A ID SPECIFICALLY SET GET ID TO THE ID YOU ARE CARRYING
    if request.method == "GET":
        context = {
            'course' : Course.objects.get(id=course_id)
        }
        return render(request, "destroy.html", context)
    
    if request.method == "POST":
        delete_course = Course.objects.get(id=course_id)
        delete_course.delete()
        return redirect("/")