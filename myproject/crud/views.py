from django.shortcuts import render,redirect
from .models import Member

# Create your views here.

def index(request):
    member=Member.objects.all()
    return render(request,'index.html',{'member':member})

def add(request):
    return render(request,'add.html')

# def add_display(request):
#     firstname=request.POST['first']
#     lasttname=request.POST['last']
#     member = Member(firstname=firstname, lasttname=lasttname)
#     member.save()
#     return redirect('index')

def add_display(request):
    firstname = request.POST['first']
    lasttname = request.POST['last']
    dob = request.POST['dob']
    member = Member(firstname=firstname, lasttname=lasttname, dob=dob)
    member.save()
    return redirect('index')

def delete(request,id):
    member=Member.objects.get(id=id)
    member.delete()
    return redirect('index')

def update(request,id):
    member=Member.objects.get(id=id)
    return render(request,'update.html',{'member':member})

def display_list(request,id):
    firstname = request.POST['first']
    lastname = request.POST['last']
    dob = request.POST['dob']
    member=Member.objects.get(id=id)
    member.firstname=firstname
    member.lasttname=lastname
    member.dob=dob
    member.save()
    return redirect('index')


