# Task Reservation

## Initial Setup

```
git clone https://github.com/AhmedELGAMMUDI/Test_Task.git

cd Test_Task

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
```
Seed the data 
```
python setup_and_seed.py
python manage.py runserver
```

for seeding large data

```
python setup_and_seed_large_data.py
python manage.py runserver
```

For reset the database 

```
python manage.py flush
```


