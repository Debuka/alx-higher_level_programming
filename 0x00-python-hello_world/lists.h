#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - The singly linked list to be implemented.
 * @n: An int value.
 * @next: pointer which points to next node.
 *
 * Description: A singly linked list's structure.
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

int check_cycle(listint_t *list);

#endif /* LISTS_H */
