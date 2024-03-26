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
