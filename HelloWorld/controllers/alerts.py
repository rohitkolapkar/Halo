from HelloWorld.controllers.view import HelloWorldView


@HelloWorldView._app_routes.view('/api/halo/alerts')
class AlertsView(HelloWorldView):
    def __init__(self, request):
        super(HelloWorldView, self).__init__(request)
        pass

    async def get(self):
        list_response = list()
        response = {
            "time": "1589956569",
            "alert_uuid": "15899565680a19bcfadbff47a483bc653fa5cca1d2",
            "description": "Seagate Storage Platform Library - Sensor Response",
            "severity": "critical",
            "state": "fault",
            "acknowledged": False,
            "resolved": False,
            "hostname": "ssc-vm-g4-rhev4-0392.colo.seagate.com"
        }
        list_response.append(response)
        return {"alerts":list_response}
