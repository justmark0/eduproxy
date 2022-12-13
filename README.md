# What is this
This is proxy for SSD course. It was difficult to make it work with mitmproxy. 

# How to use
`docker-compose up` with jucie-shop on 3000 port.

# How does it work
It is simply reverse proxy. It is listening on 8080 port and redirecting all requests to juice-shop on 3000 port to its container.
But also it can check the rules. For example we can check that in search bar it does not appear work script to make an XSS attack.