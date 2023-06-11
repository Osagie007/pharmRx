PharmRx
-----

## Introduction

PharmRx is a sample pharmacy website that can be used by any pharmacy or community phamacist for dispensing drugs. The website template was designed by [Colorib](https://Colorib.com/) and a functional backend made with Python and Django micro-service was employed for the development of this site.


## Overview

This web_app is complete as it features
* a functional ORM that can interface with any database for example MySQL, SQLite, PostgreSQL
* a functional admin page
* a functional checkout page integrated with paypal payment api(do not test it with real money)
* a functional search button
* last and not the least clean working code

I want PharmRx to be the next new platform that community pharmacists and pharmaceutical company sales' representatives can use to find each other, and discover new drugs. Let's make that happen!

## Tech Stack (Dependencies)

### 1. Backend Dependencies
Our tech stack will include the following:
 * **virtualenv** as a tool to create isolated Python environments
 * **Python3** and **Flask** as our server language and server framework
 * **Javascript** for DOM Manipulation
 * **PostgreSQL, SQLite or MySql** as our database of choice
 * **Html** as our markup language
 * **Css, FontAwesome and Bootstrap** for styles
You can download and install the dependencies mentioned above using `pip` as:
```
pip install django
```
> **Note** - If we do not mention the specific version of a package, then the default latest stable package will be installed. 

### 2. Frontend Dependencies
You must have the **HTML**, **CSS**, and **Javascript** with [Bootstrap 3](https://getbootstrap.com/docs/3.4/customize/) 

Install [Bootstrap 3](https://getbootstrap.com/docs/3.3/getting-started/) for the website's frontend:





Overall:
* Models are located in the `models.py`.
* Views are also located in `views.py`.
* The web frontend is located in `templates/`, which builds static assets deployed to the web server at `staticfiles/`.
* Ur;s for the ecommerce app are in `ULS.py`


**Endpoints:**
```
'/', 
/store/,
/cart/', 
/checkout/',
/about, 
/search,
/contact,
/product_info/<int:product_id>,
/update_item/,
/process_order/,
```

**Initialize and activate a virtualenv using:**
```
python -m virtualenv env
source env/bin/activate
```
>**Note** - In Windows, the `env` does not have a `bin` directory. Therefore, you'd use the analogous command shown below:
```
source env/Scripts/activate
```

**Install the dependencies:**
```
pip install -r requirements.txt
```

**Run the development server:**
```
python3 manage.py runserver
```

**Verify on the Browser**<br>
Navigate to project homepage [http://127.0.0.1:8000/](http://127.0.0.1:8000/) or [http://localhost:8000](http://localhost:8000) 



# THANK YOU !!!