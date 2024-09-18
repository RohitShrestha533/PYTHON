from django.shortcuts import render,redirect
from . models import student
from django.http import Http404

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
def display_student(request):
    std = student.objects.all()
    return render(request, 'student/display.html', {'students': std})

#edit
def edit_student(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        std = student.objects.get(id=id)
        return render(request, 'student/update.html', {'students': std})
    else:        
        return redirect('display_student')

def update_student(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        address = request.POST.get('address')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        course = request.POST.get('course')
        std = student.objects.get(id=id)
        std.name = name
        std.address = address
        std.email = email
        std.phone = phone
        std.course = course
        std.save()
        return redirect('display_student')
    else:
        return redirect('display_student')



#delete
def delete_student(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        print(f"Received ID for deletion: {id}")  # Debug output
        try:
            std = student.objects.get(id=id)
            std.delete()
            print(f"Student with ID {id} deleted.")  # Debug output
        except student.DoesNotExist:
            print("Student does not exist.")  # Debug output
            raise Http404("Student does not exist")

        return redirect('display_student')
    else:
        print("Invalid request method.")  # Debug output
        return Http404("Invalid request method")
