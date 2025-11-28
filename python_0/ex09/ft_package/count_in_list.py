def count_in_list(liste, element) -> int:
	"""count_in_list(liste, element) -> int

Count occurrences of element in liste.

Args:
    liste: A list to search in
    element: The element to count

Returns:
    The number of occurrences"""

	count = 0
	for each in liste:
		count += each == element
	return count