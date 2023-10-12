#include "lists.h"

/**
 * print_dlistint - The name of the function.
 * @h: The input of the function.
 * Return: The result
 */

size_t print_dlistint(const dlistint_t *h)
{
	const dlistint_t *node;
	size_t i = 0;

	for (node = h; node; node = node->next)
	{
		printf("%d\n", node->n);
		i++;
	}
	return (i);
}
