# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build a RESTful API using FastAPI framework, including defining endpoints, handling HTTP methods, data validation with Pydantic models, and testing API responses.

## 📝 Tasks

### 🛠️	Create Basic API Structure

#### Description
Set up a FastAPI application with basic configuration and create simple GET endpoints to return data.

#### Requirements
Completed program should:

- Install and import FastAPI and uvicorn packages
- Create a FastAPI application instance
- Implement a root endpoint (`/`) that returns a welcome message
- Implement a `/health` endpoint that returns the API status
- Run the application using uvicorn on port 8000


### 🛠️	Build CRUD Endpoints for Books

#### Description
Create a complete set of CRUD (Create, Read, Update, Delete) endpoints for managing a collection of books.

#### Requirements
Completed program should:

- Define a Pydantic model for a Book with fields: id, title, author, year, and isbn
- Implement GET `/books` to retrieve all books
- Implement GET `/books/{book_id}` to retrieve a specific book by ID
- Implement POST `/books` to add a new book to the collection
- Implement PUT `/books/{book_id}` to update an existing book
- Implement DELETE `/books/{book_id}` to remove a book from the collection


### 🛠️	Add Data Validation and Error Handling

#### Description
Enhance your API with proper input validation, error handling, and appropriate HTTP status codes.

#### Requirements
Completed program should:

- Use Pydantic models to validate request data automatically
- Return appropriate HTTP status codes (200, 201, 404, 422, etc.)
- Handle cases where a book ID is not found with a 404 error
- Validate that the year is between 1000 and current year
- Ensure ISBN is a valid format (13 digits)
