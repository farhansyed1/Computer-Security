FROM ubuntu:24.04

RUN apt-get update\
 && apt-get install -y nasm gcc expect build-essential make python3 python3-pycryptodome gdb git radare2

WORKDIR /root
CMD ["bash"]
