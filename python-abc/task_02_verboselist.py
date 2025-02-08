#!/usr/bin/env python3
"""Task 02: VerboseList"""


class VerboseList(list):
    """VerboseList class"""

    def append(self, item):
        """Append method"""
        print(f"Added [{item}] to the list.")
        super().append(item)

    def extend(self, items):
        """Extend method"""
        items = [2]
        print(f"Extended the list with {items} items.")
        super().extend(items)

    def remove(self, item):
        """Remove method"""
        print(f"Removed [{item}] from the list")
        super().remove(item)

    def pop(self, index=-1):
        """Pop method"""
        print(f"Popped [{index}] from the list")
        return super().pop(index)
