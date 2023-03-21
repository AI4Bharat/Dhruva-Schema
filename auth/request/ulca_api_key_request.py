import re

from pydantic import BaseModel, EmailStr, validator


class ULCAApiKeyRequest(BaseModel):
    emailId: EmailStr
    appName: str

    @validator("appName")
    def check_api_key_name_format(cls, v):
        name_regex = r"^[a-z0-9\.\-@_]+$"
        if not re.search(name_regex, v):
            raise ValueError("Name has invalid characters")
        return v
