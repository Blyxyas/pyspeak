from typing import List, Tuple
def translate(vec: List[str]) -> List[Tuple[int]]:
	result: List[List[int]] = []
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
		result.append(tuple(wordvec))
		wordvec.clear()
	
	return result

