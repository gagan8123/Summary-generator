from django.shortcuts import render,HttpResponse
from myapp.summary import Summary
# Create your views here.

        
        
    
def fun(request):
    if request.method == "POST":
        
       
        orgtext = request.POST.get('orgtext')
        if orgtext == '' or orgtext ==" ":
             print('true')
             return render(request,"index.html")
        
        
        out = Summary(orgtext)
        sumry = {'org':orgtext,'text':out.output[0],"path":out.output[1]}
        print("false")
        return render(request,"index.html",sumry)
        
        
    print("false2")
    return render(request,"index.html") #or HttpResponse("hello world")