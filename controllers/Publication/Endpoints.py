from controllers.Publication.PublicationController import PublicationController


publicationsEndpoints = {

    "POST": {
        "/publications/create": lambda data : (
            PublicationController().create(data)
        )
    },

    "GET": {
        "/publications": lambda id : (
            PublicationController().findById(id)
        ),
        "/publications/all": lambda : (
            PublicationController().findAll()
        )
    }
}