from HelloWorld.controllers.view import HaloView
from HelloWorld.controllers.hello_world import HelloWorldView
from HelloWorld.controllers.buckets import BucketsView
from HelloWorld.controllers.iam_users import IAMUsersView

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
