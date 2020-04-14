import time
from prometheus_client.core import GaugeMetricFamily, REGISTRY, CounterMetricFamily
from prometheus_client import start_http_server


class CustomCollector(object):
    def __init__(self):
        pass

    def collect(self):
        g = GaugeMetricFamily('jira_epic_process_status', 'This is the status of the epic', labels=["Epic_Id","Dial_V"])
        g.add_metric(["Dops-17","DIAL-2"],1)
        yield g

if __name__ == '__main__':
    start_http_server(8000)
    REGISTRY.register(CustomCollector())
    while True:
        time.sleep(1)
