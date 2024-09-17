from django.shortcuts import render
from . models import student

# Create your views here.

#add student
def add_std(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        course = request.POST.get('course')

        std = student(
            name=name,
            email=email,
            phone=phone,
            address=address,
            course=course
        )
        std.save()

        students = student.objects.all()  # Fetch all student records
        return render(request, 'student/display.html', {'students': students})
        
    
    return render(request, 'student/form.html')


def form(request):
    return render(request, 'student/form.html')


#display (SELECT)
def display(request):
    std = student.objects.all()
    return render(request, 'student/display.html', {'students': std})

