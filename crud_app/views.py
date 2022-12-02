from .models import University, Student
from .forms import UniversityForm, StudentForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import Http404
# Create your views here.


def index(request):
    form = UniversityForm()
    univer_list = University.objects.all()
    context = {
        'form': form,
        'univer_list': univer_list,
    }
    return render(request, 'index.html', context)


def add_university(request):
    if request.method == 'POST':
        form = UniversityForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "ADDED SUCCESSFULLY")
            return redirect(index)
        else:
            messages.info(request, "INVALID FIELDS")
            return redirect(index)
    form = UniversityForm()
    univer_list = University.objects.all()
    context = {
        'form': form,
        'univer_list': univer_list
    }
    return render(request, 'index.html', context)


def delete_university(request, id):
    try:
        data = get_object_or_404(University, id=id)
        data.delete()
        messages.info(request, "DELETED SUCCESSFULLY")
        return redirect(index)
    except Exception:
        messages.info(request, "UNIVERSITY DOES NOT EXISTS")
        raise Http404('University does not exists')


def edit_university(request, id):
    try:
        data = get_object_or_404(University, id=id)
        form = UniversityForm()
        form.fields["full_name"].initial = data.full_name
        form.fields["short_name"].initial = data.short_name
        form.fields["established"].initial = data.established
        univer_list = University.objects.all()
        context = {
            'form': form,
            'univer_list': univer_list,
            'self_item': data
        }
        return render(request, 'index.html', context)
    except Exception:
        messages.info(request, "UNIVERSITY DOES NOT EXISTS")
        raise Http404('University does not exists')


def update_university(request, id):
    try:
        data = get_object_or_404(University, id=id)
        data.full_name = request.POST['full_name']
        data.short_name = request.POST['short_name']
        data.established = request.POST['established']
        form = UniversityForm(request.POST)
        if form.is_valid():
            data.save()
            messages.info(request, "EDITED SUCCESSFULLY")
            return redirect(index)
        else:
            messages.info(request, "INVALID FIELDS")
            return redirect(index)
    except Exception:
        messages.info(request, "UNIVERSITY DOES NOT EXISTS")
        raise Http404('University does not exists')


def students(request):
    form = StudentForm()
    students_list = Student.objects.all()
    context = {
        'form': form,
        'students_list': students_list,
    }
    return render(request, 'students.html', context)


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "ADDED SUCCESSFULLY")
            return redirect(students)
        else:
            messages.info(request, "INVALID FIELDS")
            return redirect(students)
    form = StudentForm()
    students_list = Student.objects.all()
    context = {
        'form': form,
        'students_list': students_list
    }
    return render(request, 'students.html', context)


def delete_student(request, id):
    try:
        data = get_object_or_404(Student, id=id)
        data.delete()
        messages.info(request, "DELETED SUCCESSFULLY")
        return redirect(students)
    except Exception:
        messages.info(request, "STUDENT DOES NOT EXISTS")
        raise Http404('Student does not exists')


def edit_student(request, id):
    try:
        data = get_object_or_404(Student, id=id)
        form = StudentForm()
        form.fields["name"].initial = data.name
        form.fields["birth_date"].initial = data.birth_date
        form.fields["university"].initial = data.university
        form.fields["admission_year"].initial = data.admission_year
        students_list = Student.objects.all()
        context = {
            'form': form,
            'students_list': students_list,
            'self_item': data
        }
        return render(request, 'students.html', context)
    except Exception:
        messages.info(request, "STUDENT DOES NOT EXISTS")
        raise Http404('Student does not exists')


def update_student(request, id):
    try:
        data = get_object_or_404(Student, id=id)
        university = get_object_or_404(
            University, id=request.POST['university'])
        data.name = request.POST['name']
        data.birth_date = request.POST['birth_date']
        data.university = university
        data.admission_year = request.POST['admission_year']
        form = StudentForm(request.POST)
        if form.is_valid():
            data.save()
            messages.info(request, "EDITED SUCCESSFULLY")
            return redirect(students)
        else:
            messages.info(request, "INVALID FIELDS")
            return redirect(students)
        return redirect(students)
    except Exception:
        messages.info(request, "STUDENT DOES NOT EXISTS")
        raise Http404('Student does not exists')
