#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * Au_pal - the function name
 * @A: the first input
 * @B: the second input
 * Return: the result
 */
int Au_pal(listint_t **A, listint_t *B)
{
	if (!B)
		return (1);
	if (Au_pal(A, B->next) && (*A)->n == B->n)
	{
		*A = (*A)->next;
		return (1);
	}
	return (0);
}

/**
 * is_palindrome - the function name
 * @head: the input
 * Return: the result
 */
int is_palindrome(listint_t **head)
{
	if (!head || !(*head))
		return (1);
	return (Au_pal(head, *head));
}
