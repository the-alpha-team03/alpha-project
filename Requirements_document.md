# Requirements

 ## Functional Requirements:

  R.1. User Registration:
  * R.1.1 Users should be able to register with the required information including name, age, mobile number, DOB, address, email and password.
  * E.1.1 This requirement states that users should be able to register with necessary information. It's a fundamental feature of user registration systems. To evaluate this, you would check if the system allows users to input all the required information (name, age, mobile number, DOB, address, email, and password) and successfully registers them.
  * R.1.2 Proper error messages should be displayed if registration fails due to invalid input.
  * E.1.2 Proper error messages are crucial for user-friendly registration systems. To evaluate this, you would check if the system displays clear and descriptive error messages when users input invalid data or encounter other registration errors. This could include messages such as "Invalid email address" or "Password must be at least 8 characters long".
  * R.1.3  Registered users should be able to sign in using valid credentials.
  * E.1.3 This requirement ensures that registered users can successfully sign in using their credentials. To evaluate this, you would check if the system allows registered users to input their email and password and successfully logs them in if the credentials are valid.
  * R.1.4  Login Button: Triggers user authentication, redirects to the dashboard or displays error.
  * E.1.4 The login button's functionality is critical for user authentication. To evaluate this, you would check if clicking the login button triggers the authentication process, verifies the user's credentials, and redirects them to the dashboard upon successful login. Additionally, the system should display appropriate error messages if authentication fails.
  * R.1.5 SignUp Button: Redirects to registration, handles input and registration process.
  * E.1.5 The signup button's functionality is essential for initiating the registration process. To evaluate this, you would check if clicking the signup button redirects users to the registration page where they can input their information. The system should guide users through the registration process and handle input validation effectively.


  R.2. Searching and Filtering:
  * R.2.1 Enable job search by job title, location, industry, salary range, and keyword.
  * E.2.1 Enabling job search by various criteria such as job title, location, industry, salary range, and keyword is crucial for users to find relevant job opportunities. To evaluate this, check if the system allows users to input their search criteria using these parameters and returns accurate results matching the search query.
  * R.2.2 Implement filters for refining search results by job type.
  * E.2.2 Implementing filters for refining search results by job type enhances the search experience for users. To evaluate this, verify if the system provides options for users to filter search results based on job types (e.g., full-time, part-time, contract, etc.) and if these filters effectively narrow down the search results.
  * R.2.3 Provide a user-friendly interface for users to easily input their search criteria and apply filters to find relevant job opportunities.
  * E.2.3 Providing a user-friendly interface for users to input their search criteria and apply filters is essential for a positive user experience. To evaluate this, assess the interface's intuitiveness and ease of use. Check if users can easily input their search criteria, apply filters, and navigate through the search results without encountering usability issues.
 
  R.3. Job listing and Details:
  * R.3.1 Display job postings with key details: title, salary range, category, company, email and description.
  * E.3.1 Displaying job postings with key details such as title, salary range, category, company, email, and description is necessary for users to evaluate job opportunities. To evaluate this, check if the system presents job listings in a clear and organized manner, displaying all relevant details prominently for users to review.
  * R.3.2 Allow users to access complete job descriptions, including responsibilities, requirements, qualifications, benefits, and instructions.
  * E.3.2 Allowing users to access complete job descriptions, including responsibilities, requirements, qualifications, benefits, and instructions, provides them with comprehensive information about the job. To evaluate this, verify if users can access detailed job descriptions by clicking on individual job postings and if these descriptions contain all necessary information.

  R.4. Employer management:
  * R.4.1 User registration and profile management for employers.
  * E.4.1 Enabling user registration and profile management for employers is essential for them to interact with the platform effectively. To evaluate this, check if the system allows employers to register accounts, create profiles, and manage their profile information such as company details, contact information, etc.
  * R.4.2 Posting and managing job listings.
  * E.4.2 Allowing employers to post and manage job listings is a key functionality for employer management. To evaluate this, verify if employers can create new job listings, edit existing listings, and manage their listings effectively, including options to deactivate or remove postings when necessary.
  * R.4.3 Enable employers/Admin to edit and delete job postings.
  * E.4.3 Enabling employers/administrators to edit and delete job postings adds flexibility and control over job listings. To evaluate this, check if employers/administrators have the necessary permissions and tools to edit or delete job postings as needed, ensuring accuracy and relevance of the listings on the platform.

  R.5. Settings and Security:
  * R.5.1 Display user information in the settings section, allowing users to update their details.
  * E.5.1 Displaying user information in the settings section and allowing users to update their details is important for maintaining accurate user profiles and preferences. To evaluate this, check if the system provides a settings section where users can view and edit their profile information such as name, email, address, etc. Additionally, verify if users can successfully update their details and if changes are reflected accurately across the platform.
  * R.5.2 Include a logout option for users to securely log out of their accounts.
  * E.5.2 Including a logout option for users to securely log out of their accounts is essential for maintaining account security and privacy. To evaluate this, check if the system provides a logout option prominently accessible from any page within the platform. Verify if clicking on the logout option successfully logs the user out of their account and redirects them to a secure logout page or the login page, ensuring that the user session is terminated effectively.

 ## Non - Functional Requirements:

  1. Performance: Ensure fast response times and minimal latency for user interactions, maintaining high usability.
  2. Security: Implement robust measures to protect user data and ensure confidentiality, integrity, and availability.
  3. Compatibility: Ensure the application works seamlessly across various devices, browsers, and operating systems.
  4. Reliability: Ensure the system operates consistently without unexpected downtime, with reliable error handling mechanisms in place.
  5. Maintainability: Design the codebase with clear documentation and modular structure to facilitate easy maintenance and updates over time.



 ## Technical Requirements:

 #### 1. Frontend:
  * Language: Python
  * Framework: Flask
 ##### Libraries used in Frontend:
   * Flask
   * Jinja2
   * Flask-WTF
   * WTForms
   * Requests

  #### 2. Database:
   * MYsql

  #### 3. Backend:
   * Language: Python
   * Framework: Flask
  ##### Libraries used in Backend:
   * Flask-Migrate
   * Jinja2 template
   * Mysqlclient
   * SQL alchemy - to connect with database

 #### Tools:
   * Visual Studio Code
   * Mysql workbench







   
