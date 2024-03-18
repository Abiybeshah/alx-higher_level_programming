#include "lists.h"
#include <stddef.h>
/**
* palindrome - utility for palindrome
* @top: pntr to a pointer to a single linked list
* @next: pntr to a singly linked list
*
* Return: integer, 1 if palindrome, else 0
*/
int palindrome(listint_t **l, listint_t *r)
{
	int response;

	if (r != NULL)
	{
		response = palindrome(l, r->next);
		if (response != 0)
		{
			response = (r->n == (*l)->n);
			*l = (*l)->next;
			return (response);
		}
		return (0);

	}
	return (1);
}

/**
* is_palindrome - check if a singly linked list is a palindrome
* @head: linked list double pnter
*
* Return: int, 1 if list is a palindrome else 0
*/
int is_palindrome(listint_t **head)
{
	if (head == NULL)
	{
		return (0);
	}
	return (palindrome(head, *head));
}
