FROM theflash2k/pwn-chal:py38

ENV CHAL_NAME=freeme.py
COPY . .
COPY flag.txt /flag.txt
RUN chmod +rx ${CHAL_NAME}