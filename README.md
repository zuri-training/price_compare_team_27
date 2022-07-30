# price_compare_team_27
## Price Compare Team

## Project Documentation
 > [Documentation Link](https://docs.google.com/document/d/1qCUDKd5Hb_DAtzi2BKYs_Svso_pp2-m57vPPuYOYh74/edit?usp=drivesdk)





Follow these commands to run the proect on your local machine :

Clone the project 
```
git clone https://github.com/zuri-training/price_compare_team_27.git 
```

Enter the project directory 

```
cd price_compare_team_27
```

Create a virtual env

```
python -m venv env 
```

Activate your env(for windows)

```
./env/Scripts/activate 	 
```
(for linux or mac)

```
source env/bin/activate 
``` 

Install Project Dependencies

```
pip install -r requirements.txt
```

Make Migrations

```
python manage.py makemigrations
python manage.py migrate
```

Create Superuser

```
python manage.py createsuperuser
```

Run the server

```
python manage.py runserver
```

## To contribute :

### NOTE :

- Don't push to the main branch
- Create a branch and switch to it ` git checkout -b (branchname)` *Dont include brackets*
- After finishing your tasks run `git pull ` then `git push (your branchname)`

```
git add .
git commit -m " The task you did "
git push branchname 

```
