Yacht Charter Project

This project is a web application for searching and reserving yachts. The project is still in progress, with the backend mostly complete and the frontend currently under development.

Project Status:

    Backend: Completed
    Frontend: In progress

Technologies Used:
 - Backend:

    FastAPI: For building the API endpoints.
    SQLAlchemy: For ORM and database interactions.
    PostgreSQL: Database.
    Pydantic: For data validation.
    JWT: For user authentication.

 - Frontend:

    React: For building the user interface.
    Vite: For bundling the frontend assets.
    Tailwind CSS: For styling the application.
    Axios: For making HTTP requests.

Setup Instructions:
 - Prerequisites:

    Python 3.8+
    Node.js
    PostgreSQL

 - Backend Setup:

    Clone the repository

    bash

	git clone https://github.com/yourusername/yacht-charter.git
	cd yacht-charter

 - Create a virtual environment

    bash

	python -m venv venv
	source venv/bin/activate  # On Windows use `venv\Scripts\activate`

 - Install dependencies

    bash

	pip install -r requirements.txt

 - Set up environment variables

   Create a .env file in the root directory with the following content:

 - env

	DATABASE_URL=postgresql://user:password@localhost/yacht_charter
	SECRET_KEY=secret_key

 - Run database migrations

    bash

	alembic upgrade head

 - Start the backend server

    bash

	uvicorn app.main:app --reload

 - Frontend Setup

    Navigate to the frontend directory

    bash

	cd client

 - Install dependencies

    bash

	npm install

 - Start the frontend development server

    bash

    	npm run dev

Accessing the Application

    The backend API will be running at http://localhost:8000
    The frontend application will be running at http://localhost:5174

 - API Documentation

    Swagger UI: http://localhost:8000/docs
    ReDoc: http://localhost:8000/redoc
