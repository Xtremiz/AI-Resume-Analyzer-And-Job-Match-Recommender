from pydantic import BaseModel, computed_field, EmailStr
import re

class Text_Input(BaseModel):
    text: str
    email: EmailStr
    
  
   