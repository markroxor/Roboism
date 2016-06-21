[![Build Status](https://travis-ci.org/markroxor/Roboism.svg?branch=master)](https://travis-ci.org/markroxor/Roboism)
[![Dependency status](https://gemnasium.com/markroxor/Roboism.svg)](https://gemnasium.com/markroxor/Roboism)

## RoboISM - Running at roboism.pythonanywhere.com

###Issues to be sorted out -

* Go to templates -> active-members.html, there find div class="W3-accordion". Problem is that individual accordion for bio of each member cannot be opened. If clicked, only opens first bio. Please sort it out as soon as possible.


* In [fill_info.py](https://github.com/markroxor/Roboism/blob/master/mainsite/templates/registration/fill_info.html), I have styled it using CSS and Django. (See styling classes [here](https://github.com/markroxor/Roboism/blob/master/mainsite/forms.py) ) I want the names and fill boxes under each other, like

  Name: 
  [ fill box  ]
  
  Not like
  
  Name: [ fill box ]

* User identification is creating problem. 
```
user = request.user.username 
```
seem to give different and unpredictable results of user on different occations, which is resulting in wrong identification of current logged in user. 

```
if request.method == 'POST':
		details = MemberForm(request.POST)
		if details.is_valid():
			member = details.save(commit=False) 
			if request.user.is_authenticated():
				member.username = request.user.username // just here is problem
			member.save()
			return HttpResponseRedirect('/register/success/')
	else:
		details = MemberForm()
	return render(request, 'registration/fill_info.html', {'details': details})
```
	
See the whole code [here](https://github.com/markroxor/Roboism/blob/master/mainsite/views.py) of views.py.
