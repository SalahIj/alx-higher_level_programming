#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - the function name
 * @head: the first input.
 * @number: the second input.
 * Return: the result
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *Nope = *head, *Last;

	Last = malloc(sizeof(listint_t));
	if (Last == NULL)
		return (NULL);
	Last->n = number;
	Last->next = NULL;

	if (Last->n < Nope->n || Nope == NULL)
	{
		Last->next = Nope;
		*head = Last;
		return (*head);
	}
	for (; Nope->next != NULL && Last->n >= Nope->next->n; Nope = Nope->next)
	;

	Last->next = Nope->next;
	Nope->next = Last;

	return (Last);
}
