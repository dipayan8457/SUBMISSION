from pydantic import BaseModel

class User(BaseModel):
    user_id: int
    username: str
    email: str
    # Add more user-related fields as needed
