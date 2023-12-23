from typing import Optional
from pydantic import BaseModel, Field
import uuid

class TaskModel(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias='_id')
    name: str = Field(...)
    completed: bool = False

    class Config:
        allow_population_by_name = True
        schema_extra = {
            "example": {
                "id": "00010203-0405-0607-0809-0a0b0c0d0e0f",
                "name": "Learn FARM stack",
                "completed": False
            }
        }

class UpdateTaskModel(BaseModel):
    name: Optional[str]
    completed: Optional[bool]

    class Config:
        schema_extra = {
            "example": {
                "name": "Learn FARM stack",
                "completed": True
            }
        }