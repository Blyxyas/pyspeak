from chunking import *
from mapping import *
from speak import *
from typing import List

#
# ===================
#    TESTS
# ===================
#

#@pytest
def test_into_chunks():
	mem: int = 2
	
	# 1. Create a list of mem % len == 0;

	first: List[int] = [1,2,3,4,5,6,7,8]

	# 2. Create a list of mem % len != 0;

	second: List[int] = [1,2,3,4,5,6,7,8,9]

	# (The nine will be left out by the second[-1] chunk)

	first_chunks1: chunks = into_chunks(first, mem)
	second_chunks1: chunks = into_chunks(second, mem)

	first_chunks2: chunks = into_chunks(first, mem + 1)
	second_chunks2: chunks = into_chunks(second, mem + 1)
	
	first_chunks3: chunks = into_chunks(first, mem + 2)
	second_chunks3: chunks = into_chunks(second, mem + 2)

	first_chunks4: chunks = into_chunks(first, mem + 3)
	second_chunks4: chunks = into_chunks(second, mem + 3)

	print("\n", first)
	print(second)
	print("")
	print(first_chunks1.base)
	print(second_chunks1.base)
	print("")
	print(first_chunks2.base)
	print(second_chunks2.base)
	print("")
	print(first_chunks3.base)
	print(second_chunks3.base)
	print("")
	print(first_chunks4.base)
	print(second_chunks4.base)

	# Now, let's assert both results:
	
	assert first_chunks1.base == [[1, 2], [3, 4], [5, 6], [7, 8]]
	assert second_chunks1.base == [[1, 2], [3, 4], [5, 6], [7, 8], [8, 9]]

#@pytest
def test_translate():
	to_translate: List[str] = ["A B C D", "A B C D"]
	translated = translate(to_translate)

	for tuple_ in translated:
		for (i, letter) in enumerate(tuple_):
			rawletter = to_translate[0].split(" ")[i]
			t_rawletter = ((((ord(rawletter) << 1) + 1) << 1) + 1)
			assert t_rawletter == letter

#@pytest
def 