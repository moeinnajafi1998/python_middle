# Frozensets
# •	Description: Immutable sets.
# •	Syntax:
frozen_unique_numbers = frozenset([1, 2, 3, 4, 4, 5])
# •	Operations:
# o	Similar to sets, but no methods to add or remove items.

# Arrays (from array module)
# •	Description: Mutable sequences of items of the same type.
# •	Syntax:
import array
numbers = array.array('i', [1, 2, 3, 4])
# •	Operations:
# o	Access: numbers[0]
# o	Append: numbers.append(5)
# o	Remove: numbers.remove(3)

# Deques (from collections module)
# •	Description: Mutable, double-ended queues.
# •	Syntax:
from collections import deque
d = deque([1, 2, 3, 4])
# •	Operations:
# o	Append: d.append(5)
# o	Appendleft: d.appendleft(0)
# o	Pop: d.pop()
# o	Popleft: d.popleft()

# Namedtuples (from collections module)
# •	Description: Immutable, tuple-like objects with named fields.
# •	Syntax:
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
# •	Operations:
# o	Access by name: p.x
# o	Access by index: p[0]

# Defaultdicts (from collections module)
# •	Description: Dictionaries with default values for non-existent keys.
# •	Syntax:
from collections import defaultdict
dd = defaultdict(int)
dd['key'] += 1
# •	Operations:
# o	Access: dd['key']
# o	Add/Update: dd['key'] = 5

# Counter (from collections module)
# •	Description: A dictionary subclass for counting hashable objects.
# •	Syntax:
from collections import Counter
count = Counter(['a', 'b', 'c', 'a', 'b', 'b'])
# •	Operations:
# o	Access counts: count['a']
# o	Most common: count.most_common(2)

# OrderedDicts (from collections module)
# •	Description: Dictionaries that remember the order in which items were inserted.
# •	Syntax:
from collections import OrderedDict
od = OrderedDict()
od['a'] = 1
od['b'] = 2
# •	Operations:
# o	Access: od['a']
# o	Add/Update: od['c'] = 3

# These data structures provide a wide range of functionalities to handle various programming tasks efficiently.