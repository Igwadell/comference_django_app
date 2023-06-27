# from django.shortcuts import render, redirect
# # from .models import Speaker

# speakers = [
#     {
#         "name": "John Doe",
#         "bio": "John Doe is an expert in web development...",
#         "other_info": "John has spoken at various conferences...",
#     },
#     {
#         "name": "Jane Smith",
#         "bio": "Jane Smith is a data scientist specializing in...",
#         "other_info": "Jane has a Ph.D. in Computer Science...",
#     },
#     {
#         "name": "Mark Johnson",
#         "bio": "Mark Johnson is a renowned entrepreneur and...",
#         "other_info": "Mark has been featured in several business magazines...",
#     },
#     {
#         "name": "Sarah Johnson",
#         "bio": "Sarah Johnson is a cybersecurity expert with...",
#         "other_info": "Sarah has conducted extensive research on emerging cyber threats...",
#     },
#     {
#         "name": "Michael Chen",
#         "bio": "Michael Chen is a data privacy and compliance specialist...",
#         "other_info": "Michael is a frequent speaker at privacy conferences...",
#     },
# ]


# def speakerList(request):
#     # speakers = Speaker.objects.all()
#     return render(request, "speakers.html", 
#                   {"speakers": speakers})


# def createSpeakers(response):
#     if response.method == "POST":
#         speaker = {
#             "name": response.POST.get("name"),
#             "bio": response.POST.get("bio"),
#             "other_info": response.POST.get("other_info"),
#         }
#         speakers.append(speaker)
#         return redirect("/speakers/")
#     else:
#         return render(response, "createSpeaker.html")


# def viewSpeaker(request, id):
#     return render(request, "viewSpeaker.html", {"speaker": speakers[id - 1]})


# def choosetopic(request):
#     return render(request,'topic.html')




# def speakerUpdate(response, id):
#     if response.method == "POST":
#         speaker = {
#             "name": response.POST.get("name"),
#             "bio": response.POST.get("bio"),
#             "other_info": response.POST.get("other_info"),
#         }
#         speakers[id - 1] = speaker
#         return redirect("/speakers/")
#     else:
#         return render(response, "updateSpeaker.html", {"speaker": speakers[id - 1]})


# def speakerDelete(response, id):
#     if response.method == "POST":
#         speakers.pop(id - 1)
#         return redirect("/speakers/")
#     else:
#         return render(response, "deleteSpeaker.html", {"speaker": speakers[id - 1]})















# from django.shortcuts import render, redirect
# from .models import Speaker


# def speakerList(request):
#     speakers = Speaker.objects.all()
#     return render(request, "speakers.html", {"speakers": speakers})


# def createSpeakers(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         bio = request.POST.get("bio")
#         area_of_experience = request.POST.get("area_of_experience")
#         speaker = Speaker.objects.create(name=name, bio=bio, area_of_experience=area_of_experience)
#         return redirect("/speakers/")
#     else:
#         return render(request, "createSpeaker.html")


# def viewSpeaker(request, id):
#     speaker = Speaker.objects.get(id=id)
#     return render(request, "viewSpeaker.html", {"speaker": speaker})

def choosetopic(request):
    return render(request,'topic.html')

# def speakerUpdate(request, id):
#     speaker = Speaker.objects.get(id=id)
#     if request.method == "POST":
#         speaker.name = request.POST.get("name")
#         speaker.bio = request.POST.get("bio")
#         speaker.other_info = request.POST.get("other_info")
#         speaker.save()
#         return redirect("/speakers/")
#     else:
#         return render(request, "updateSpeaker.html", {"speaker": speaker})


# def speakerDelete(request, id):
#     speaker = Speaker.objects.get(id=id)
#     if request.method == "POST":
#         speaker.delete()
#         return redirect("/speakers/")
#     else:
#         return render(request, "deleteSpeaker.html", {"speaker": speaker})












from django.shortcuts import render, redirect
from .models import Category, Speaker


def speakerList(request):
    speakers = Speaker.objects.all()
    return render(request, "speakers.html", {"speakers": speakers})


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


def viewSpeaker(request, id):
    speaker = Speaker.objects.get(id=id)
    return render(request, "viewSpeaker.html", {"speaker": speaker})


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
