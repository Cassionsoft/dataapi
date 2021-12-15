from typing import List,Optional
from pydantic import BaseModel, Field, EmailStr

from models.question import Question

class Form(BaseModel):
    name :str = Field(None, title="name of the form")
    url_out :str = Field(None, title="url_out: Url to forward the form")
    questions :Optional[List[Question]] = Field(None, title="questions: list of questions")
    format_out :str = Field(None, title="The format of the output data to url_out")
    format_in :Optional[str] = Field(None, title="The format of the input data to the form")