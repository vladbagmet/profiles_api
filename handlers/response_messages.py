from enum import Enum


class MessageType(Enum):
    validation_error = "validation error"
    request_error = "request error"
    service_health = "service is up and running"
    not_allowed = "method not allowed"
    not_found = "url not found"
    server_error = "server error"
    handle_processed = "profile picture url retrieval was requested"
    data_retrieved = "profile data successfully retrieved"
    profile_not_found = "profile not found"
