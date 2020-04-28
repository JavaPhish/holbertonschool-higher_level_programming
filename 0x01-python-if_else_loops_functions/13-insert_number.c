#include<stdio.h>
#include"lists.h"
#include<stdlib.h>

/**
 * insert_node - Inserts a node into a sorted linked list
 * @head: The head of the list to insert into
 * @number: value to be inserted into the list
 *
 * Return: The address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *(head);
	listint_t *temp;

	while (node->next != NULL && node->next->n < number)
		node = node->next;

	temp = node->next;
	node->next = NULL;

	add_nodeint_end(&node, number);

	node = node->next;
	node->next = temp;
	free(temp);

	return node;
}
