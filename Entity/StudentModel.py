from datetime import date
from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field, EmailStr

from Entity.PyObjectId import PyObjectId


class StudentModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    email: EmailStr = Field(...)
    course: str = Field(...)
    average: float = Field(...)
    birthday: Optional[date] = None
    previousJob: Optional[str] = None

    class Config:
        allow_population_by_field_name = True
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
