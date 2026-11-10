Django Job Portal

A web-based Job Portal application developed using **Python and Django**. The platform connects job seekers with recruiters, allowing candidates to explore job opportunities and apply for positions while recruiters can publish job openings and manage applications.

🚀 Features

 👨‍💻 Job Seeker
- User registration and authentication.
- Browse available job opportunities.
- Search and filter jobs.
- Apply for jobs with resume uploads.
- Manage uploaded resumes.
- Track application history and application status.
- Access a personalized dashboard.

 🏢 Recruiter
- Recruiter registration and authentication.
- Create and publish job vacancies.
- Edit and delete job postings.
- Manage published job listings.
- View applicants for each job.
- Update application statuses.
- Access a recruiter dashboard.

 🛠️ Technologies Used

| Category | Technologies |
|---|---|
| Backend | Python, Django |
| Frontend | HTML, CSS, Bootstrap 5 |
| Database | SQLite (Development), PostgreSQL (Production configuration) |
| Static Files | WhiteNoise |
| Application Server | Gunicorn |
| Environment Management | Python-dotenv |
| Version Control | Git, GitHub |

 📂 Project Structure


```text
JOBPORTAL/
│
├── accounts/
│   ├── migrations/
│   └── ...
│
├── dashboard/
│   ├── migrations/
│   └── ...
│
├── jobs/
│   ├── migrations/
│   ├── templates/
│   └── ...
│
├── jobportal/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
│
├── templates/
├── media/
├── staticfiles/
│
├── manage.py
├── Procfile
├── requirements.txt
├── .gitignore
└── README.md
```


⚙️ Installation and Setup

Follow these steps to run the project locally.

1. Clone the repository


git clone YOUR_GITHUB_REPOSITORY_URL


2. Navigate to the project directory


cd JOBPORTAL


3. Create a virtual environment


python -m venv venv

4. Activate the virtual environment

Windows:

powershell
venv\Scripts\activate


Linux / macOS:


source venv/bin/activate


5. Install dependencies

bash
pip install -r requirements.txt


6. Configure environment variables

Create a `.env` file in the project root directory.


DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost


Never commit your `.env` file or expose your secret key publicly.

7. Apply database migrations


python manage.py makemigrations
python manage.py migrate


8. Create a superuser (Optional)


python manage.py createsuperuser


9. Run the development server


python manage.py runserver


Open your browser and visit:

http://127.0.0.1:8000/


🗄️ Database

The project is configured to use:

- SQLite for local development.
- PostgreSQL for production deployment.

Production database configuration uses environment variables:

env
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=your_database_host
DB_PORT=5432


☁️ Deployment

The project is being prepared for deployment using **AWS Elastic Beanstalk**.

Deployment configuration includes:

- Gunicorn as the WSGI application server.
- WhiteNoise for serving static files.
- Environment-based Django configuration.
- PostgreSQL database support.

Production deployment and persistent resume storage configuration are separate setup steps.

🔐 Security Considerations

- Secret keys and database credentials are managed through environment variables.
- Debug mode should be disabled in production.
- Production hosts and HTTPS settings must be configured before public deployment.
- User-uploaded resumes should be stored using persistent storage in production.

👨‍💻 Author

Jerin Thomas

B.Tech Computer Science and Engineering

LinkedIn: https://www.linkedin.com/in/jerin-thomas-7a695731b/

---

⭐ If you find this project useful, consider giving the repository a star!
