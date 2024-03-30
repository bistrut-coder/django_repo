from django.shortcuts import render

# Create your views here.
def jobs_view(request):
    return render(request,'testapp/index.html')

from testapp.models import Hybdjobs
def hybd_view(request):
    hybd_jobs=Hybdjobs.objects.all()
    my_dict={'hybd_jobs':hybd_jobs}
    return render(request,'testapp/hybd.html',my_dict)

from testapp.models import Bngjobs
def bng_view(request):
    bng_jobs=Bngjobs.objects.all()
    my_dict={'bng_jobs':bng_jobs}
    return render(request,'testapp/bng.html',my_dict)

from testapp.models import Punejobs
def pune_view(request):
    pune_jobs=Punejobs.objects.all()
    my_dict={'pune_jobs':pune_jobs}
    return render(request,'testapp/pune.html',my_dict)