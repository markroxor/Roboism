[![Build Status](https://travis-ci.com/markroxor/Roboism.svg?token=FzX7CPA4K1qbQP1HdyLt&branch=master)


## RoboISM - Running at [roboism.markroxor.in](roboism.markroxor.in)

RoboISM is the official site of Robotics Club ISM Dhanbad. Well right now it is ![alt tag](https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQpNgHwfZ40zcRFx2AJ-17aoqeQF9xR53Ho-dPXPh7mku_uaETCjg)


####For Newbies: How to run code locally ?
* Clone your code into your PC. Let the folder name be Roboism. 
* Install python 3 in your PC. Preferably in default directory (C:/)
* delete Roboism/myvenv folder
* Open Command Prompt and cd into the directory (Roboism). <br>
  For Window Users:-
  ```C:\Python34\python -m venv myvenv```<br>
  For Linux Users and OS X Users:-
  ```python 3 -m venv myvenv```<br>

* Then do <br>
  For Window Users:- ```myvenv\Scripts\activate```<br>
  For Linux Users and OS X Users:-
  ```source myvenv/bin/activate``` <br>
  Now, you should see a (myvenv) script before cmd commands. <br>

* Now, do
  ```pip install django==1.9.7```

* After installation is complete, do
  ```python manage.py makemigration mainsite```
  And 
  ```python manage.py migrate mainsite```
  And
  ```python manage.py collectstatic```

* Finally, to run a virtual server, do
  ```python manage.py runserver```
  Go to any browser, type this url '127.0.0.1:8000' without quotes. If everything went as planned, you will see the site locally. <br>
  Make any changes the code and see the change reflected on the locally hosted site. 


