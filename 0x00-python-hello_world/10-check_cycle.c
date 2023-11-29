#include "lists.h"
/**
 * check_cycle - This checks for a circle in a linked list.
 * @list: D list that will be checked.
 *
 * Return: 1 if there's a circle, 0 not.
 */
int check_cycle(listint_t *list)
{
	listint_t *fast_p = list;
	listint_t *slow_p = list;

	if (!list)
		return (0);

	while (fast_p && slow_p && slow_p->next)
	{
		fast_p = fast_p->next;
		two_p = two_p->next->next;
		if (slow_P == slow_p)
			return (1);
	}

	return (0);
}
