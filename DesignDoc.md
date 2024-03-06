### JOB FINDER DESIGN SPECIFICATION DOCUMENT
## Introduction
The Job Finder Application is a platform made to assist admin in posting job listings and job seekers in finding opportunities for suitable employment. This document describes the Job Finder Application's architecture, features, and design requirements. 
## Objectives
* Provide a user-friendly interface for job seekers to search and apply for jobs.
* Allows the admin to add and delete the jobs.
* Make it possible for employers to effectively and efficiently post job listings.
* Provide comprehensive search tools to help job searchers find relevant job postings.
## Functional Requirements 
D.1. User Registration:
* D.1.1 When a user enters all the required details using the form, and click on signup button, Validations will happen (Validating mobile number, date of birth and email) then we will make an api request to the backend. The backend will verify the user details (checking if the email is already registered). If everything goes well, the backend will store the user information in the database and send the successful response to the frontend. It will send a failure response if anything goes wrong.
* D.1.2 If the backend sends the failure response with error message in it, The frontend will display the error message which is received from backend.
* D.1.3 After the user is registered, Then the user will be able to login with the correct credentials. When user clicks on login button after entering the details, Then it sends the details (entered by the user) to the backend. Then backend will verify the user credentials (by looking to the database). If the details are correct, the backend will send a successful response, or else a failure response.
* D.1.4: If the response is success, the frontend will redirect the user to the home page. If the front-end get a failure response from the backend, The front-end will display an error.

D.2 Searching and Filtering:
* D.2.1: When a user enters a keyword in the search field and clicks on search button, the frontend makes api call to the backend. The backend will fetch the corresponding data from database using the keyword which is sent by the frontend. If the database does not contains any data for the keyword, It sends empty list of jobs to the frontend.
* D.2.2: The home page contains list of job types (Categories). When user selects any category, Frontend makes api call to backend to fetch all the jobs available for the category (which is selected by the user) and displays it.

D.3 Job Listing and Details:
* D.3.1: Whenever user clicks on any job, The frontend will display all the information about job in a new page in detail.
 
D.4 Employer management:
* D.4.1: The Admin can manage the users and user profiles. There will be some pages, those are hidden from normal users. Only Admin can access the admin related pages(Admin can Create,Update and Delete any user using User interface).
* D.4.2: Admin will upload any new job using create-job page, where admin enters the job details like title, salary range, category,company details etc,. When Admin clicks on submit/upload button, all the job details sent to the backend. The backend will store the job details in the database and sends the success response. If anything goes wrong, the backend will send the failure response.
* D.4.3: There will be separate pages (accessible only to the Admins) to edit the job and delete it.  

D.5 Settings and Security:
* D.5.1: When user changes any information and clicks on update button, Frontend makes an api call to the backend to update the corresponding user information. The backend will update user information in the database and then respond to the frontend.
* D.5:2: When user clicks on logout button, The session will the destroyed and redirected to the login page.

# Front-end
* Language: Python • Framework: Flask
* Libraries used in Frontend: • Flask • Jinja2 • Flask-WTF • WTForms • Requests
# Database:
* MYsql
# Backend: 
* Language: Python 
* Framework: Flask
* Libraries used in Backend: 
* Flask-Migrate 
* Jinja2 template 
* Mysqlclient 
* SQL alchemy - to connect with database
# Tools: 
* Visual Studio Code
* Mysql workbench

