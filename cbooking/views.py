from django.shortcuts import render,redirect
from .models import Booking
from .forms import Bookhere

# Create your views here.
def book(request):
    data= Booking.objects.all()
    print('BOOKING DETAILS',data)
    content={
        'data':data
    }
    return render(request, 'booking.html', context=content)

def book_here(request):
    if request.method == 'POST':
        form = Bookhere(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Bookhere()

    return render(request,'bookhere.html',{'form': form})