
# Getting Started

## 1. SSH into the pod using Lens

- **Create Migration Scripts:**

  ```bash
  flask db migrate
  ```
  Ensure that your models and database configuration are set up correctly.

## 2. Access the Application

Once the Docker containers are up and running, you can access your Flask application at [http://localhost:5000](http://localhost:5000).

# Customization

- **Migration Scripts:** Place your migration scripts in the `migrations` directory. These scripts will be executed during the Docker build process.

- **Dependencies:** Update `requirements.txt` with your project dependencies.

- **Application Configuration:** Modify `config.py` and `app.py` to configure your Flask application as per your requirements.

# Notes

- Ensure that your Flask application is configured to use the correct database URI.
