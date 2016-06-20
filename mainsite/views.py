from django.shortcuts import render, redirect
from .models import Member, Project
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from .forms import *

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form':form})

def register_success(request):
    return render_to_response('registration/fill_info.html',)

@login_required
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def userprofile(request):
    try:
    	member = Member.objects.get(username=request.user.username)
    	return render(request, 'mainsite/profile.html', {'member':member})
    except ObjectDoesNotExist:
    	return render(request, 'mainsite/404.html', {})

def index(request):
    return render(request, 'mainsite/frontpage.html', {'user': request.user })

def about_us(request):
	return render(request, 'mainsite/about-us.html', {})

def achievements(request):
	return render(request, 'mainsite/achievements.html', {})

def members(request):
	member = Member.objects.filter()
	class Count:
		first = second = third = fourth = alumni = 0

	count = Count()
	for m in member:
			if m.active == False:
				count.alumni += 1
			else:
				if m.year == "First Year":
					count.first += 1
				elif m.year == "Second Year":
					count.second += 1
				elif m.year == "Third Year":
					count.third += 1
				elif m.year == "Final Year":
					count.fourth += 1

	return render(request, 'mainsite/members.html', {"count":count})

def our_projects(request):
	project = Project.objects.all()
	class Count:
		total = ongoing = completed = 0

	count = Count()
	for p in project:
		if p.completed:
			count.completed += 1
		else:
			count.ongoing += 1
	count.total = count.completed + count.ongoing

	return render(request, 'mainsite/our-projects.html', {'count':count})


def tutorials(request):
	return render(request, 'mainsite/tutorials.html', {})

def support_us(request):
	return render(request, 'mainsite/support-us.html', {})

def alumni(request):
	member = Member.objects.filter(active = False)
	return render(request, 'mainsite/alumni.html', {'member':member})

def active_members(request):
	member = Member.objects.filter(active = True)
	return render(request, 'mainsite/active-members.html', {'member':member})

def ongoing_projects(request):
	project = Project.objects.filter(completed=False)
	return render(request, 'mainsite/ongoing-projects.html', {'project':project})

def completed_projects(request):
	project = Project.objects.filter(completed=True)
	return render(request, 'mainsite/completed-projects.html', {'project':project})

def fill_info(request):
	if request.method == 'POST':
		details = MemberForm(request.POST)
		if details.is_valid():
			member = details.save(commit=false)
			member.username = request.user.username
			member.password1 = request.user.password1
			member.password2 = member.password1
			member.email = request.user.email
			member.pic = details.cleaned_data['pic']
			member.name = details.cleaned_data['name']
			member.branch = details.cleaned_data['branch']
			member.work = details.cleaned_data['work']
			member.DOB = details.cleaned_data['DOB']
			member.year = details.cleaned_data['year']
			member.bio = details.cleaned_data['bio']
			member.linkedin = details.cleaned_data['linkedin']
			member.resume = details.cleaned_data['resume']
			member.active = details.cleaned_data['active']
			member.save()
			return HttpResponseRedirect('/profile/')
	else:
		form = MemberForm()
	return render(request, 'registration/fill_info.html', {'details':details })
