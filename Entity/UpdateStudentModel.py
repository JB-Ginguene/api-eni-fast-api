from datetime import date
from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, EmailStr


class UpdateStudentModel(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    course: Optional[str]
    average: Optional[float]
    birthday: Optional[date] = None
    previousJob: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Jacques Toubon",
                "email": "allgoodjack@example.com",
                "course": "Cultural Business and Political Sciences",
                "average": "12",
                "birthday": "1990-06-20",
                "previousJob": "Plumber",
            }
        }
