from halo.controllers.view import HaloView

class HaloRoutes():
    """
    Common class for adding routes
    """

    @staticmethod
    def add_routes(app):
        """
        Add routes to Web application
        """
        app.add_routes(HaloView._app_routes)
