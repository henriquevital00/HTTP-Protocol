from controllers.Publication.Endpoints import publicationsEndpoints
from controllers.Users.Endpoints import usersEndpoints

endpoints = {
    "POST": publicationsEndpoints["POST"],

    "GET": publicationsEndpoints["GET"],

    "DELETE": publicationsEndpoints["DELETE"]

}