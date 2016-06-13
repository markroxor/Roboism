from django.shortcuts import render

def index(request):
    return render(request, 'mainsite/frontpage.html', {})

def about_us(request):
	return render(request, 'mainsite/about-us.html', {})

def achievements(request):
	return render(request, 'mainsite/achievements.html', {})

def members(request):
	return render(request, 'mainsite/members.html', {})

def our_projects(request):
	return render(request, 'mainsite/our-projects.html', {})

def tutorials(request):
	return render(request, 'mainsite/tutorials.html', {})

def support_us(request):
	return render(request, 'mainsite/support-us.html', {})

def alumni(request):
	return render(request, 'mainsite/alumni.html', {})

def acitve_members(request):
	return render(request, 'mainsite/active-members.html', {})

def ongoing_projects(request):
	return render(request, 'mainsite/ongoing-projects.html', {})

def completed_projects(request):
	return render(request, 'mainsite/completed-projects.html', {})