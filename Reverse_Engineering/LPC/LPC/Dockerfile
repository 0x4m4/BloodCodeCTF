FROM ubuntu:22.04@sha256:2b7412e6465c3c7fc5bb21d3e6f1917c167358449fecac8176c6e496e5c1f05f

RUN apt-get update && apt-get install -y socat python3 python3-pip

WORKDIR /app
COPY . ./
COPY ./flag.txt /flag.txt

RUN pip3 install python-chess
RUN chmod +x /app/chess_chall.py

EXPOSE 8000

CMD ["socat", "-T60", "TCP-LISTEN:8000,reuseaddr,fork", "EXEC:python3 /app/chess_chall.py 2>&1"]
