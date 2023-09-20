from pydantic import BaseModel

class ImageData(BaseModel):
    imageData: str  # This should match the name of the parameter in the POST request
