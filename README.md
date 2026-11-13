# PaintPro
Web application for residential and commercial painting businesses.

# Exceutive Summary
PaintPro is a web application designed to help painting companies organize and support daily operations. The goal is to provide a centralized platform where business owners can manage painting projects, assign crew members to job sites, maintain customer 
information, create estimates, and track invoices. The app features a dashboard that displays active and completed project, expected revenue, payments received, and outstanding customer balances.

The app also supports multiple user roles, including business owner, administartor, crew members. Role-based access controls help ensure that employees can access the information needed for their responsibliies.

# Installation
1. Clone Repository
``` powershell
git clone https://github.com/damianramirez07/PaintPro.git
```
2. Navigate to project folder
```powershell 
cd PaintPro
```
3. Create virtual environment
```powershell
python -m venv venv
```

4. Activate virtual environment
```powershell 
.\venv\Scripts\Activate.ps1 
```

Note: If you receive an error, run the following before moving onto next step: 
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

5. Install Django
```powershell 
python -m pip install Django==5.2.19
```

6. Apply migrations
```powershell
 python manage.py migrate
```

# Getting Started
1. Once the app is installed start the Django server
python manage.py runserver

2. Open a web browser and go to:
http://127.0.0.1:8000/

Note: Ctr + C to stop server 

# License

PaintPro is licensed under MIT License. Check out the LICENSE file for more details.
