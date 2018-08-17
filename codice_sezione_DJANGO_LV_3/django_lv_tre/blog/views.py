from django.shortcuts import render
from django.http import HttpResponse
from .forms import BlogPostModelForm

# Create your views here.
def creaPostView(request):

    if request.method == "POST":
        form = BlogPostModelForm(request.POST)
        if form.is_valid():
            print("Il Form è valido!")
            new_post = form.save()
            print("new_post: ", new_post)
            return HttpResponse("<h1>Post creato con successo!</h1>")
    else:
        form = BlogPostModelForm()
    context = {"form": form}
    return render(request, "blog/crea_post.html", context)
