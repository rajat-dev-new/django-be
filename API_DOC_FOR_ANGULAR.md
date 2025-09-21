# Django REST API Endpoints for Angular Integration

Use these endpoints in your Angular app to send and retrieve form data.

## API Base URL
```
http://localhost:8000/api/form/
```

---

## POST: Submit Form Data
- **URL:** `http://localhost:8000/api/form/`
- **Method:** POST
- **Content-Type:** application/json
- **Payload Example:**
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "message": "Hello!"
}
```
- **Response Example:**
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "message": "Hello!"
}
```

---

## GET: Retrieve All Submissions
- **URL:** `http://localhost:8000/api/form/`
- **Method:** GET
- **Response Example:**
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "message": "Hello!"
  },
  {
    "id": 2,
    "name": "Jane Smith",
    "email": "jane@example.com",
    "message": "Hi!"
  }
]
```

---

## Notes
- All keys (`name`, `email`, `message`) must be sent in the POST request.
- The GET response includes all submissions with their `id`.
- Adjust your Angular service to use these URLs and keys for backend communication.
