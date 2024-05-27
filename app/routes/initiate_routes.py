from . import logs_route


class InitiateRouters:
    def __init__(self, app):
        app.include_router(logs_route.router)

