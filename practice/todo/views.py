from django.shortcuts import render ,redirect


# Create your views here.
def index(request):
    return render(request, "todo/index.html")

def addtask(request):
    if request.method == "POST":
        if "tasks" in request.session:
            request.session["tasks"] += request.POST["task"]
            redirect(request,"todo/index.html", {
            "tasks":request.session["tasks"]
            })
        else:
            request.session["tasks"] = []
            request.session["tasks"] += request.POST["task"]
            redirect(request,"todo/index.html", {
            "tasks":request.session["tasks"]
            })
    else:
        return HttpResponse("404 Not found")
