from django.core import serializers
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from main.models import Item

# Create your views here.
def show_main(request: HttpRequest):
    light_cone_list = Item.objects.all()

    context = {
        "light_cone_list": light_cone_list
    }

    return render(request, "main.html", context)

def add_light_cone(request: HttpRequest):
    if (request.method == "GET"):
        return render(request, "add_light_cone.html")
    elif (request.method == "POST"):
        post_data = list(request.POST.items())
        kwargs = {}
        for i in post_data:
            if i[0] == "csrfmiddlewaretoken":
                continue
            if i[1] == '':
                return HttpResponseRedirect("/main/")
            kwargs[i[0]] = i[1]

        item = Item(**kwargs)
        item.save()

        return HttpResponseRedirect("/main/")

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
