from dataclasses import dataclass
from typing import List, Tuple, Union

@dataclass
class chunks:
	base: Union[List[Tuple[int]], Tuple[int, ...]]

def into_chunks(l: List[int], memory: int) -> chunks:
	"""
	Converts a list of integers to a list of chunks (Tuple[int]) by dividing integers in smaller chunks by the memory:

	Example:

	`[1, 2, 3, 4, 5, 6, 7, 8]` → `[(1, 2), (3, 4), (5, 6), (7, 8)]`
	"""
	if memory >= len(l):
		return chunks(
			base = tuple(l)
		)

	tmpchunks: list = []

	for i in l[memory - 1::memory]:
		tmpchunks.append(l[i - memory:i])
	
	if len(l) % memory != 0:
		tmpchunks.append(l[len(l) - memory:])
	
	return chunks(
		base = tmpchunks
	)
