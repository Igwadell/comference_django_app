from django.shortcuts import render, redirect
from .models import Category, Speaker
##############
def speaker_list(request):
    speakers = Speaker.objects.all()
    return render(request, 'speaker_list.html', {'speakers': speakers})

def speaker_details(request, name):
    speaker = Speaker.objects.get(name=name)
    return render(request, 'speaker_details.html', {'speaker': speaker})
##############

def choosetopic(request):
    return render(request,'topic.html')

def createSpeakers(request):
    if request.method == "POST":
        name = request.POST.get("name")
        bio = request.POST.get("bio")
        contact_info = request.POST.get("contact_info")
        area_of_experience = request.POST.get("area_of_experience")
        profile_picture = request.POST.get("profile_picture")

        category_id = request.POST.get("category_id")
        category = Category.objects.get(id=category_id)

        speaker = Speaker.objects.create(
            Category=category,
            name=name,
            bio=bio,
            contact_info=contact_info,
            Profile_picture=profile_picture,
            area_of_experience=area_of_experience,
        )
        return redirect("/speakers/")
    else:
        categories = Category.objects.all()
        return render(request, "createSpeaker.html", {"categories": categories})


def viewspeaker(request, id):
    speaker = Speaker.objects.get(id=id)
    return render(request, "viewspeaker.html", {"speaker": speaker})


def speakerUpdate(request, id):
    speaker = Speaker.objects.get(id=id)
    if request.method == "POST":
        speaker.name = request.POST.get("name")
        speaker.bio = request.POST.get("bio")
        speaker.contact_info = request.POST.get("contact_info")
        speaker.Profile_picture = request.FILES.get("profile_picture")
        speaker.area_of_experience = request.POST.get("area_of_experience")
        speaker.save()
        return redirect("/speakers/")
    else:
        categories = Category.objects.all()
        return render(request, "updateSpeaker.html", {"speaker": speaker, "categories": categories})


def speakerDelete(request, id):
    speaker = Speaker.objects.get(id=id)
    if request.method == "POST":
        speaker.delete()
        return redirect("/speakers/")
    else:
        return render(request, "deleteSpeaker.html", {"speaker": speaker})
