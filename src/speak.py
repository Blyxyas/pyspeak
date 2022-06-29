from typing import List, Optional, Tuple
from mapping import DynMap
from chunking import into_chunks

DEFAULT_MEMORY: int = 2
DEFAULT_THRESHOLD: float = 0.15
DEFAULT_MAX_OUTPUT_LENGTH: int = 2
DEFAULT_RANGE = 2

def translate(vec: List[str]) -> List[Tuple[int]]:
	result: List[Tuple[int]] = []
	wordvec: List[int] = []

	sum: int = 0

	for phrase in vec:
		for word in phrase.split(" "):
			for char in word:
				sum += ord(char)
			# End word
			wordvec.append((((sum << 1) + 1) << 1) + 1)
			sum = 0
		# End phrase
		result.append(tuple(wordvec.copy()))
		wordvec.clear()

	return result

def learn(map: DynMap, memory: Optional[str] = DEFAULT_MEMORY):
	# Thanks to the default values I don't have to create a wrapper with a O(16) case covering! (for `run`)

	TKeys: List[List[int]] = translate(map.keys)
	TValues: List[List[int]] = translate(map.values)

	mega: List[List[int]] [[]]
	ram: List[int] = []

	for (key, value) in (TKeys, TValues):
		for keychunk in key.into_chunks(memory).base:
			for valuechunk in value.into_chunks(memory).base:
				ram.append(
					sum(keychunk) / sum(valuechunk)
				)
		
		mega.append(ram)
		ram.clear()

	return mega