# Ecommerce Backend (Enactus Thapar Task)
A REST-API based backend for a startup catering to sustainable products. 

## Tech Stack
[Django](https://www.djangoproject.com/), [SQLite](https://www.sqlite.org/), [Django REST Framework](https://www.django-rest-framework.org/), HTML/CSS/JS

## Features

1. Perform CRUD operations on a product database which stores information about product descriptions, material composition, performance specifications, pricing, inventory levels, suppliers.

2. Manage product availability through tracking and managing suppliers and inventory levels.

3. Shopping cart system where users can add/remove products.

4. Admin website for interacting and managing all of the above.

5. Protected through [knox](https://jazzband.github.io/django-rest-knox/) (a better and more secure alternative to the standard TokenAuthentication provided by the Django REST Framework).

>**Note:** For ease of deployment and developement time constraints, sqlite database has been used. However, the backend will work just fine with any other database backends supported by Django.

## Setup
1. Clone the repo via `git clone https://github.com/B4S1C-Coder/Enactus-Backend-Task-Ecommerce-Backend.git`

2. Install dependencies via (make sure you are in the same directory as `manage.py`) `pip install -r requirements.txt`

3. Don't forget to `makemigrations` and `migrate`

4. You should now be good to go.