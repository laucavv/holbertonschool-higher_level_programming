#include "lists.h"
/**
 *check_cycle - verify if there is a cycle in the list
 *@list: head
 * Return:0 is no cycle, 1 is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *actual, *aux;

	actual = list;
	aux = list;

	while (actual != NULL && aux != NULL && aux->next != NULL)
	{
		actual = actual->next;
		aux = aux->next->next;
		if (actual == aux)
			return (1);
	}
	return (0);
}
