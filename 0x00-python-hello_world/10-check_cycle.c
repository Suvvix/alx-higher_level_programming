#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checl if list cycleical
 * @list: pointer to list
 * Return: 1 if cycleical, 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return(1);
	}
	return (0);
}
