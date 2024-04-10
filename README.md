# Ecommerce Backend (Enactus Thapar Task)
A REST-API based backend for a startup catering to sustainable products. 

## Tech Stack
[Django](https://www.djangoproject.com/), [SQLite](https://www.sqlite.org/), [Django REST Framework](https://www.django-rest-framework.org/), HTML/CSS/JS

## Features

1. Perform CRUD operations on a product database which stores information about product descriptions, material composition, performance specifications, pricing, inventory levels, suppliers.

2. Manage product availability through tracking and managing suppliers and inventory levels.

3. Shopping cart system where users can add/remove products.

4. Admin website for interacting and managing all of the above.

5. User accounts with profile photos and bio.

6. Protected through [knox](https://jazzband.github.io/django-rest-knox/) (a better and more secure alternative to the standard TokenAuthentication provided by the Django REST Framework).

>**Note:** For ease of deployment and developement time constraints, sqlite database has been used. However, the backend will work just fine with any other database backends supported by Django.

## Endpoints
1. `admin/` - To navigate to admin site.
2. `products/create/` - To create a new product.
3. `products/alter/<int:pk>` - GET for retrieving product, PUT for updating, DELETE for deleting.
4. `suppliers/create/` - To create a new product.
5. `suppliers/alter/<int:pk>` - GET for retrieving supplier, PUT for updating, DELETE for deleting.
6. `shopping-cart/add-item/` - To add an item to the currently logged-in user's cart.
7. `shopping-cart/remove-item/<int:itemid>` - Remove specified item from currently logged-in user's cart if it exists.
8. `shopping-cart/view-cart/` - To view the contents of the currently logged-in user's cart
9. `user-management/` - POST with Username, Email, Password to create a user (customer/buyer) account
10. `user-management/login/` - POST with credentials to log in.
11. `user-management/logout/` - POST to logout
12. `user-management/update-profile-photo/<filename>` - To update the profile photo of the currently logged in user
13. `user-management/user-info/` - To get details of the currently logged in user

>**Note**: `user-management/login/` upon success will return a token. For subsequent requests to the server this token must be included in the request headers as `Authorization: Token <Yout-Token>`. By default each of these tokens are valid for 10 hours since they are issued and are destroyed if the corresponding user logs out.

## Setup
1. Clone the repo via `git clone https://github.com/B4S1C-Coder/Enactus-Backend-Task-Ecommerce-Backend.git`

2. Install dependencies via (make sure you are in the same directory as `manage.py`) `pip install -r requirements.txt`

3. Don't forget to `makemigrations` and `migrate`

4. You should now be good to go.