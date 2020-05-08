# FullThrottle Labs
This project is made to replicate the db.json given below. The project is designed and implemented with Django API and Django Rest Framework, made production ready and hosted on PythonAnywhere.

>{
>	"ok": true,
>	"members": [{
>			"id": "W012A3CDE",
>			"real_name": "Egon Spengler",
>			"tz": "America/Los_Angeles",
>			"activity_periods": [{
>					"start_time": "Feb 1 2020  1:33PM",
>					"end_time": "Feb 1 2020 1:54PM"
>				},
>				{
>					"start_time": "Mar 1 2020  11:11AM",
>					"end_time": "Mar 1 2020 2:00PM"
>				},
>				{
>					"start_time": "Mar 16 2020  5:33PM",
>					"end_time": "Mar 16 2020 8:02PM"
>				}
>			]
>		},
>		{
>			"id": "W07QCRPA4",
>			"real_name": "Glinda Southgood",
>			"tz": "Asia/Kolkata",
>			"activity_periods": [{
>					"start_time": "Feb 1 2020  1:33PM",
>					"end_time": "Feb 1 2020 1:54PM"
>				},
>				{
>					"start_time": "Mar 1 2020  11:11AM",
>					"end_time": "Mar 1 2020 2:00PM"
>				},
>				{
>					"start_time": "Mar 16 2020  5:33PM",
>					"end_time": "Mar 16 2020 8:02PM"
>				}
>			]
>		}
>	]
>}


## Getting Started 
```
git status
git add --all .
git commit -m "What changes you have made"
git push -u origin master
git clone https://github.com/nikhil-aniill/django_project
mkvirtualenv --python=python3.8 myvenv
pip install -r requirements.txt
cd django_project/ 
run manage.py migrate 
```
Since all this is already done and hosted on [Server](http://nikhilaniill.pythonanywhere.com).
1. ### To add data
  - Go to [Admin page](http://nikhilaniill.pythonanywhere.com/admin)
    with 
    Username:'Nikhil'
    Password:'1234'
  - Under MYAPI there are 3 Options :- 
      - Members - To create real name and tz(time zone) 
      - Periods - To mention the activity periods. 
      - Main_classs - To link Members which has manytomany relation
         > many-to-many relationship refers to a relationship between tables in a database when a parent row in one table contains several child rows in the second table, and vice versa.
2. ### To see the db.json 
   - Go to [API Root](http://nikhilaniill.pythonanywhere.com/) and click on [Members](http://nikhilaniill.pythonanywhere.com/Members/)
