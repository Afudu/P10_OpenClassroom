# Create a Secure RESTful API Using Django REST

**OpenClassrooms - Python Developer Path:** Project 10

**Student:** Abdoul Baki Seydou

**Date:** 04/03/2024

## Table of Contents
1. [Summary](#summary)
2. [Features](#features)
3. [API Endpoints](#api-endpoints)
4. [Technologies Used](#technologies-used)
5. [Project Tasks](#project-tasks)
6. [Local Development](#local-development)
   - [Prerequisites](#prerequisites)
   - [Setup on macOS/Linux](#setup-on-macoslinux)
   - [Setup on Windows](#setup-on-windows)
   - [Running the Application](#running-the-application)
   - [Linting and Testing](#linting-and-testing)
   - [Admin Panel](#admin-panel)

## Summary
This project consists of developing for **SoftDesk**, a product-based company, 
a secure a RESTful issue-tracking API.

The tracking application covers all three platforms (Web, Android, and iOS), and enables users to create projects, 
add users as contributors to a particular project, create issues in a project, and add comments to an issue.

## Features
- **Authentication & Authorization**: Role-based and Ownership-based secure access.
- **API Endpoints**: Support CRUD (create, read, update, and delete).

## API Endpoints 

| API Endpoint                    | HTTP Method | URI                                      | Permission             |
|---------------------------------|-------------|------------------------------------------|------------------------|
| User Signup	                    | POST        | /signup/                                 | Anyone above 16 yrs    |
| User Login                      | POST        | /login/                                  | Registered users       |
| List Projects of Logged-in User | GET         | /projects/                               | Owner and Contributors |
| Create a New Project            | POST        | /projects/                               | Registered users       |
| Get a Project                   | GET         | /projects/{id}/                          | Owner and Contributors |
| Update a Project                | PUT         | /projects/{id}/                          | Project Owner          |
| Delete a Project and its Issues | DELETE      | /projects/{id}/                          | Project Owner          |
| Add a Contributor to a Project  | POST        | /projects/{id}/contributors/             | Project Owner          |
| List all the Users in a Project | GET         | /projects/{id}/contributors/             | Project Owner          |
| Delete a User From a Project    | DELETE      | /projects/{id}/contributors/{id}         | Project Owner          |
| Get Issues of a Project         | GET         | /projects/{id}/issues/                   | Owner and Contributors |
| Create an Issue in a Project    | POST        | /projects/{id}/issues/                   | Owner and Contributors |
| Update an Issue in a Project    | PUT         | /projects/{id}/issues/{id}               | Issue Owner            |
| Delete an Issue in a Project    | DELETE      | /projects/{id}/issues/{id}               | Issue Owner            |
| Create Comments on an Issue     | POST        | /projects/{id}/issues/{id}/comments/     | Owner and Contributors |
| List all Comments on an Issue   | GET         | /projects/{id}/issues/{id}/comments/     | Owner and Contributors |
| Edit a Comment                  | PUT         | /projects/{id}/issues/{id}/comments/{id} | Comment Owner          |
| Delete a Comment                | DELETE      | /projects/{id}/issues/{id}/comments/{id} | Comment Owner          |
| Get a Particular Comment        | GET         | /projects/{id}/issues/{id}/comments/{id} | Owner and Contributors |

## Technologies Used
- **Programming Language:** Python  
- **Framework:** Django REST
- **Database:** SQLite
- **Back-end authentication** JWT (JSON Web Token)

## Project Tasks
1. Complete Designing Django models in Database Schema.
2. Create Serializers for data validation and transformation.
3. Create Views to handle API logic.
4. Define URL routes for the API.
5. Apply Permissions to the Views to ensure authorized access.

## Local Development

### Prerequisites
- PostgreSQL installed.
- Python 3.6 or higher.

### Setup on macOS/Linux

1. **Clone the Repository**
   ```bash
   cd /path/to/put/project/in
   git clone https://github.com/Afudu/P10_OpenClassroom.git

2. **Move to the folder**
   ```bash
   cd P10_OpenClassroom

3. **Set Up Virtual Environment**
   ```bash
   python -m venv venv
   
4. **Activate Environment**
   ```bash
   source venv/bin/activate 

5. **Securely upgrade pip**
   ```bash
   python -m pip install --upgrade pip 

6. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   
7. **To deactivate Environment**
   ```bash
   deactivate

### Setup on Windows

1. Follow the steps above.

2. To activate the environment:
   ```bash
   .\venv\Scripts\Activate

### Running the application

1. **Start the server**
   ```bash
   cd SoftDesk; python manage.py runserver
   
2. **Access in the browser**
- To register, navigate to:
  ```bash
  http://localhost:8000/api/signup

- To log in, navigate to:
  ```bash
  http://localhost:8000/api/login

### Admin Panel
1. Create a superuser account
   ```bash
   python manage.py createsuperuser
2. Navigate to:
   ```bash
    http://localhost:8000/admin
3. Use the superuser user created above to log in.

### Linting and Testing

- **Run Linting**
  ```bash
  flake8

- **Tests**

   * Signup and Login endpoints do not require an access token.
  
   * All other endpoints require an access token to work, and can be tested using [Postman](https://www.postman.com/) or any other tool like cURL or Django REST framework’s localhost server.
  
   * The tests performed and their results can be viewed from this [link](https://documenter.getpostman.com/view/25994788/2sA3JRafGj).