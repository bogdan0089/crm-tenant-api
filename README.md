# CRM Tenant API

![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-async-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-blue)

Async REST API for a multi-tenant CRM system built with FastAPI and PostgreSQL. The system manages two core entities — **Tenant** (company/client) and **Order** (client order) — with a 1:N relationship.

---

## Project Structure

```
crm-tenant-api/
├── app/
│   ├── core/
│   │   ├── config.py
│   │   ├── enums.py
│   │   └── exceptions.py
│   ├── database/
│   │   ├── session.py
│   │   └── unit_of_work.py
│   ├── models/
│   │   ├── model_tenant.py
│   │   └── model_order.py
│   ├── repositories/
│   │   ├── repository_tenant.py
│   │   └── repository_order.py
│   ├── routers/
│   │   ├── router_tenant.py
│   │   └── router_order.py
│   ├── schemas/
│   │   ├── schemas_tenant.py
│   │   └── schemas_order.py
│   └── service/
│       ├── service_tenant.py
│       └── service_order.py
├── alembic/
├── .env.example
├── docker-compose.yml
├── Dockerfile
├── main.py
└── requirements.txt
```

---

## Architecture Overview

The project follows a layered architecture:

```
Router → Service → Repository → Database
```

- **Router** — handles HTTP requests, validates input via Pydantic schemas, returns responses
- **Service** — contains business logic, raises custom exceptions
- **Repository** — handles all database queries via SQLAlchemy ORM
- **Unit of Work** — manages session lifecycle, ensures all operations within a request are committed or rolled back together
- **Database** — PostgreSQL, accessed asynchronously via asyncpg

### Why this architecture?

- Clear separation of concerns — each layer has a single responsibility
- Easy to test each layer independently
- Industry-standard pattern for FastAPI applications
- Unit of Work pattern ensures atomicity — either all operations succeed or none (automatic commit/rollback)

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.13 | Programming language |
| FastAPI | Web framework |
| SQLAlchemy 2.0 (async) | ORM |
| asyncpg | Async PostgreSQL driver |
| Alembic | Database migrations |
| Pydantic v2 | Data validation and serialization |
| pydantic-settings | Environment variables management |
| uvicorn | ASGI server |
| Docker + Docker Compose | Containerization |
| PostgreSQL 17 | Database |

---

## Data Schema

### Tenant

| Field | Type | Description |
|-------|------|-------------|
| id | int | Primary key |
| name | str | Company name |
| email | str | Contact email |
| created_at | datetime | Creation timestamp |
| orders | List[Order] | Related orders |

### Order

| Field | Type | Description |
|-------|------|-------------|
| id | int | Primary key |
| tenant_id | int | Foreign key to Tenant |
| title | str | Order title |
| amount | float | Order amount |
| status | enum | NEW / IN_PROGRESS / DONE / CANCELLED |
| created_at | datetime | Creation timestamp |
| tenant | Tenant | Related tenant |

---

## API Design

### Tenants

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /tenants/ | Create tenant |
| GET | /tenants/ | Get all tenants |
| GET | /tenants/{id} | Get tenant by ID |
| PATCH | /tenants/{id} | Update tenant |
| DELETE | /tenants/{id} | Delete tenant |

**POST /tenants/** — Request body:
```json
{
  "name": "FOP Petrenko",
  "email": "petrenko@gmail.com"
}
```
Response `200`:
```json
{
  "id": 1,
  "name": "FOP Petrenko",
  "email": "petrenko@gmail.com",
  "created_at": "2026-05-07T15:25:47.318229"
}
```

**GET /tenants/** — Query params: `limit=10&offset=0`  
Response `200`: array of tenant objects

**GET /tenants/{id}** — Response `200`: single tenant object, `404` if not found

**PATCH /tenants/{id}** — Request body (all fields optional):
```json
{
  "name": "New Name",
  "email": "new@email.com"
}
```
Response `200`: updated tenant object

**DELETE /tenants/{id}** — Response `204 No Content`

---

### Orders

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /orders/ | Create order |
| GET | /orders/ | Get all orders |
| GET | /orders/{id} | Get order by ID |
| PATCH | /orders/{id} | Update order |
| PATCH | /orders/{id}/status | Update order status |
| DELETE | /orders/{id} | Delete order |

**POST /orders/** — Request body:
```json
{
  "title": "Website development",
  "amount": 5000.0,
  "status": "NEW",
  "tenant_id": 1
}
```
Response `200`:
```json
{
  "id": 1,
  "title": "Website development",
  "amount": 5000.0,
  "status": "NEW",
  "tenant_id": 1,
  "created_at": "2026-05-07T15:30:00.000000"
}
```

**GET /orders/** — Query params: `limit=10&offset=0`  
Response `200`: array of order objects

**GET /orders/{id}** — Response `200`: single order object, `404` if not found

**PATCH /orders/{id}** — Request body (all fields optional):
```json
{
  "title": "Updated title",
  "amount": 7000.0,
  "status": "IN_PROGRESS"
}
```
Response `200`: updated order object

**PATCH /orders/{id}/status** — Request body:
```json
{
  "status": "DONE"
}
```
Response `200`: updated order object

**DELETE /orders/{id}** — Response `204 No Content`

---

## Task Decomposition

1. Project structure setup
2. Database connection (SQLAlchemy async + asyncpg)
3. Unit of Work pattern implementation
4. SQLAlchemy models (Tenant, Order)
5. Alembic migrations
6. Pydantic schemas (Create, Update, Response)
7. Repositories (CRUD operations)
8. Services (business logic + custom exceptions)
9. Routers (HTTP endpoints)
10. Docker + Docker Compose setup
11. Testing via Postman

---

## AI Usage Strategy

AI was used as a code review and debugging tool — to identify bugs, validate implementation decisions, and catch runtime errors during development. All code was written manually.

---

## Running Locally

### Prerequisites

- Python 3.13+
- PostgreSQL
- Virtual environment

### Setup

```bash
git clone https://github.com/bogdan0089/crm-tenant-api.git
cd crm-tenant-api

python -m venv .venv
.venv\Scripts\activate  # Windows

pip install -r requirements.txt
```

### Configure environment

Copy `.env.example` to `.env` and fill in your values:

```
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=crm_tenant
```

### Run migrations

```bash
alembic upgrade head
```

### Start server

```bash
uvicorn main:app --reload
```

API available at: `http://127.0.0.1:8000`  
Swagger docs: `http://127.0.0.1:8000/docs`

---

## Running with Docker

```bash
docker compose up --build
```

Then run migrations in a separate terminal:

```bash
docker compose exec api alembic upgrade head
```

API available at: `http://localhost:8000`  
Swagger docs: `http://localhost:8000/docs`

> Note: When running with Docker, set `DB_HOST=db` in your `.env` file.
