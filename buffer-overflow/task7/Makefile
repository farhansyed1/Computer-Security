.PHONY: all attack clean test

CC=gcc
CFLAGS=-static -O0 -ggdb -fno-stack-protector

all: test

main.elf: main.c
	$(CC) -o $@ $< $(CFLAGS) 

my.fifo:
	[ -p $@ ] || mkfifo $@

attack: main.elf my.fifo
	./solution7.py < my.fifo | ./main.elf 2>my.fifo

test:
	./test.py

clean:
	rm -f main.elf my.fifo
