from django.shortcuts import render,redirect
from .forms import Myforms
from .models import Logg
from django.db.models import F

# Create your views here.
def home(request):
    dataa=Logg.objects.filter(confirm="yes")
    return render(request,'minor/homee.html',{'dataa':dataa})
def teacher(request):
    form = Myforms()
    if request.method == 'POST':
        form = Myforms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = Myforms()

    return render(request, 'minor/myformt.html', {'form': form})


def upv(request,id):
    reporter = Logg.objects.get(id=id)
    reporter.upvote = reporter.upvote+1
    reporter.save()
    return redirect('/')


