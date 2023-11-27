#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: pointer to head of list.
 * Return: 0 if no cycle, 1 if there is cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *count1 = NULL;
	listint_t *count2 = NULL;

	if (list == NULL)
		return (0);
	count1 = list;
	count2 = list;

	while (count1 && count2 && count2->next)
	{
		count1 = count1->next;
		count2 = count2->next->next;

		if (count1 == count2)
			return (1);
	}
	return (0);
}
