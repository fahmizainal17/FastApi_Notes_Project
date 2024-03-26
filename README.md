# FastApi_Notes_Project

Welcome to the **FastApi_Notes_Project**! This project demonstrates the capabilities of FastAPI, a modern, fast (high-performance) web framework for building APIs with Python 3.7+ that's based on standard Python type hints. It provides a simple yet effective example of receiving HTTP request parameters, processing them through Python functions, and returning a JSON response. Specifically, this project showcases an endpoint that combines first and last names to generate a full name.

## Project Structure

- **`.gitignore`**: Helps in ignoring files that should not be tracked by Git.
- **`LICENSE`**: The MIT License document, detailing the permissions for the project's reuse and distribution.
- **`README.md`**: The guide and overview document for the project.
- **`main.py`**: The main application file where FastAPI is instantiated and routes are defined.
- **`requirements.txt`**: A list of project dependencies that need to be installed for the application to run.

## Features

- **Full Name Combination**: Provides an API endpoint to concatenate a first name and a last name into a full name, demonstrating basic data manipulation and API response techniques.
- **Built with FastAPI**: Utilizes FastAPI's capabilities for quick development, performance, and less boilerplate code for API creation.

## Getting Started

### Prerequisites

To run this project locally, you will need:
- Python 3.8 or later.
- pip, the Python package installer.

### Installation

1. **Clone the Project**:
   ```sh
   git clone https://github.com/fahmizainal17/FastApi_Notes_Project.git
   ```
   
2. **Navigate to the Project Directory**:
   ```sh
   cd FastApi_Notes_Project
   ```

3. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

### Running the Application

1. **Launch the FastAPI Server**:
   ```sh
   uvicorn main:app --reload
   ```
   The `--reload` option enables code changes to be picked up live without needing to restart the server.

2. **Access the API Endpoint**:
   Use a web browser or a tool like Postman to send requests to:
   ```
   http://127.0.0.1:8000/full-name/?first_name=John&last_name=Doe
   ```
   You can replace `John` and `Doe` with any names of your choice. The API will respond with a JSON object containing the combined full name.

### FastAPI Application Example Code

Here is the core of the FastAPI application contained within `main.py`:

```python
from fastapi import FastAPI

app = FastAPI()

def get_full_name(first_name: str, last_name: str) -> str:
    """Combines first name and last name into a full name."""
    full_name = first_name.title() + " " + last_name.title()
    return full_name

@app.get("/full-name/")
async def full_name_endpoint(first_name: str, last_name: str):
    """
    An endpoint to obtain a full name by combining the first name and last name.
    """
    full_name = get_full_name(first_name, last_name)
    return {"full_name": full_name}
```

## Contribution

Contributions to improve or enhance the **FastApi_Notes_Project** are highly encouraged. Fork the repository, commit your changes, and open a pull request with a detailed description of your updates or new features.

## License

This project is openly distributed under the MIT License. See the [LICENSE](LICENSE) file for full details.

---

For questions, suggestions, or further information, please contact the project maintainer at `fahmizainals9@gmail.com`. Let's collaborate to make this project a cornerstone for those venturing into the world of FastAPI!
