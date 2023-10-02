#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - the function name
 * @list: the input of the function.
 * Return: the result.
 */

int check_cycle(listint_t *list)
{
	listint_t *add = list, *addd;

	for (addd = list; addd && addd->next;)
	{
		add = add->next;
		addd = addd->next->next;
		if (add == addd)
			return (1);
	}
	return (0);
}
