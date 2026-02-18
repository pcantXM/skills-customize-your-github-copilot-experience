"""
FastAPI REST API Assignment - Starter Code
Build a RESTful API for managing a book collection
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional
import uvicorn

# TODO: Create FastAPI app instance


# TODO: Define Pydantic model for Book
# Include fields: id (int), title (str), author (str), year (int), isbn (str)


# TODO: Create an in-memory storage for books (list)
books_db = []


# TODO: Implement root endpoint
# GET / - Return a welcome message


# TODO: Implement health check endpoint
# GET /health - Return API status


# TODO: Implement CRUD endpoints for books
# GET /books - Return all books
# GET /books/{book_id} - Return a specific book
# POST /books - Create a new book
# PUT /books/{book_id} - Update a book
# DELETE /books/{book_id} - Delete a book


# Run the application
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
