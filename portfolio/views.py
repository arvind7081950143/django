from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
def about(request):
    val=request.GET.get('output')
    return render(request,"about.html",{'out':val})
def dummy(request):
    n1=0
    try:
        n=int(request.POST['val1'])
        n1=n
        data={'output':n1}
        url='/about/?output={}'.format(n1)
        return HttpResponseRedirect(url)
    except:
        pass
    return render(request,"dummy.html",{'nums':n1})
def homepage(request):
    return render(request,"index.html")
