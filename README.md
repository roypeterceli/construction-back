<p align="center">
<img src="https://wowperu.pe/_astro/internet-hogar-wow-peru.lf6fogPl.svg" width="auto" height="50">
</p>

## Acerca de

Wow Perú es una empresa proveedora de internet, telefonia IP y Cable que utiliza una red de Fibra Óptica. En Materia Gris tuvimos el encargo de implementar el sistema de gestión de clientes e instalación de servicios.

## Sobre el proyecto

Este proyecto cubre la necesidad de un sistema de gestión de bd para construcción de instalaciones: [wow-construccion-backend]
(https://gitlab.com/wow-construccion/backend.construccion.wowperu.pe)

## Encargados del Proyecto
- Diego Alvarado

### Gestión de Proyecto
- Cesar Vallejo

### Desarrollo y Base de datos
- Roy Celino 

## Prerequisites

Ensure you have the following tools installed on your system before proceeding:

- **Python**: Version 3.13 or higher.
- **UV**: Universal package manager for Python.

## Development Environment Setup

### 1. Setup package manager
```bash
pip install uv
```
### 2. Activate the Virtual Environment

- On **Windows**:
  ```bash
  .venv\Scripts\activate
  ```
- On **macOS/Linux**:
  ```bash
  source .venv/bin/activate
  ```

### 3. Install Dependencies

To install the dependencies, simply run:

```bash
uv sync
```
## Running the Project

### Development Mode

Before starting the server, ensure that you have created a `.env` file in the root directory. This file should contain
the necessary environment variables for database connections and application configuration.

To start the server in development mode, run:

```bash
fastapi dev app/main.py --port 9009
```
or
```bash
uvicorn app.main:app --port 9009 --reload
```

This will start the server at `http://localhost:9000` with automatic code reload.


## Project Structure

The basic structure of the project is as follows:

```
Microservice/
├── app/
│   ├── main.py         # Application entry point
│   ├── config/         # Configuration files
│   ├── routers/        # API route definitions
│   ├── services/       # Business logic
│   ├── repositories/   # Database interaction layer
│   ├── models/         # SQLAlchemy models
│   ├── schemas/        # DTO object models
│   ├── clients/        # HTTP clients for external services
│   ├── exceptions/     # Exception handlers
│   ├── utils/          # Utility functions
│   └── ...
├── migrations/         # Alembic migration folder
├── pyproject.toml      # Project info and dependencies
├── uv.lock             # UV lock file
├── Dockerfile          # Docker configuration
├── README.md           # Project documentation
├── .gitignore          # Git ignore file
├── .env                # Environment variables (excluded from repository)
└── .venv/              # Virtual environment (excluded from repository)
```


## Key Features

- **FastAPI**: A lightweight and high-performance framework with OpenAPI support.
- **SQLAlchemy**: A powerful ORM for database interactions.
- **Modular Design**: Clear structure for easy maintenance and scalability.
- **Automatic Reload**: Ideal for rapid and uninterrupted development.
- **UV Package Manager**: Modern dependency management for efficiency and reliability.

## License

This software is proprietary and intended for internal use only. All rights reserved
by [WOW TEL S.A.C](https://wowperu.pe/).

![WOW Logo](https://wowperu.pe/_astro/internet-hogar-wow-peru.lf6fogPl.svg)
