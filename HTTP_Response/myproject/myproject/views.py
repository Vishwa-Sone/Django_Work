from django.http import HttpResponse

def sheela(request):
    return HttpResponse("Hello how are you")


def apple(request):
    return HttpResponse("Apple a day keep's doctor way")


def banana(request):
    return HttpResponse("<h1>It is a Banana</h1>")


def list(request):
    list_data = [1,2,3,4,5,"abc",True,{"name":"smith"}]
    return HttpResponse(list_data)

def addition(request):
    a = 10
    b = 40
    sum = a + b
    return HttpResponse(sum)

def sheela(request):
    return HttpResponse("Second Sheela")
    