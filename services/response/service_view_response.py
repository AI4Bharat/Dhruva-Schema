from module.services.model import Model
from .service_response import ServiceResponse

class ServiceViewResponse(ServiceResponse):
    model: Model
    usage: int = 0
