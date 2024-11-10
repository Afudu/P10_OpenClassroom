# OpenClassrooms - Python Developer Path

**Project 10:** Create a Secure RESTful API Using Django REST

**Student:** Abdoul Baki Seydou

**Date:** 04/03/2024

## Abstract
This project consists of developing for SoftDesk, a product-based company that produces software development
and collaboration tools, a RESTful issue-tracking API using the Django REST framework.

The tracking application covers all three platforms (Web, Android, and iOS), and enables users to create projects, 
add users as contributors to a particular project, create issues in a project, and add comments to an issue.

In addressing the OWASP(Open Worldwide Application Security Project) vulnerability checks to be implemented,
the application uses JWT (JSON Web Token) for back-end authentication with Django REST Permissions, 
and guarantees the following required features:

- Only authenticated users are able to access anything on the application.
- Only a project's author is able to add contributors, update and delete the project. 
- Only a project's author and its contributors are able to access it.
- Only a project's contributors are able to:
  - create or access issues in the project, 
  - create & read comments on an issue, 
  - update & delete issues or comments if they are the author.

The design follows the diagram of the database schema provided, 
and GDPR standards have been adhered to with data share and contact consents, 
and allowing users to access and update only their own account.

### API Endpoints 

| API Endpoint                          | HTTP Method | URI                                      |
|---------------------------------------|-------------|------------------------------------------|
| User Signup	                          | POST        | /signup/                                 |
| User Login                            | POST        | /login/                                  |
| List Projects of the Logged-in User   | GET         | /projects/                               |
| Create a New Project                  | POST        | /projects/                               |
| Get a Project                         | GET         | /projects/{id}/                          |
| Update a Project                      | PUT         | /projects/{id}/                          |
| Delete a Project and its Issues       | DELETE      | /projects/{id}/                          |
| Add a User (contributor) to a Project | POST        | /projects/{id}/contributors/             |
| List all the Users in a Project       | GET         | /projects/{id}/contributors/             |
| Delete a User From a Project          | DELETE      | /projects/{id}/contributors/{id}         |
| Get Issues of a Project               | GET         | /projects/{id}/issues/                   |
| Create an Issue in a Project          | POST        | /projects/{id}/issues/                   |
| Update an Issue in a Project          | PUT         | /projects/{id}/issues/{id}               |
| Delete an Issue in a Project          | DELETE      | /projects/{id}/issues/{id}               |
| Create Comments on an Issue           | POST        | /projects/{id}/issues/{id}/comments/     |
| List all the Comments on an Issue     | GET         | /projects/{id}/issues/{id}/comments/     |
| Edit a Comment                        | PUT         | /projects/{id}/issues/{id}/comments/{id} |
| Delete a Comment                      | DELETE      | /projects/{id}/issues/{id}/comments/{id} |
| Get a Particular Comment              | GET         | /projects/{id}/issues/{id}/comments/{id} |

## Requirement

Latest version of Python must be installed.

You can download the latest version for your system from : https://www.python.org/downloads/

## Installation

The following commands rely on the knowledge of how to use the terminal (Unix, macOS) or the command line (Windows).

**1 - Get the code**

   * Unix/macOS/Windows

       ```bash
       git clone https://github.com/Afudu/P10_OpenClassroom.git
       ```

**2 - Move to the folder**

   * Unix/macOS/Windows

       ```bash
       cd P10_OpenClassroom
       ```  

**3 - Create a virtual environment**

  * Unix/macOS

    ```bash
    python3 -m venv pythonenv
     ```
  * Windows

    ```bash
    py -m venv pythonenv
    ```
  
    * Note: you can create the virtual environment in another folder, then move to that folder to run the command above.
    * Example: in the above command, our virtual environment created is called pythonenv - you can give a different name.

**4 - Activate the virtual environment created**

  * Unix/macOS

    ```bash
    source pythonenv/bin/activate
    ```

  * Windows

    ```bash
    pythonenv\Scripts\activate
    ```

**5 - Securely upgrade pip**

   * Unix/macOS/Windows

      ```bash
     pip install --upgrade pip
     ```

**6 - Install all dependencies**

  * Unix/macOS/Windows

    ```bash
    pip install -r requirements.txt
    ```

## Running the application

**Move to the folder**

  * Unix/macOS/Windows

      ```bash
      cd SoftDesk
      ```

**Start the server**

  * Unix/macOS/Windows

    ```bash
    python manage.py runserver
    ```

## Testing the application
After the server has started, the API can then be tested by navigating to:

* Signup:  http://localhost:8000/api/signup
* Login :  http://localhost:8000/api/login

Or use the account below to log in:

 * Username = User_Account_1
 * Password = Password01

Signup and Login endpoints are the only ones that don't require an access token.

All other endpoints require an access token to work, and can be tested using [Postman](https://www.postman.com/) 
or any other tool like cURL or Django REST framework’s localhost server.

All required API Endpoints have been tested, documented, 
and [published](https://documenter.getpostman.com/view/25994788/2sA3JRafGj) on Postman.

The database used is in the file ```db.sqlite3``` located in ```SoftDesk``` folder.

# PEP 8 adherence

The folder ```flake_report``` in the repository contains an HTML report generated by flake8-html which displays no errors.
A new report can be generated by running the following command: 

  * Unix/macOS/Windows

      ```bash
        flake8
       ```

The file ```setup.cfg``` in the root of the repository contains the settings used to generate the report.
