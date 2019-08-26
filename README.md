# myshop
a demo shopping api with items brands and categories

-----------------------------------------------------------------------------

To run This Project on your local machine

1. clone this project
2. create virtual environment (python > 3) and activate it.
3. RUN ---  cd myshop  --- 
4. RUN ---  pip install -r requirements.txt ---
5. RUN --- cd myshop && python manage.py migrate ---
6. RUN --- python manage.py createsuperuser ---
7. RUN --- python manage.py runserver --- 

------------------------------------------------------------------------------

By default we get two test users with below ids and passwords
1. username = testuser1 , password = shop@123
2. username = testuser2 , password = shop@123

API Defenitions

------------------------------------------------------------------------------

GET localhost:8000/brands/ (access for admin and testusers)
POST localhost:8000/brands/ {"brand_name" : "mynewbrand"} (access only for admin)

GET localhost:8000/brands/id/ (access for admin and testusers)
PUT localhost:8000/brands/id/ {"brand_name" : "mynewbrand"} (access only for admin)
DELETE localhost:8000/brands/id/ (access only for admin)

------------------------------------------------------------------------------

GET localhost:8000/items/ (access for admin and testusers)
POST localhost:8000/items/ {"item_name" : "mynewitem , "item_quantity" : 5, "item_brand" : 1, "item_category" : 1} (access only for admin)

GET localhost:8000/items/id/ (access for admin and testusers)
PUT localhost:8000/items/id/ {"item_name" : "mynewitem , "item_quantity" : 5, "item_brand" : 1, "item_category" : 1} (access only for admin)
DELETE localhost:8000/items/id/ (access only for admin)

------------------------------------------------------------------------------

POST localhost:8000/orders/ {"order_item" : 2} (access for testusers only)

------------------------------------------------------------------------------