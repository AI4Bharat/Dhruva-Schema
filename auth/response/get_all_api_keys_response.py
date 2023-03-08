from typing import List, Optional
from bson import ObjectId
from pydantic import BaseModel
from db.MongoBaseModel import ObjectIdField
from schema.auth.common import RoleType


class _ServiceUsage(BaseModel):
    service_id: str
    usage: int

class _ApiKey(BaseModel):
    # TODO: Add this field back once _id is correctly loaded in ApiKey model
    id: ObjectIdField  # str
    name: str
    masked_key: str
    active: bool
    type: str
    created_on: str
    usage: int = 0
    services: Optional[List[_ServiceUsage]]
    role_type: Optional[RoleType]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectIdField: str, RoleType: str}


class GetAllApiKeysResponse(BaseModel):
    api_keys: List[_ApiKey]
    total_usage: int = 0
    page: Optional[int]
    limit: Optional[int]
    total_pages: int
