from django.shortcuts import render
#usage: pdb.set_trace()
import pdb

# Create your views here.
#pdb.set_trace()
def home(request):
        return render(request, 'home/home.html')
