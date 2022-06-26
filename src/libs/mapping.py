from typing import Union, List, Any

# This mapping.* file is very simple because the original Rust's `DynMap` was meant to be a dynamic HashMap, but Python has `dict` so there's no need to re-create anything.

# I'll create a class `DynMap` only to use encourage and disencourage.

def move_index(l: List[Any], idx: int, to: int) -> None:
	l.insert(to, l.pop(idx))

class DynMap(dict):
	def encourage(self, index: Union[str, int], how_much: int) -> None:
		if isinstance(index, str):
			newindex = list(self.keys()).index(index)
	
		else:
			newindex = index

		move_index(list(self.keys()), newindex, newindex - how_much)
		move_index(list(self.values()), newindex, newindex - how_much)

	def discourage(self, index: Union[str, int], how_much: int):
		if isinstance(index, str):
			newindex = list(self.keys()).index(index)
	
		else:
			newindex = index

		move_index(list(self.keys()), newindex, newindex + how_much)
		move_index(list(self.values()), newindex, newindex + how_much)
