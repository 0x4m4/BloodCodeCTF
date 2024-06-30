FROM theflash2k/pwn-chal:2204
ENV CHAL_NAME=babyrop
COPY ${CHAL_NAME} .
COPY flag.txt /flag
EXPOSE 8000
# # For setting up the dynamic flagging.
# COPY docker-entrypoint.sh /tmp/docker-entrypoint.sh
# RUN chmod +x /tmp/docker-entrypoint.sh
# ENTRYPOINT [ "/tmp/docker-entrypoint.sh" ]