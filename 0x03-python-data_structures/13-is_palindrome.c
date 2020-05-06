#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: first element of a linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	int palindro[3056];
	int i = 0, j;

	if (head == NULL || *head == NULL)
		return (1);

	while (tmp)
	{
		palindro[i] = tmp->n;
		i++;
		tmp = tmp->next;
	}
	i--;
	for (j = 0; j <= i ; i--, j++)
	{
		if (palindro[i] != palindro[j])
			return (0);
	}
	return (1);
}
