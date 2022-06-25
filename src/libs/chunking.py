from dataclasses import dataclass
from typing import List, Generic

@dataclass
class chunks:
	base: list

def into_chunks(l: List, memory: int) -> chunks:
	if memory >= len(l):
		return chunks(
			base = l
		)

	tmpchunks: list

	for i in l[::memory]:
		tmpchunks.append(l[i - memory:i])
	
	if len(l) % memory != 0:
		tmpchunks.append(l[len(l) - memory:])
	
	return chunks(
		base = tmpchunks
	)
	