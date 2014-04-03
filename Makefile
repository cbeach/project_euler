
CC=gcc
CFLAGS=-std=c99 -lm

all: problem_13

problem_13: problem_13.c
	$(CC) -o problem_13.e problem_13.c $(CFLAGS)
