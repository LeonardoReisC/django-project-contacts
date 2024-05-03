# django-project-contacts

This repo showcases a web application developed using the Django Framework and Django-Templates, aimed at facilitating the storage and management of contact information for users. Inspired by [Otávio Miranda's](https://www.otaviomiranda.com.br) Python course.

## Features

### Home

The Home page displays a list of contacts where users can see their saved contacts.

![Home Page](/images/home.png)

### Login/Register

The Login/Register page allows users to create an account or log in to an existing account.

![Login Page](/images/login.png)

![Register Page](/images/register.png)

### Create

The Create page enables logged-in users to add new contacts to their account.

![Create page](/images/create.png)

### Detail

The Detail page provides a detailed view of each contact, including the ability to update or delete contacts if the logged-in user is the contact creator.

![Detail page](/images/detail.png)

## Getting Started

To run this Contacts Web Application locally, follow these steps:

- **Clone the Repository**

  ```bash
  git clone https://github.com/LeonardoReisC/django-project-contacts.git
  ```

- **Install Dependencies** 

  ```bash
  pip install -r requirements.txt
  ```

- **Migrate Database**

  ```bash
  python manage.py migrate
  ```

- **Seed Database (Optional)**

  ```bash
  python ./utils/create_contacts.py
  ```

- **Start the Application**

  ```bash
  python manage.py runserver
  ```

***
