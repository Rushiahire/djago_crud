from django.shortcuts import redirect, render, resolve_url
from django.views import View
from . import models
from . import forms

class Home(View):
    def get(self,request):
        content={
            'Student_details':models.Student_info.objects.all(),
            'Student_forms':forms.Student_forms()
        }
        return render(request,'index.html',content)

    def post(self,request):
        student_name=request.POST['student_name']
        email = request.POST['email']
        roll_number = request.POST['roll_number']

        new_data= models.Student_info(student_name=student_name,email=email,roll_number=roll_number)
        new_data.save()
        return redirect('/')

class Delete_data(View):
    def post(self,request):
        student_id = request.POST['student_id']
        student_details = models.Student_info.objects.filter(id=student_id)
        student_details.delete()
        return redirect('/')
    
