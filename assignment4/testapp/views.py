from django.shortcuts import render, HttpResponseRedirect
from .models import WFreq

def PAnalysisview(request):
    return render(request, 'PAnalysis.html')

# Create your views here.
def testlogininfo(request,userid):
    print("You will see this number in the console:",userid)
    return render(request, 'PAnalysis.html')

def testlogininfo2(request,userid, userpwd):
    print("You will see this user in the console:",userid)
    print("You will see this password in the console:", userpwd)
    return render(request, 'PAnalysis.html')

def testformdisplay(request):
    return render(request, 'Testform.html')

def CreateWview(request):
    if request.method=="POST":
        wviewpost = Wfreq()
        wviewpost.ttextmanageid = request.POST.get['manageinputid']
        wviewpost.word = request.POST.get['wordnameid']
        wviewpost.frequency = request.POST.get['frequencyid']
        wviewpost.save()