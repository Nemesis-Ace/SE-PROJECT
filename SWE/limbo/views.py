from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Student, Course, Mark, Addon, Schedule, Instructor,DefaultList,DueList,HostelAllot,LoanList
from .forms import MarkForm, ScheduleForm, AddonForm,  DefaultForm,DueForm,HostelForm,LoanForm
from django.contrib.auth import logout


@login_required
def dashboard(request):
    if request.user.get_username() == "AAA" or request.user.get_username() == "Director" or request.user.get_username() == "Dean" or request.user.get_username() == "Registrar" :
        return redirect('/admin/')
    group = request.user.groups.filter(user=request.user)[0]
    if group.name == "Student":
        pg_dict = dict()
        pg_dict['group'] = "Student"
        students = Student.objects.order_by('semester')
        for student in students:
            if student.sid == request.user.get_username():
                pg_dict['sem'] = student.semester
        return render(request, 'student/student_dashboard.html', context=pg_dict)
    elif group.name == "Faculty":
        pg_dict = {'group': "Faculty"}
        return render(request, 'academic/faculty_dashboard.html', context=pg_dict)
    elif group.name == "HoD":
        pg_dict = dict()
        pg_dict = {'isHoD': True}
        pg_dict['group'] = "HoD"
        return render(request, 'academic/faculty_dashboard.html', context=pg_dict)
    elif group.name == "AddOnC":
        pg_dict = dict()
        pg_dict = {'isAddOnC': True}
        pg_dict['group'] = "AddOnC"
        return render(request, 'academic/faculty_dashboard.html', context=pg_dict)
    elif group.name == "Warden" or group.name == "Librarian" or group.name == "Lab-Incharge" or group.name == "FnA" or group.name == "Gymkhana":
        pg_dict = dict()
        if group.name== "Warden":
            pg_dict = {'isWarden': True}
        if group.name== "Librarian":
            pg_dict = {'isLibrarian': True}
        pg_dict['group'] = group.name
        return render(request, 'admin_dashboard.html', context=pg_dict)

    context = {}
    template = "login.html"
    return render(request, template, context)


def maincourse(request):
    courselist = Course.objects.order_by('cid')
    marklist = Mark.objects.order_by('student_id')
    pg_dict = {'courses': courselist, 'marks': marklist}
    students = Student.objects.order_by('semester')
    for student in students:
        if student.sid == request.user.get_username():
            pg_dict['sem'] = student.semester
    for mk in marklist:
        if mk.student_id == request.user.get_username():
            for obj in courselist:
                if obj.cid == mk.course_id:
                    pg_dict['registered'] = "1"

    if request.method == 'POST':
        var = request.POST.getlist('completed')
        print(var)
        if len(var) > 0:
            for c in var:
                for course in courselist:
                    if c == course.cid:

                        p = Mark(student_id=request.user.get_username(
                        ), instructor_id=course.iid, course_id=c, course_name=course.name, score=0)
                        p.save()
            return render(request, 'student/student_dashboard.html', context=pg_dict)

    return render(request, 'student/maincourse.html', context=pg_dict)


def addon(request):
    courselist = Addon.objects.order_by('cid')
    marklist = Mark.objects.order_by('student_id')
    pg_dict = {'courses': courselist, 'marks': marklist}
    students = Student.objects.order_by('semester')
    for student in students:
        if student.sid == request.user.get_username():
            pg_dict['sem'] = student.semester
    for mk in marklist:
        if mk.student_id == request.user.get_username():
            for obj in courselist:
                if obj.cid == mk.course_id:
                    pg_dict['registered'] = "1"

    if request.method == 'POST':
        var = request.POST.getlist('completed')
        if len(var) > 0:
            for c in var:
                for course in courselist:
                    if c == course.cid:
                        p = Mark(student_id=request.user.get_username(
                        ), instructor_id=course.iid, course_id=c, course_name=course.name, score=0)
                        p.save()
            return render(request, 'student/student_dashboard.html', context=pg_dict)

    return render(request, 'student/addon.html', context=pg_dict)


def result(request):
    marklist = Mark.objects.order_by('student_id')
    stmark = []
    for mk in marklist:
        if mk.student_id == request.user.get_username():
            stmark.append(mk)
    pg_dict = {'result': stmark}
    students = Student.objects.order_by('semester')
    for student in students:
        print(request.user.get_username())
        if student.sid == request.user.get_username():
            pg_dict['sem'] = student.semester
    return render(request, 'student/semresults.html', context=pg_dict)


def markupdate(request):
    group = request.user.groups.filter(user=request.user)[0]
    marklist = Mark.objects.filter(
        instructor_id=request.user.get_username()).order_by('course_id', 'student_id')
    pg_dict = {'mark': marklist}
    pg_dict['group'] = group.name
    if group.name == "HoD":
        pg_dict['isHoD'] = True
    elif group.name == "AddOnC":
        pg_dict['isAddOnC'] = True
    return render(request, 'academic/markupdate.html', context=pg_dict)


def markedit(request, id):
    group = request.user.groups.filter(user=request.user)[0]
    mark = Mark.objects.get(id=id)
    pg_dict = dict()
    pg_dict['mark'] = mark
    pg_dict['group'] = group.name
    if group.name == "HoD":
        pg_dict['isHoD'] = True
    elif group.name == "AddOnC":
        pg_dict['isAddOnC'] = True
    return render(request, 'academic/markedit.html', context=pg_dict)


def updatemark(request, id):
    group = request.user.groups.filter(user=request.user)[0]
    if request.method == 'POST':
        mark = Mark.objects.get(id=id)
        pg_dict = dict()
        pg_dict['mark'] = mark
        pg_dict['group'] = group.name
        if group.name == "HoD":
            pg_dict['isHoD'] = True
        elif group.name == "AddOnC":
            pg_dict['isAddOnC'] = True
        form = MarkForm(request.POST, instance=mark)

        if form.is_valid():
            form.save()
            return redirect("/markupdate")
        else:
            print('not valid')
    return render(request, 'academic/markedit.html', pg_dict)


def viewschedule(request):
    group = request.user.groups.filter(user=request.user)[0]
    pg_dict = {'group': group.name}
    schedulelist = Schedule.objects.filter(
        iid=request.user.get_username()).order_by('day', 'time')
    pg_dict['schedule'] = schedulelist
    if group.name == "HoD":
        pg_dict['isHoD'] = True
    elif group.name == "AddOnC":
        pg_dict['isAddOnC'] = True
    return render(request, 'academic/viewschedule.html', context=pg_dict)


def scheduleupdate(request):
    group = request.user.groups.filter(user=request.user)[0]
    pg_dict = {'group':group.name}
    schdlist = Schedule.objects.order_by('day', 'time')
    pg_dict['schedule'] = schdlist
    if group.name == "HoD":
        pg_dict['isHoD'] = True
    elif group.name == "AddOnC":
        pg_dict['isAddOnC'] = True
    return render(request, 'academic/scheduleupdate.html', context=pg_dict)


def scheduleedit(request, id):
    group = request.user.groups.filter(user=request.user)[0]
    pg_dict = {'group' : group.name}
    schedule = Schedule.objects.get(id=id)
    pg_dict['schedule'] = schedule
    if group.name == "HoD":
        pg_dict['isHoD'] = True
    elif group.name == "AddOnC":
        pg_dict['isAddOnC'] = True
    return render(request, 'academic/scheduleedit.html', context=pg_dict)


def updateschedule(request, id):
    group = request.user.groups.filter(user=request.user)[0]
    pg_dict = {'group' : group.name}
    if group.name == "HoD":
        pg_dict['isHoD'] = True
    elif group.name == "AddOnC":
        pg_dict['isAddOnC'] = True
    if request.method == 'POST':
        schedule = Schedule.objects.get(id=id)
        pg_dict['schedule'] = schedule
        form = ScheduleForm(request.POST, instance=schedule)

        if form.is_valid():
            form.save()
            return redirect("/scheduleupdate")
        else:
            print('not valid')
    return render(request, 'academic/scheduleedit.html', context=pg_dict)


def destroyschedule(request, id):
    schedule = Schedule.objects.get(id=id)
    schedule.delete()
    return redirect("/scheduleupdate")


def addschedule(request):
    group = request.user.groups.filter(user=request.user)[0]
    pg_dict = {'group' : group.name}
    if group.name == "HoD":
        pg_dict['isHoD'] = True
    elif group.name == "AddOnC":
        pg_dict['isAddOnC'] = True
    form = ScheduleForm()
    if request.method == "POST":
        form = ScheduleForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/scheduleupdate')
            except:
                pass
    else:
        form = ScheduleForm()
        print('not valid')
    pg_dict['form'] = form
    return render(request, 'academic/addschedule.html', context=pg_dict)


def manageaddon(request):
    group = request.user.groups.filter(user=request.user)[0]
    pg_dict = {'group' : group.name}
    if group.name == "HoD":
        pg_dict['isHoD'] = True
    elif group.name == "AddOnC":
        pg_dict['isAddOnC'] = True
    addonlist = Addon.objects.order_by('cid')
    pg_dict['addon'] = addonlist
    return render(request, 'academic/manageaddon.html', context=pg_dict)


def addonedit(request, id):
    group = request.user.groups.filter(user=request.user)[0]
    addon = Addon.objects.get(id=id)
    pg_dict = {'addon': addon}
    pg_dict['group'] = group.name
    if group.name == "HoD":
        pg_dict['isHoD'] = True
    elif group.name == "AddOnC":
        pg_dict['isAddOnC'] = True
    return render(request, 'academic/addonedit.html', context=pg_dict)


def updateaddon(request, id):
    group = request.user.groups.filter(user=request.user)[0]
    if request.method == 'POST':
        addon = Addon.objects.get(id=id)
        form = AddonForm(request.POST, instance=addon)
        if form.is_valid():
            form.save()
            return redirect("/manageaddon")
        else:
            print('not valid')
    pg_dict = {'addon': addonlist}
    pg_dict['group'] = group.name
    if group.name == "HoD":
        pg_dict['isHoD'] = True
    elif group.name == "AddOnC":
        pg_dict['isAddOnC'] = True
    return render(request, 'academic/addonedit.html', context=pg_dict)


def destroyaddon(request, id):
    addon = Addon.objects.get(id=id)
    addon.delete()
    return redirect("/manageaddon")


def addaddon(request):
    group = request.user.groups.filter(user=request.user)[0]
    form = AddonForm()
    if request.method == "POST":
        form = AddonForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/manageaddon')
            except:
                pass
    else:
        form = AddonForm()
    pg_dict = {'form': form}
    if group.name == "HoD":
        pg_dict['isHoD'] = True
    elif group.name == "AddOnC":
        pg_dict['isAddOnC'] = True
    pg_dict['group'] = group.name
    return render(request, 'academic/addaddon.html', context=pg_dict)


def defaultlist(request):
    group = request.user.groups.filter(user=request.user)[0]
    pg_dict = dict()
    if group.name== "Warden":
        pg_dict = {'isWarden': True}
    if group.name== "Librarian":
        pg_dict = {'isLibrarian': True}
    if group.name=='Warden':
        defaultlist = DefaultList.objects.filter(department='Hostel').order_by('sid')
        pg_dict['actionWarden'] = False
    if group.name=='Librarian':
        defaultlist = DefaultList.objects.filter(department='Library').order_by('sid')
        pg_dict['actionLibrarian'] = False
    if group.name=='Lab-Incharge':
        defaultlist = DefaultList.objects.filter(department='Lab').order_by('sid')
        pg_dict['actionLab'] = False
    if group.name=='FnA':
        defaultlist = DefaultList.objects.order_by('department')
        pg_dict['actionFnA'] = True
    if group.name=='Gymkhana':
        defaultlist = DefaultList.objects.order_by('department')
        pg_dict['actionGymkhana'] = True

    pg_dict['default'] = defaultlist
    pg_dict['group'] = group.name
    return render(request, 'defaultlist.html', context=pg_dict)


def defaultedit(request, id):
    default = DefaultList.objects.get(id=id)
    return render(request, 'defaultedit.html', {'default': default})


def updatedefault(request, id):
    if request.method == 'POST':
        default = DefaultList.objects.get(id=id)
        form = DefaultForm(request.POST, instance=default)

        if form.is_valid():
            form.save()
            return redirect("/defaultlist")
        else:
            print('not valid')
    return render(request, 'defaultedit.html', {'deafult': default})


def destroydefault(request, id):
    default = DefaultList.objects.get(id=id)
    default.delete()
    return redirect("/defaultlist")


def adddefault(request):
    pg_dict = dict()
    group = request.user.groups.filter(user=request.user)[0]
    if group.name== "Warden":
        pg_dict = {'isWarden': True}
    if group.name== "Librarian":
        pg_dict = {'isLibrarian': True}
    if group.name=='Warden':
        pg_dict['dept'] = "Hostel"
    if group.name=='Librarian':
        pg_dict['dept'] = "Library"
    if group.name=='Lab-Incharge':
        pg_dict['dept'] = "Lab"
    form = DefaultForm()
    if request.method == "POST":
        form = DefaultForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/defaultlist')
            except:
                pass
    else:
        form = DefaultForm()

    pg_dict['form']=form
    return render(request, 'adddefault.html', context=pg_dict)


def duelist(request):
    pg_dict = dict()
    group = request.user.groups.filter(user=request.user)[0]
    if group.name== "Warden":
        pg_dict = {'isWarden': True}
    if group.name== "Librarian":
        pg_dict = {'isLibrarian': True}
    if group.name=='Warden':
        duelist = DueList.objects.filter(department='Hostel').order_by('sid')
        pg_dict['actionWarden'] = False
    if group.name=='Librarian':
        duelist = DueList.objects.filter(department='Library').order_by('sid')
        pg_dict['actionLibrarian'] = False
    if group.name=='Lab-Incharge':
        duelist = DueList.objects.filter(department='Lab').order_by('sid')
        pg_dict['actionLab'] = False
    if group.name=='FnA':
        duelist = DueList.objects.order_by('department')
        pg_dict['actionFnA'] = True
    if group.name=='Gymkhana':
        duelist = DueList.objects.order_by('department')
        pg_dict['actionGymkhana'] = True

    pg_dict['due'] = duelist
    pg_dict['group'] = group.name
    return render(request, 'duelist.html', context=pg_dict)


def dueedit(request, id):
    due = DueList.objects.get(id=id)
    return render(request, 'dueedit.html', {'due': due})


def updatedue(request, id):
    if request.method == 'POST':
        due = DueList.objects.get(id=id)
        form = DueForm(request.POST, instance=due)

        if form.is_valid():
            form.save()
            return redirect("/duelist")
        else:
            print('not valid')
    return render(request, 'dueedit.html', {'due': due})


def destroydue(request, id):
    due = DueList.objects.get(id=id)
    due.delete()
    return redirect("/duelist")


def adddue(request):
    pg_dict = dict()
    group = request.user.groups.filter(user=request.user)[0]

    if group.name== "Warden":
        pg_dict = {'isWarden': True}
    if group.name== "Librarian":
        pg_dict = {'isLibrarian': True}
    if group.name=='Warden':
        pg_dict['dept'] = "Hostel"
    if group.name=='Librarian':
        pg_dict['dept'] = "Library"
    if group.name=='Lab-Incharge':
        pg_dict['dept'] = "Lab"
    form = DueForm()
    if request.method == "POST":
        form = DueForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/duelist')
            except:
                pass
    else:
        form = DueForm()

    pg_dict['form']=form
    return render(request, 'adddue.html', context=pg_dict)

def allotroom(request):
    pg_dict = dict()
    group = request.user.groups.filter(user=request.user)[0]
    if group.name== "Warden":
        pg_dict = {'isWarden': True}
    if group.name== "Librarian":
        pg_dict = {'isLibrarian': True}
    room = HostelAllot.objects.order_by('room')


    pg_dict['room'] = room

    return render(request, 'allotroom.html', context=pg_dict)


def allotedit(request, id):
    room = HostelAllot.objects.get(id=id)
    return render(request, 'allotedit.html', {'room': room})


def updateallot(request, id):
    if request.method == 'POST':
        room = HostelAllot.objects.get(id=id)
        form = HostelForm(request.POST, instance=room)

        if form.is_valid():
            form.save()
            return redirect("/allotroom")
        else:
            print('not valid')
    return render(request, 'allotedit.html', {'room': room})


def destroyallot(request, id):
    room = HostelAllot.objects.get(id=id)
    room.delete()
    return redirect("/allotroom")


def addallot(request):
    pg_dict = dict()
    group = request.user.groups.filter(user=request.user)[0]
    if group.name== "Warden":
        pg_dict = {'isWarden': True}
    if group.name== "Librarian":
        pg_dict = {'isLibrarian': True}
    form = HostelForm()
    if request.method == "POST":
        form = HostelForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/allotroom')
            except:
                pass
    else:
        form = HostelForm()

    pg_dict['form']=form
    return render(request, 'addallot.html', context=pg_dict)

def loanlist(request):
    pg_dict = dict()
    group = request.user.groups.filter(user=request.user)[0]
    if group.name== "Warden":
        pg_dict = {'isWarden': True}
    if group.name== "Librarian":
        pg_dict = {'isLibrarian': True}

    loan = LoanList.objects.order_by('sid')


    pg_dict['loan'] = loan

    return render(request, 'loanlist.html', context=pg_dict)


def loanedit(request, id):
    loan = LoanList.objects.get(id=id)
    return render(request, 'loanedit.html', {'loan': loan})


def updateloan(request, id):
    if request.method == 'POST':
        loan = LoanList.objects.get(id=id)
        form = LoanForm(request.POST, instance=loan)

        if form.is_valid():
            form.save()
            return redirect("/loanlist")
        else:
            print('not valid')
    return render(request, 'loanedit.html', {'loan': loan})


def destroyloan(request, id):
    loan = LoanList.objects.get(id=id)
    loan.delete()
    return redirect("/loanlist")


def addloan(request):
    pg_dict = dict()
    group = request.user.groups.filter(user=request.user)[0]
    if group.name== "Warden":
        pg_dict = {'isWarden': True}
    if group.name== "Librarian":
        pg_dict = {'isLibrarian': True}
    form = LoanForm()
    if request.method == "POST":
        form = LoanForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/loanlist')
            except:
                pass
    else:
        form = LoanForm()

    pg_dict['form']=form
    return render(request, 'addloan.html', context=pg_dict)
