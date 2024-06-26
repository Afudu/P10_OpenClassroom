# OpenClassrooms - Python Developer Path

**Project 10:** Create a Secure RESTful API Using Django REST

**Student:** Abdoul Baki Seydou

**Date:** 04/03/2024

# Abstract
This project consists of developing for SoftDesk, a product-based company that produces software development
and collaboration tools, a RESTful issue-tracking API using the Django REST framework.

The tracking application covers all three platforms (Web, Android, and iOS), and would enable users to create projects, 
add users as contributors to a particular project, create issues in the project, and add comments to the issues.

In addressing the OWASP(Open Worldwide Application Security Project) vulnerability checks to be implemented,
the application uses JWT (JSON Web Token) for back-end authentication and Django REST Permissions, 
and guarantees the following main features:

- Only authenticated users should be able to access anything on the application.
- Only project author and contributors are able to access it.
- Only project author should be able to add contributors, update and delete the project. 
- Only project contributors should be able to:
  - create or access issues in a project, 
  - create & read comments on an issue, 
  - update & delete issues or comments if they are the author.

The design follows the diagram of the database schema provided, 
and GDPR standards have been adhered to by allowing users to update and delete their own data.

In meeting the project's deliverables requirements, all the required API Endpoints and their URIs have been tested documented 
in a collection in Postman, and published on the web. The link is provided in the deliverables.

# Requirement

Latest version of Python must be installed.

You can download the latest version for your system from : https://www.python.org/downloads/

# Installation

The following commands rely on the knowledge of how to use the terminal (Unix, macOS) or the command line (Windows).

**1 - Get the code**

  * $ git clone https://github.com/Afudu/P10_OpenClassroom.git

**2 - Move to the folder**

  * Unix/macOS/Windows: cd P10_OpenClassroom

**3 - Create a virtual environment**

  * Unix/macOS: $ python3 -m venv pythonenv
  * Windows: py -m venv pythonenv
  
    * Note: you can create the virtual environment in another folder, then move to that folder to run the command above.
    * Example: in the above command, our virtual environment created is called pythonenv - you can give a different name.

**4 - Activate the virtual environment created**

  * Unix/macOS: $ source pythonenv/bin/activate

  * Windows: pythonenv\Scripts\activate

**5 - Securely upgrade pip**

 * Unix/macOS/Windows: pip install --upgrade pip

**6 - Install all dependencies**

 * Unix/macOS/Windows: pip install -r requirements.txt

# Running the application
In the terminal (Unix, macOS) or command line (Windows):
1- Move to the SoftDesk folder : cd SoftDesk
2 - Start the server: python manage.py runserver

# Testing the application
After the server has started,  navigate to http:/localhost:8000/api/login to check the api,
Use the account:
Username = User_Account_1
Password = Password01
For tests, go to Postman - https://www.postman.com/

# PEP 8 adherence

The folder 'flake_report' in the repository contains an HTML report generated by flake8-html which displays no errors.
A new report can be generated by running the following command in the terminal (Unix, macOS) 
or command line (Windows): flake8

The file setup.cfg in the root of the repository contains the settings used to generate the report.
