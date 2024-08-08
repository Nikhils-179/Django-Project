from django.shortcuts import render

# Create your views here.
def renderTemplate(request):
    return render(request,'templateApp/firstTemplate.html')

def EmpInfo(request):
    myDict = {"id" : 123 , "name" : "Nikhil" , "Sal" : 10000}
    return render(request,'templateApp/Empinfo.html',myDict)