Title: cgo: Go lang with C
Date: 2015-11-19 00:00
Tags: c, tlpi, glibc, memory
Author: José Guilherme Vanz

Some time ago I bought the The Linux Programming Interface, one of the best books I have bought.
One of the first chapters I read were about memory allocation. At the end of the chapter author offers some exercises to the reader.
Among them there is one more challenged. Implement the equivalent to the malloc and free functions. The challenge has been accepted!

First of all, this implementation has only study purposes. It is mean you SHOULD not start to implement your malloc and free functions.
Do not reinvent the wheel! The glibc are being improved for decades for many great guys. ;)

Theory
------

Before show the code, I will explain how and what I use to create my own memory allocator. For this, I assume that you have a background of how a process works
and its data, text, heap, stack segments. If you do not have this acknowledgement, I will give some references in the end of this post.

### System calls

There are two system calls allows the program to increase the program break, `brk` and `sbrk`. The program break defines where is the end of process's data segment. It means if the program
increases the program break, memory is allocated. Otherwise, it is deallocating memory.  In my code I used only `sbrk`, this function has one parameter the amount of memory the program wants to
increase. If the program break has being increased successfully, a pointer to the beginning of the allocated memory is returned. Otherwise, (void*) -1 is returned. In my code I do not use `brk`, I did
not feel need to used it. `brk` allows the program set the end of data segment to the pointer passed in the functions arguments. I think I do use this functions because my code do not decrease the
program break. Maybe in the future I implement this feature and use the `brk` system call.

### Memory management

A linked list is used to handle which memory block are free and which is allocated, let's call the list `free_list`. Each element in `free_list` is a memory block available to be allocated, it is
composed of a header and the available memory itself. The header contains two fields, the  memory block's size and a pointer to the next element in the list. Therefore, when a mount of memory
is requested a search in the list is performed looking for a memory block with enough size to attempt the request. The algorithm follows the 'First fit' approach. Thus, the first memory block found
with enough size is slitted, if necessary, and returned to the caller. If any block has enough size, the heap is increased and the new memory is returned.

- free algorithm
- free list
- avoid memory fragmentation

Code
----

TODO
memory.c
sample program

References
----------

[brk, sbrk](http://linux.die.net/man/2/sbrk)
- The Linux Programing Interface
- man pages
- some good link about process memory layout