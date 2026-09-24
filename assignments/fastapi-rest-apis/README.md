# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI and learn how routes, request data, response models, and HTTP status codes work together.

## 📝 Tasks

### 🛠️ Create GET Endpoints

#### Description

Complete the starter project so clients can retrieve the sample books in the collection. Run the API with Uvicorn and use the automatically generated documentation at `/docs` to try each route.

#### Requirements
Completed program should:

- Create a `GET /books` endpoint that returns all books
- Create a `GET /books/{book_id}` endpoint that returns one book by ID
- Return a clear `404` response when a requested book does not exist
- Start successfully with `uvicorn starter-code:app --reload`


### 🛠️ Add Create and Update Operations

#### Description

Add endpoints that allow API clients to create a new book and update an existing book. Use Pydantic models to validate incoming JSON data.

#### Requirements
Completed program should:

- Define a request model requiring a book `title`, `author`, and `year`
- Create a `POST /books` endpoint that adds a book and returns its assigned ID
- Return a `201 Created` status code when a book is added successfully
- Create a `PUT /books/{book_id}` endpoint that replaces an existing book's details
- Return a `404` response when an update targets a missing book


### 🛠️ Delete Books and Test the API

#### Description

Finish the CRUD API by adding deletion and a small set of automated tests. Test both successful requests and common error cases.

#### Requirements
Completed program should:

- Create a `DELETE /books/{book_id}` endpoint
- Return a success response when a book is deleted
- Return a `404` response when a deletion targets a missing book
- Add tests for listing books, creating a book, and handling a missing book
- Keep the API data consistent after create, update, and delete requests
