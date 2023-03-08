from enum import Enum

from pydantic import BaseModel


class ApiKeyAction(Enum):
    ACTIVATE = "ACTIVATE"
    REVOKE = "REVOKE"


class SetApiKeyStatusQuery(BaseModel):
    api_key_id: str
    action: ApiKeyAction