📅 Day 26 – Building REST APIs with FastAPI

🗒️ Topics Covered  
🔹 REST API Basics – GET, POST, PUT, DELETE methods  
🔹 FastAPI – A modern web framework for building APIs with Python  
🔹 Endpoint Creation – Define API routes for CRUD operations  
🔹 Pydantic Models – Used for request and response validation

🎯 Challenge  
🔧 Build a RESTful API to manage a **library of books** using FastAPI.  
The API should support the following endpoints:  
- `GET /books` → Retrieve all books  
- `GET /books/{id}` → Retrieve a book by ID  
- `POST /books` → Add a new book  
- `PUT /books/{id}` → Update an existing book  
- `DELETE /books/{id}` → Remove a book  

💻 Solution  
Check the `Day26_main.py` file in this folder.  
Run the API using:  
```bash
uvicorn Day26_main:app --reload
