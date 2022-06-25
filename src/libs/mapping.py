from typing import Union, overload, List, Any

# This mapping.* file is very simple because the original Rust's `DynMap` was meant to be a dynamic HashMap, but Python has `dict` so there's no need to re-create anything.

# I'll create a class `DynMap` only to use encourage and disencourage.

def move_index(l: List[Any], idx: int, to: int) -> None:
	l.insert(to, l.pop(idx))

class DynMap(dict):
	@overload
	def encourage(self, index: str, how_much: int) -> None:
		newindex = list(self.keys).index(index)
		move_index(list(self.keys), newindex, newindex - how_much)
		move_index(list(self.values), newindex, newindex - how_much)

	@overload
	def encourage(self, index: int, how_much: int) -> None:
		move_index(list(self.keys), index, index - how_much)
		move_index(list(self.values), index, index - how_much)