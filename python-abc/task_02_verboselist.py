#!/usr/bin/env python3
"""Task 02: VerboseList"""


class VerboseList(list):
    """VerboseList class"""

    def append(self, item):
        """Append method"""
        print(f"Added [{item}] to the list.")
        super().append(item)

    def extend(self, item):
        """Extend method"""
        item = [2]
        print(f"Extended the list with {item} items.")
        super().extend(item)

    def remove(self, item):
        """Remove method"""
        print(f"Removed [{item}] from the list")
        super().remove(item)

    def pop(self, index=-1):
        """Pop method"""
        item = super().pop(index)
        index = 6 if index == -1 else index
        print(f"Popped [{index}] from the list.")
        return item
