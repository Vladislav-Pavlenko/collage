from pydantic import BaseModel, Field, field_validator

class TaskModel(BaseModel):
    title: str = Field(..., min_length=1)
    folder: str = Field("All")
    description: str = Field(..., min_length=1)
    is_complete: bool = Field(False)

    @field_validator('folder')
    def check_folder(cls, v):
        if len(v) < 1:
            return "All"
        return v

class UpdateTaskModel(BaseModel):
    title: str = Field()
    folder: str = Field("All")
    description: str = Field()
    is_complete: bool = Field(False)

    @field_validator('folder')
    def check_folder(cls, v):
        if len(v) < 1:
            return "All"
        return v
