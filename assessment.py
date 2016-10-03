"""List Assessment 

Edit the functions until all of the doctests pass when
you run this file.
"""


def all_odd(numbers):
    """Return a list of only the odd numbers in the input list.

    For example::

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []
    """
    # empty list to store results
    list_of_odd_numbers = []
    # looping through each number in list of numbers
    for number in numbers:
        # if number does not divide evenly with 2, that means it's odd
        if number % 2 != 0:
            # add the odd number fo the list_of_odd_numbers list
            list_of_odd_numbers.append(number)
        # otherwise, skip it
        else:
            pass
    return list_of_odd_numbers


def print_indices(items):
    """Print index of each item in list, followed by item itself.

    Do this without using a "counting variable" --- that is, don't
    do something like this::

        count = 0
        for item in list:
            print count
            count = count + 1

    Output should look like this::

        >>> print_indices(["Toyota", "Jeep", "Volvo"])
        0 Toyota
        1 Jeep
        2 Volvo
    """
    # using the enumerate built-in function to print each number with its
    # index value, starting at zero
    for c, value in enumerate(items, 0):
        print c, value


def foods_in_common(foods1, foods2):
    """Find foods in common.

    Given 2 lists of foods, return the items that are in common
    between the two, sorted alphabetically.

    **NOTE**: for this problem, you're welcome to use any of the
    Python data structures you've been introduced to (not just
    lists). Is there another that would be a good idea?

    For example::

        >>> foods_in_common(
        ...     ["cheese", "bagel", "cake", "kale"],
        ...     ["hummus", "beets", "bagel", "lentils", "kale"]
        ... )
        ['bagel', 'kale']

    If there are no foods in common, return an empty list::

        >>> foods_in_common(
        ...     ["lamb", "chili", "cheese"],
        ...     ["cake", "ice cream"]
        ... )
        []

    """
    # turn the foods lists into sets in order to use set math
    set_foods1 = set(foods1) 
    set_foods2 = set(foods2)
    # find the intersection / commonality between the two food sets
    common_set = set_foods1 & set_foods2
    # turn the common set into a list, and sort it
    common_list = sorted(list(common_set))
    # if the common_list is empty, then there was no commonality
    # return empty list
    if not common_list:
        return []
    # if there were items in common, return the sorted list
    else: 
        return common_list


def every_other_item(items):
    """Return every other item in `items`, starting at first item.

    For example::

       >>> every_other_item([1, 2, 3, 4, 5, 6])
       [1, 3, 5]

       >>> every_other_item(
       ...   ["you", "z", "are", "z", "good", "z", "at", "x", "code"]
       ... )
       ['you', 'are', 'good', 'at', 'code']
    """
    # empty list
    alternate = []
    # looping through each item in items, but with a cadence of 2
    # therefore skipping every other item
    for item in items[::2]:
        # add the item not skipped to the alternate list
        alternate.append(item)
    return alternate


def largest_n_items(items, n):
    """Return the `n` largest integers in list, in ascending order.

    You can assume that `n` will be less than the length of the list.

    For example::

        >>> largest_n_items([2, 6006, 700, 42, 6, 59], 3)
        [59, 700, 6006]

    It should work when `n` is 0::

        >>> largest_n_items([3, 4, 5], 0)
        []

    If there are duplicates in the list, they should be counted
    separately::

        >>> largest_n_items([3, 3, 3, 2, 1], 2)
        [3, 3]
    """
    # empty list
    largest = sorted([])
    # throwaway list that provides a sorted version of items inputted
    sorted_and_deletable_list = sorted(items)
    # looping through each item in items
    for item in items:
        # if the length of the list of stored numbers is equal to n, we have
        # enough numbers in the list and can just return the list
        if len(largest) == n:
            return largest
        # but while the length of stored numbers is still less than n....
        elif len(largest) < n:
            # add the last number from the sorted / throwaway list
            # presumably the largest
            largest.append(sorted_and_deletable_list[-1])
            # delete the last number from the throwaway list
            sorted_and_deletable_list.pop()
            # sort the largest list while you're at it
            largest.sort()
    
    return largest


#####################################################################
# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
