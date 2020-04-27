#include "lists.h"

/**
 * check_cycle - Detect a loped linked list
 * @list: list head
 * Return: 0 false, 1 true
 */
int check_cycle(listint_t *list)
{
	listint_t *actual, *aux;

	actual = list;
	check = list;

	while (actual != NULL && aux != NULL && aux->next != NULL)
	{
		actual = actual->next;
		aux = aux->next->next;
		if (actual == aux)
			return (1);
	}

	return (0);
}
