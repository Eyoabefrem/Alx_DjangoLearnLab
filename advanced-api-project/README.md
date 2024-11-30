# Advanced API Project: Book Views

## Overview
This project demonstrates how to configure CRUD operations for a Book model using Django REST Framework’s generic views. It also includes advanced query capabilities for filtering, searching, and ordering data.

---

## Endpoints

| Method   | Endpoint                     | Description                    | Permission       |
|----------|------------------------------|--------------------------------|------------------|
| GET      | `/books/`                    | List all books                 | Public           |
| GET      | `/books/<int:pk>/`           | Retrieve a book by ID          | Public           |
| POST     | `/books/create/`             | Add a new book                 | Authenticated    |
| PUT      | `/books/<int:pk>/update/`    | Update an existing book        | Authenticated    |
| DELETE   | `/books/<int:pk>/delete/`    | Delete a book                  | Authenticated    |

---

## Custom Features

### Validation
- Ensures that books cannot have a publication date in the future.

### Permissions
- Authenticated users can perform write operations (POST, PUT, DELETE).
- Unauthenticated users have read-only access (GET).

### Nested URLs
- Each view is mapped to a unique endpoint for clarity and organization.

---

## Testing

### Testing Endpoints
- Use tools like **Postman**, **curl**, or **httpie** to manually test API endpoints.
- Ensure that permissions and validations work as expected for both authenticated and unauthenticated users.

---

## Advanced Query Capabilities

### Features
1. **Filtering**
   - Filter books by attributes like title or author.
   - Example: `/books/?title=Django&author__name=John`

2. **Searching**
   - Search for books by text in specific fields (e.g., title, author).
   - Example: `/books/?search=Python`

3. **Ordering**
   - Order books by any field, such as title or publication year.
   - Ascending example: `/books/?ordering=title`
   - Descending example: `/books/?ordering=-publication_year`

### Sample Requests
- **Filter by title:**  
  `GET /books/?title=Learning REST`
  
- **Search for books containing 'Django':**  
  `GET /books/?search=Django`

- **Order by publication year (descending):**  
  `GET /books/?ordering=-publication_year`

---

## Testing the API

### How to Run Tests
1. Ensure your virtual environment is activated.
2. Run the following command to execute the test suite:
   ```bash
   python manage.py test api
