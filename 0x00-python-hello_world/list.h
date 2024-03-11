#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>
#include <stdlib.h>

/**
* struct listint_s - singly linked list
* @n: integer
* @next: points to the next node
*/

typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

int check_cycle(listint_t *list);

#endif
