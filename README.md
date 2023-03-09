# TaskMenagementApp - Django Rest App

A simple DRF project to manage tasks
<hr>

## Table of contents
* General info
* Technologies
* Setup
* Status
* Other information
<hr>

## General info
The project was created to manage tasks assigned to employees.
Its assumption is to facilitate the work of people responsible for distributing tasks in a group and monitoring the status of tasks.
It has such functionalities as:
* task creation
* task editing
* task deletion
* preview of the list of all tasks
* preview of the list of filtered tasks
It works together with the PostgreSQL database<br><br>
The task itself takes the following values:
* ID
* Title
* Description
* Status
* Assigned user<br><br>
The project will be further developed and its final version will resemble a simple form of a CRM system. In addition, it will also have an improved visual version (front-end). HTML and CSS will be used for this purpose.
<hr>

## Technologies
* Python 3.10
* Django 
* Django Rest Framework
* PostgreSQL 15.2
<hr>

## Setup

Clone this repo to your desktop. Run this in any Python environment. From the terminal, start the virtual environment and then run the server.

Access to the PostgreSQL database is in the setting.py file in the application
### Usage <br>

After You clone this repo to your desktop and you'll open it in Python environment You have to open terminal and start the virtual environment by writing: `cd myenv/Scripts/activate`. Once you've done that, you can run the server by writing `py manage.py runserver`. Then You will see url adress which should look like `http://127.0.0.1:8000/`
, You have to run it.
<br>
Once you are on the project page, you will be able to go to several functions of the application.
The first without which you will not be able to do anything is registration:<br>
`http://127.0.0.1:8000/api/register/` <br> or login <br>
#### Application functionalities:
* List of all tasks (displays a list of all tasks in the database):
url address- `http://127.0.0.1:8000/api/task-list/`
<br>
* Filtered task list (displays a list of filtered tasks):
`http://127.0.0.1:8000/api/task-list/?=` at the end you have to specify what parameter you want to filter by. Examples:<br>
`http://127.0.0.1:8000/api/task-list/?id=8` <br>or<br>
`http://127.0.0.1:8000/api/task-list/?title=Second%20task`
<br>
* Task creation (displays the page where you can create a new task): `http://127.0.0.1:8000/api/task-create/`
<br>
* Updating and displaying task details (displays a page where you can see and edit task details): `http://127.0.0.1:8000/api/task-detail/` at the end you need to add task id
<br>
<hr>

## Status
Project is working on local server. I'm going to keep working on it. As I wrote at the beginning, this project will continue to develop and become a much larger and more useful tool similar to the CRM system 
<hr>

## Inspiration
This app is inspired by <strong>Antonio Mele</strong> book <strong>"Django 3 By Example"</strong>.
<hr>

#### Postscriptum
This is my first project using Django Rest Framework and PostgreSQL database.<br>