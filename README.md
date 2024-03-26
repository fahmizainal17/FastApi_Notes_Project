# FastApi
Certainly! Here's an expanded example that integrates your function into a FastAPI application, allowing you to use it in a more practical, API-driven context. This will provide a simple but comprehensive example to practice with FastAPI.

The following code snippet demonstrates how to set up a FastAPI application that includes an endpoint to receive a first name and last name via HTTP GET request parameters, uses your `get_full_name` function to combine them into a full name, and then returns the full name in the response.

### FastAPI Application Code

```python
from fastapi import FastAPI

app = FastAPI()

def get_full_name(first_name: str, last_name: str) -> str:
    """Combine first name and last name into a full name."""
    full_name = first_name.title() + " " + last_name.title()
    return full_name

@app.get("/full-name/")
async def full_name_endpoint(first_name: str, last_name: str):
    """
    Endpoint to get a full name by combining first name and last name.
    """
    full_name = get_full_name(first_name, last_name)
    return {"full_name": full_name}
```

### How to Run the Application

1. **Install FastAPI and Uvicorn**: If you haven't already, make sure you have FastAPI and Uvicorn installed. Uvicorn will serve as the ASGI server to run your FastAPI app. You can install both using pip:
   ```bash
   pip install fastapi uvicorn
   ```

2. **Save the Code**: Save the code snippet above in a Python file, for example, `main.py`.

3. **Run the Application**: In the terminal, navigate to the directory where your `main.py` file is located and run the following command:
   ```bash
   uvicorn main:app --reload
   ```
   The `--reload` flag enables auto-reload so the server will restart after code changes. This is very useful during development.

4. **Test the Application**: Once the application is running, open a web browser and navigate to `http://127.0.0.1:8000/full-name/?first_name=John&last_name=Doe`. Replace `John` and `Doe` with any first name and last name you want to combine. You should see a JSON response like this:
   ```json
   {
       "full_name": "John Doe"
   }
   ```

This simple application demonstrates how you can use FastAPI to create web APIs with Python functions. It's a practical example of how to receive query parameters, process them in your Python code, and return a JSON response. Feel free to expand upon this example with more complex logic, additional endpoints, or by integrating other FastAPI features!
