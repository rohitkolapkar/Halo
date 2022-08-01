from HelloWorld.controllers.view import HelloWorldView
from HelloWorld.controllers.hello_world import HelloWorldDemo
from HelloWorld.controllers.alerts import AlertsView

class HelloWorldRoutes():
    """
    Common class for adding routes
    """

    @staticmethod
    def add_routes(app):
        """
        Add routes to Web application
        """
        app.add_routes(HelloWorldView._app_routes)
