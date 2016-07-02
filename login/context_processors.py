from django.contrib.auth import authenticate
from django.contrib.auth.models import User

def login_info(request):
	if request.user.is_authenticated:
		name = request.user.username
		return {'name':name}