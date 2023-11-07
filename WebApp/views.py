from django.shortcuts import render,redirect
from .models import Student
from .forms import AddStudentForm
# Create your views here.
def Home(request):
    stu_obj = Student.objects.all()
    return render(request,'home.html', {"studentData":stu_obj})


def add_Student(request):
    fm = AddStudentForm(request.POST)
    if fm.is_valid():
        fm.save()
        return redirect('/')
    else:
        return render(request,'add-student.html',{'form':fm})
    
def delete(request):
    data= request.POST
    id= data.get("id")
    stu_obj= Student.objects.get(id=id)
    stu_obj.delete()
    return redirect("/")

def edit(request,id):
    stu_obj = Student.objects.get(id=id)
    form = AddStudentForm(instance=stu_obj)
    if request.method=="POST":
        form=AddStudentForm(request.POST,instance=stu_obj)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request,'editDetail.html',{'form':form})  