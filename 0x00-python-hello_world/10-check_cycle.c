#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - Seeks a cycle within a singly linked list
 * @list: The linked list to search through
 *
 * Return: 1 if true, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *tail_t = list;
	listint_t *head = list;

	while (head->next != NULL && tail_t->next != NULL)
	{

		head = head->next;
		if (head == NULL)
			return (0);
		head = head->next;
		if (head == NULL)
			return (0);
		tail_t = tail_t->next;

		if (head == tail_t)
		return (1);
	}

	return (0);
}
