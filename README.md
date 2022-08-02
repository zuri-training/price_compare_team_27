# Team 27 Price_compare 

### Pricify
What is Pricify? Pricify is a price comparison website which focuses on comparing phone prices across various brands such as Nokia, Samsung, iPhone, Tecno and a host of other phone manufacturing brands, for the sole aim of helping a user get the best price.

### Project Documentation
 > [Team 27_Price_compare Documentation](https://docs.google.com/document/d/1qCUDKd5Hb_DAtzi2BKYs_Svso_pp2-m57vPPuYOYh74/edit?usp=drivesdk)
 
### Presentation Slides
> [Team 27_Price_compare  Slides](https://www.figma.com/proto/BzsR8MmSXhHvMYbPWx9Q7b/Pricify?node-id=897%3A3499&scaling=contain&page-id=856%3A3905)

### Figma Link
> [Team 27_Price_compare  Figma ](https://www.figma.com/file/BzsR8MmSXhHvMYbPWx9Q7b/Price-Compare?node-id=2%3A3)

### Figjam Link
> [Team 27_Price_compare  FigJam](https://www.figma.com/file/HppxK2j0nylpMF2OPuQaMB/Pricify-Sketch)

### List of Tasks
> [Team 27_Price_compare List of Tasks](https://docs.google.com/spreadsheets/d/1VVzcnnJz0iOHUNQ_6cVq_wheTDTpOR9279F6vc6_mng/edit?usp=sharing)

### Database Schema Link
> [Team 27_Price_compare DbSchema](https://drive.google.com/file/d/1Jt6g3BtvkQ-vgUHi05RfARbAF0o6whep/view?usp=sharing)

## Follow these commands to run the proect on your local machine :

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

Setting up default data

```
python manage.py loaddata Brand.json
python manage.py loaddata phones.json
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
Thanks
