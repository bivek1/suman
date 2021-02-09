from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import StaffForm, StudentForm
from student.models import CustomUser, Staff, Student,attendance
from django.contrib import messages
import smtplib, sys
from .sms import sendSms
# Create your views here.
def index(request):
    return render(request, "index.html")

def dologin(request):
    if request.method != "POST":
        return HttpResponse("Sorry method is not allowed!")
    else:
        username = request.POST['username']
        password = request.POST['password']
        
        dolog = authenticate(request, username = username, password= password)
        
        if dolog != None:
            login(request, dolog)
            if dolog.user_type == "1":
                return HttpResponseRedirect(reverse('adminHome'))
            elif dolog.user_type == "2":
                return HttpResponseRedirect(reverse('staffDashboard'))
            else:
                messages.error(request, "Invalid Credential")
                return HttpResponseRedirect(reverse('index'))
        else:
            messages.error(request, "Invalid Credential")
            return HttpResponseRedirect(reverse('index'))
            
def log(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
def dashBoard(request):
    student = Student.objects.all()
    staff = Staff.objects.all()
    return render(request, "dashboard.html", {'student':student, 'staff':staff})

def addStaff(request):
    staff = StaffForm()
    dist = {
        'form':staff
    }
    if request.method == 'POST':
        staff = StaffForm(request.POST)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        number = request.POST['number']
        Temporary_address = request.POST['Temporary_address']     
        gender = request.POST['gender']   
        try: 
            use = CustomUser.objects.create_user(first_name = first_name, last_name = last_name, password = password, username = username, email = username+"@school.com", user_type = '2')
            aa = staff.save(commit=False)
            aa.admin = use
            aa.number= number
            aa.Temporary_address= Temporary_address
            aa.gender= gender
            aa.save()
            messages.success(request, "Staff Added Sucessfully!")
            return HttpResponseRedirect(reverse('staffList'))
        except:
            messages.error(request, "Something went Wrong. May be username has been taken already. Try with different One")
            return render(request, "addStaff.html", dist)
    else:
        return render(request, "addStaff.html", dist)
        
def staffList(request):
    staffL = Staff.objects.all()
    return render(request, "staffList.html", {'staff':staffL})

def addStudent(request):
    student = StudentForm()
    dist = {
        'form':student
    }
    if request.method == 'POST':
        student = StudentForm(request.POST)
        first_name = request.POST['first_name']
        idcard = request.POST['id_card']
        last_name = request.POST['last_name']
        faculty = request.POST['faculty']
        email = request.POST['email']
        number = request.POST['number']
        Temporary_address = request.POST['Temporary_address']    
        street = request.POST['street']
        district = request.POST['district'] 
        gender = request.POST['gender']   
        try: 
            use = CustomUser.objects.create_user(first_name = first_name, last_name = last_name, password = email, username = email, email = email, user_type = '3')
            aa = student.save(commit=False)
            aa.admin = use
            aa.number= number
            aa.id_card = idcard
            aa.faculty = faculty
            aa.Temporary_address= Temporary_address
            aa.gender= gender
            aa.street = street
            aa.district = district
            aa.save()
            messages.success(request, "Student Added Sucessfully!")
            return HttpResponseRedirect(reverse('studentList'))
        except:
            messages.error(request, "Something went Wrong. May be email has been taken already. Try with different One")
            return render(request, "addStudent.html", dist)
    else:
        return render(request, "addStudent.html", dist)

def studentList(request):
    student = Student.objects.all()
    return render(request, "studentList.html", {'student':student})

def sendEmail(request):
    student = Student.objects.all()
    dist = {
        'student': student
    }
    if request.method == 'POST':
        name = request.POST['student']
        message = request.POST['message']
        subject = request.POST['subject']
        student = CustomUser.objects.get(id = int(name))
        email = student.email
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login('', '')
        smtpObj.sendmail('', email, 'Subject:'+subject+'\n'+message)
    
        smtpObj.quit()
        print(email)
        print(message)
        return render(request, "sucess.html", dist)
    else:
        return render(request, "email.html", dist)
    
    
def sms(request):
    student = Student.objects.all()
    dist = {
        'student': student
    }
    if request.method == 'POST':
        name = request.POST['student']
        message = request.POST['message']
        number = request.POST['number']
        student = CustomUser.objects.get(id = int(name))
        sendSms(number, message)
        return render(request, "sucess.html", dist)
    else:
        return render(request, "sms.html", dist)
    
def attendace(request):
    a = attendance.objects.all()
    dist = {
        'attendance':a
    }
    if request.method == 'POST':
        num = int(request.POST['attandance'])
        get_student = Student.objects.get(id_card=num)
        for inter in a:
            if inter.student == get_student:
                if inter.evening == None:
                    import datetime
                    x = datetime.datetime.now()
                    current_time = x.time()
                    go = current_time.replace(hour = 17)
                    
                    inter.evening = go
                    inter.save()
                    number = str(get_student.number)
                    message =  "Dear Parents  " + get_student.admin.first_name  + " (Your child) has Left School"
                    sendSms(number, message)
                    a = attendance.objects.all()
                    dist = {
                        'attendance':a
                    }
                    return render(request, "attendance.html", dist)
        Attendance = attendance()
        import datetime
        x = datetime.datetime.now()
        current_time = x.time()
        cureent = current_time.replace(hour = 10)
        Attendance.student = get_student
        Attendance.morning = cureent
        Attendance.present = True
        Attendance.save()
        number = str(get_student.number)
        message = "Dear Parents  " + get_student.admin.first_name  + " (Your child) has join School"
        sendSms(number, message)
        a = attendance.objects.all()
        dist = {
            'attendance':a
        }
        return render(request, "attendance.html", dist)
        a = attendance.objects.all()
        dist = {
            'attendance':a
        }
        return render(request, "attendance.html", dist)
    else:
        return render(request, "attendance.html", dist)
    
def staffDashboard(request):
    student = Student.objects.all()
    return render(request, "staffdashboard.html",{'student':student} )

def SearchReport(request):
    try:
        query = int(request.GET['search'])
        student = Student.objects.get(id_card=query)
        return render(request, "searchReport.html", {'student':student})
    except:
        messages.error(request, "Please Search By Id Card")
        return render(request, "searchReport.html")
