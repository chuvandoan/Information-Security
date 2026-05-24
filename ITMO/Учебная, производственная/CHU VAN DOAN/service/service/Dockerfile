FROM ubuntu:latest

RUN apt-get update && apt-get install -y socat
RUN useradd -r -m -d /home/user -s /usr/sbin/nologin user

RUN mkdir /home/user/notes && \
    chown -R root:user /home/user/notes && \
    chmod 770 /home/user/notes

RUN mkdir /home/user/users && \
    chown -R root:user /home/user/users && \
    chmod 770 /home/user/users

RUN mkdir /app && \
    chown -R root:root /app && \
    chmod 755 /app

COPY app/entrypoint.sh app/service.sh /app/

WORKDIR /home/user/

COPY app/entrypoint.sh app/service.sh /app/

RUN chmod 750 /app/service.sh /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
