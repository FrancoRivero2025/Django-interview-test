# Django Interview Test

## Requirements

- Docker and Docker Compose installed  
  [Docker Desktop (Windows and Ubuntu)](https://www.docker.com/products/docker-desktop)  
  [Official Documentation](https://docs.docker.com/desktop/)

---

## 1. Check if port 80 is in use

Debian / Linux:
```bash
netstat -tulpn | grep 80
```

---

## 2. Start the application

```bash
docker-compose build
docker-compose up
docker-compose ps
```

You should see something like:

```
    Name                  Command               State                    Ports                  
------------------------------------------------------------------------------------------------
test_nginx_1   /docker-entrypoint.sh ngin ...   Up      0.0.0.0:80->80/tcp,:::80->80/tcp        
test_web_1     python manage.py runserver ...   Up      0.0.0.0:8000->8000/tcp,:::8000->8000/tcp
```

---

## 3. Run migrations

```bash
docker exec test_web_1 python manage.py makemigrations techfix
docker exec test_web_1 python manage.py migrate
```

---

## 4. Load sample data

```bash
docker exec test_web_1 python manage.py loaddata techfix/fixtures/user.json --app techfix.user
docker exec test_web_1 python manage.py loaddata techfix/fixtures/company.json --app techfix.company
docker exec test_web_1 python manage.py loaddata techfix/fixtures/scheme.json --app techfix.scheme
docker exec test_web_1 python manage.py loaddata techfix/fixtures/pedido.json --app techfix.pedido
```

Create a superuser:
```bash
docker exec -it test_web_1 python manage.py createsuperuser
```

---

## 5. Run tests

```bash
docker exec -it test_web_1 python manage.py test
```

---

## Task Description

**TechFix Solutions** needs to log the hours worked by technicians to process payments. The task includes:

### 1. Database (optional)

The default database is SQLite. Optionally, connect a PostgreSQL instance running in a Docker container to Django.

### 2. Technician Model

Create a model for technicians and populate it with at least 5 entries.

### 3. Django Admin

Register all models in the admin panel.

### 4. Command to generate work orders

Implement a command to generate `N` work orders (where N is between 1 and 100).  
Each order should:

- Randomly assign a technician and a client.
- Assign worked hours between 1 and 10.

### 5. Technicians API Endpoint

Create an endpoint that returns all technicians with the following info:

- Full name  
- Hours worked  
- Total payment  
- Number of work orders handled  

Payment calculation:

| Hours Worked | Hourly Rate | Discount |
|--------------|-------------|----------|
| 0–14         | 200         | 15%      |
| 15–28        | 250         | 16%      |
| 29–47        | 300         | 17%      |
| >48          | 350         | 18%      |

Example:
```
Daniel Larusso, 20 hours worked:
(20 * 250) – (20 * 250 * 0.16) = 5000 – 800 = 4200
```

This list should support **filtering by partial name**.

### 6. Report API Endpoint

Create an endpoint that returns:

- Average payment for all technicians
- Technicians who earned less than average
- Most recently added technician with the lowest payment
- Most recently added technician with the highest payment

### 7. Update Endpoint (optional)

Create an endpoint to **only update work orders**.

### 8. Tests

Write tests for all new endpoints.

---