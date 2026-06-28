from pydantic import BaseModel
class BaseURL(BaseModel):
    original_url: str
class URLResponse(BaseURL):
    short_url: str
    class Config:
        from_attributes = True