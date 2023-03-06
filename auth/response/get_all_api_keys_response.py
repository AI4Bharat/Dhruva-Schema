from typing import List, Optional

from pydantic import BaseModel


class _ServiceUsage(BaseModel):
    service_id: str
    usage: int

class _ApiKey(BaseModel):
    # TODO: Add this field back once _id is correctly loaded in ApiKey model
    # id: str
    name: Optional[str]
    masked_key: Optional[str]
    active: Optional[bool]
    type: Optional[str]
    # created_on: str
    # created_by: str
    usage: Optional[int]
    services: Optional[List[_ServiceUsage]]


class GetAllApiKeysResponse(BaseModel):
    api_keys: List[_ApiKey]
    total_usage: int
    page: Optional[int]
    limit: Optional[int]
    total_pages: int
