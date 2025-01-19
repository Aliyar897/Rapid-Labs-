
### 1. Clone the Repository

Clone the project from GitHub using the following command:

```bash
git clone https://github.com/Aliyar897/Rapid-Labs-.git
```

### 2. Navigate to the Project Directory

Once the repository is cloned, navigate to the project directory:

```bash
cd Rapid-Labs-
```

### 3. Docker Desktop Installation

Make sure that Docker Desktop is installed on your system. If it's not already installed, you can download and install it from [Docker's official website](https://www.docker.com/products/docker-desktop).

### 4. Start the Project Using Docker

To start the project in detached mode, use the following command to bring up the Docker containers:

```bash
docker-compose up -d
```

This will build and run the Docker containers in the background.

### 5. Create Superusers for User, Admin, and Manager

After the containers are up and running, you need to create superusers for different roles (User, Admin, and Manager). To do this, run the following command:

```bash
docker-compose exec web python manage.py createsuperuser
```

You will be prompted to enter a username, email, and password for the superuser. Repeat this step for creating multiple superusers as needed.

### 6. Testing the API

Once the project is up and running, you can use the Postman collection to test the APIs. Make sure you have the Postman collection file ready and import it into your Postman.

You can use the provided API endpoints to perform actions and validate the functionality.
--> task collection rapidlab.postman_collection.json
""

---

### Additional Information

- The project uses Docker for containerization, which ensures that all dependencies and services are correctly isolated.
- Ensure Docker Desktop is running before attempting to start the containers.
- All database migrations will be handled automatically when you run `docker-compose up`.

---
