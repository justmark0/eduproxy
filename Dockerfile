FROM ubuntu:latest
RUN apt update
WORKDIR /app
COPY . .
RUN apt-get install mitmproxy python3 --yes
RUN python3 get-pip.py
RUN pip3 install requests
CMD ["sh", "-c", "mitmdump --set block_global=false --mode reverse:http://epic_elgamal:3000/ -s /app/proxy_settings.py"]
