from django.shortcuts import render,redirect
from .models import Tracking
from .forms import Trackhere
# Create your views here.
def track(request):
    data= Tracking.objects.all()
    print('TRACKING DETAILS',data)
    prd={
        'data':data
    }
    return render(request, 'tracking.html', context=prd)

def track_here(request):
    if request.method == 'POST':
        form = Trackhere(request.POST)
        if form.is_valid():
            form.save()
            return redirect('track/')
    else:
        form = Trackhere()

    return render(request,'trackhere.html',{'form': form})