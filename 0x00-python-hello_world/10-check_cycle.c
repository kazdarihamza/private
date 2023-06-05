#include "lists.h"
/**
 *check_cycle - a fucntion check if a list has a cycle  or not
 *@list: the signly likned list
 *Return: either 1 for the existence of a likned list or 0 if there is none
 */
int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *second = list;

	while (second != NULL && second->next != NULL)
	{
		first = first->next;
		second = second->next->next;
		if (first == second)
			return (1);
	}
	return (0);
}