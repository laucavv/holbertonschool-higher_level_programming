#include "lists.h"

/**
 * insert_node - insert a number in a sorted singly list.
 * @head: Header of the list.
 * @number: number to be inserted in the list.
 * Return: list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *tmp, *aux;

	if (head == NULL)
	{
		return (NULL);
	}
	node = malloc(sizeof(listint_t));
	if (node == NULL)
	{
		return (NULL);
	}
	node->n = number;
	if (*head == NULL || (*head)->n >= number) 
	{
		node->next = *head;
		*head = node;
		return (node);
	}
	tmp = *head;

	while (tmp->next != NULL)
	{
		if ((tmp->n < number) && tmp->next->n >= number)
		{
			break;
		}

		tmp = tmp->next;
	}
	aux = tmp->next;
	tmp->next = node;
	node->next = aux;
	return (node);

}

