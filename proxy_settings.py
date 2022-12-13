from mitmproxy import proxy, options
from mitmproxy.tools.dump import DumpMaster
from mitmproxy.addons import core
from mitmproxy.http import HTTPFlow
import datetime


class Addon:

    def __init__(self):
        pass

    def response(self, flow: HTTPFlow):
        print(datetime.datetime.now(), flow.request.pretty_url)
        with open("response.txt", "a") as f:
            f.write(str(datetime.datetime.now()) + " " + flow.request.pretty_url + "\n")

        # Block XSS in review of product
        if 'script' in flow.request.pretty_url or \
                flow.request.pretty_url.split('?') == "/search":
            flow.response.set_text('f@ck u hacker')


addons = [
    Addon()
]
