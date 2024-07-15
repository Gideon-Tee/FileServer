# Django File Server Project

This project is a file server application built using Django. It allows users to sign up, log in, view and download files, and send files via email. Admins can upload new files and see the number of downloads and emails sent for each file.

## Features

- User authentication (signup, login, logout) with email verification
- Password reset functionality
- Upload files with a title and description (Admin)
- View and download files
- Search for files
- Send files to an email through the platform
- View number of downloads and emails sent (Admin)

## Prerequisites

- Python 3.8+
- Django 4.2+
- pip (Python package installer)

## Usage

### User Authentication
1. **Sign Up:**
   
  Users sign up with an email address and password. Email verification is required

3. **Log In:**
   
   Users log in with their registered email and password

4. **Password Reset:**
   
   Users can reset their password through their email addresses

### File Management
- Logged in users can view a list of available files
- Logged in users can download files
- Logged in users can share files via email on the platform
- There's the search funtionality to allow users search the file server

  **Admin Functionalities**
- Upload files to the server with title and description
- View file statistics ( number of downloads and shares per file)

## Deployed Link

Default Superuser details

-email : `gideonlambride@gmail.com`

-password : `admin`

-link : https://lizzydocuments.pythonanywhere.com

**A little note**: The page is best rendered on a laptop or a larger screen than that of a mobile phone


## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/gideon-tee/FileServer.git
   cd FileServer
   ```
   
2. **Create and Activate a virtual environment**
   ```bash
   python3 -m venv myvenv # myvenv could be anything, the name of the virtualenv
   source myvenv/bin/activate # on windows, use myvenv\Scripts\activate
   ```
3. **Install the dependencies and requirements**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create environment variables**
   Create a `.env` file at the root of the directory and add your email address and an app password where applicable:
   ```bash
   EMAIL_ADDRESS=your-email-address
   EMAIL_PASSWORD=password
   ```

5. **Run Migrations**
   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python3 manage.py createsuperuser
   ```

7. **Run the server**
   ```bash
   python3 manage.py runserver
   ```



  
   
