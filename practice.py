"""List Practice

Edit the functions until all of the doctests pass when
you run this file.
"""


def print_list(items):
    """Print each item in the input list.

    For example::

        >>> print_list([1, 2, 6, 3, 9])
        1
        2
        6
        3
        9
    """
    for item in items:
        print item


def long_words(words):
    """Return words in input list that longer than 4 characters.

    For example::

        >>> long_words(["hello", "a", "b", "hi", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

    (If there are duplicates, show both --- notice "bacon" appears
    twice in output)

    If no words are longer than 4 characters, return an empty list::

        >>> long_words(["all", "are", "tiny"])
        []
    """
    # empty list
    longer_words = []
    # looping through each word in words
    for word in words:
        # if the length of the word is greater than four letters
        if len(word) > 4:
            # append that word to the longer_words list
            longer_words.append(word)
        # otherwise, pass
        else:
            pass
    return longer_words


def n_long_words(words, n):
    """Return words in list longer than `n` characters.

    For example::

        >>> n_long_words(
        ...     ["hello", "hey", "spam", "spam", "bacon", "bacon"],
        ...     3
        ... )
        ['hello', 'spam', 'spam', 'bacon', 'bacon']

        >>> n_long_words(["I", "like", "apples", "bananas", "you"], 5)
        ['apples', 'bananas']
    """
    # empty list
    longer_words = []
    # looping through each word in words
    for word in words:
        # if the length of the word is longer than "n"
        if len(word) > n:
            # add that word to the longer_words list
            longer_words.append(word)
        # otherwise, skip it
        else:
            pass
    return longer_words


def smallest_int(numbers):
    """Find the smallest integer in a list of integers and return it.

    **DO NOT USE** the built-in function `min()`!

    For example::

        >>> smallest_int([-5, 2, -5, 7])
        -5

        >>> smallest_int([3, 7, 2, 8, 4])
        2

    If the input list is empty, return `None`::

        >>> smallest_int([]) is None
        True
    """

    smallest = []
    # the edge case: if the input list is empty, return 'None'
    if not numbers:        
        return None
    # looping through each number, adding it to the smallest list
    for number in numbers:
        # using boolean to determine if smallest list is empty
        # if smallest list is empty, this adds the first number to the list
        # regardless of its size
        if not smallest:
            smallest.append(number)
        # now that we have a number to compare it against, if new number
        # is less than current number:
        elif number < smallest[0]:
            # delete the old (bigger) bumber
            smallest.pop(0)
            # add new (smaller) number
            smallest.append(number)
        # otherwise, if the number is bigger; just pass
        else:
            pass
    # specifically returning the value of the smallest number
    return smallest[0]


def largest_int(numbers):
    """Find the largest integer in a list of integers and return it.

    **DO NOT USE** the built-in function `max()`!

    For example::

        >>> largest_int([-5, 2, -5, 7])
        7

        >>> largest_int([3, 7, 2, 8, 4])
        8

    If the input list is empty, return None::

        >>> largest_int([]) is None
        True
    """
    largest = []
    # if the input list is empty, returning None
    if not numbers:
        return None
    # looping through each number to find largest int
    for number in numbers:
        # if this is the first number, it's automatically the largest
        # adding to list
        # using boolean to determine
        if not largest:
            largest.append(number)
        # if new number is bigger than current number in largest list, index 0
        elif number > largest[0]:
            # delete existing number
            largest.pop(0)
            # add new bigger number
            largest.append(number)
        # otherwise, skip it
        else:
            pass
    # returning the largest int of the list
    return largest[0]


def halvesies(numbers):
    """Return list of numbers from input list, each divided by two.

    For example::

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are odd, make sure you don't round off
    the half::

        >>> halvesies([1, 5])
        [0.5, 2.5]
    """
    # using list comprehension
    # making sure to turn it into a flaot, so that you don't round the answers
    halves = [float(number) / 2 for number in numbers]
    return halves

def word_lengths(words):
    """Return the length of words in the input list.

    For example::

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]
    """

    length_of_words = []
    # looping through the words
    for word in words:
    # adding just the length of the word to the list length_of_words
        length_of_words.append(len(word))
    # returning the list with word length values
    return length_of_words


def sum_numbers(numbers):
    """Return the sum of all of the numbers in the list.

    Python has a built-in function, `sum()`, which already does
    this --- but for this exercise, you should not use it.

    For example::

        >>> sum_numbers([1, 2, 3, 10])
        16

    Any empty list should return the sum of zero::

        >>> sum_numbers([])
        0
    """
    # starting at zero
    total = 0
    # for each number provided, add that number to the total
    for number in numbers:
        total += number
    return total


def mult_numbers(numbers):
    """Return product (result of multiplication) of numbers in list.

    For example::

        >>> mult_numbers([1, 2, 3])
        6

    Obviously, if there is a zero in input, the product is zero::

        >>> mult_numbers([10, 20, 0, 50])
        0

    As explained at http://en.wikipedia.org/wiki/Empty_product,
    if the list is empty, the product should be 1::

        >>> mult_numbers([])
        1
    """
    # must start with 1, otherwise all returned value will be zero
    total = 1
    # for each number, multiply by the total
    for number in numbers:
        total = total * number
    return total


def join_strings(words):
    """Return a string of all input strings joined together.

    Python has a built-in method, `list.join()` --- but for
    this exercise, **you should not use it**.

    For example::

        >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
        'spamspambaconballoonicorn'

    For an empty list, you should return an empty string::

        >>> join_strings([])
        ''
    """
    # empty string to start with
    joined = ''
    # for word in words, add the word to the empty string
    for word in words:
        joined += word
    return joined


def average(numbers):
    """Return the average (mean) of the list of numbers given.

    For example::

        >>> average([2, 4])
        3.0

    This should handle cases where the result isn't an integer::

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty;
    it's fine if this raises an error when given an empty list.

    (Think of the best way to handle an empty input list, though,
    a feel free to provide a good solution here.)
    """
    # assuming we're dealing with humans, providing a quick error message
    # explaining exactly what "went wrong" (the input list is empty)
    # should help to relieve the human
    if not numbers:
        print "Sorry, you didn't provide any numbers to get an average."
    # calculating the average using built in Python functions
    average = float(sum(numbers)) / len(numbers)
    return average


def join_strings_with_comma(words):
    """Return ['list', 'of', 'words'] like "list, of, words".

    For example::

        >>> join_strings_with_comma(
        ...     ["Labrador", "Poodle", "French Bulldog"]
        ...     )
        'Labrador, Poodle, French Bulldog'

    If there's only one thing in the list, it should return just that
    thing, of course::

        >>> join_strings_with_comma(["Pretzel"])
        'Pretzel'
    """
    # starting with empty string
    comma_string = ''
    # looping through each word
    for word in words:
        # only add the word with a comma if there are multiple things in list
        # which means it starts at index 1 in the list
        if word in words[1:]:
            comma_string = comma_string + ', ' + word
        # otherwise, it's the only item in the list, so don't bother adding
        # a comma
        else: 
            comma_string += word
    return comma_string


def reverse_list(items):
    """Return the input list, reversed.

    **Do not use** the python function `reversed()` or the method
    `list.reverse()`.

    For example::

        >>> reverse_list([1, 2, 3])
        [3, 2, 1]

        >>> reverse_list(["cookies", "love", "I"])
        ['I', 'love', 'cookies']

    You should do this without changing the original list::

        >>> orig = ["apple", "berry", "cherry"]
        >>> reverse_list(orig)
        ['cherry', 'berry', 'apple']
        >>> orig
        ['apple', 'berry', 'cherry']
    """
    # empty list
    reversed_list = []
    # looping through each item in items, using list slicing to go backwards
    for item in items[::-1]:
        # add the item in the reversed_empty list
        reversed_list.append(item)
    return reversed_list


def reverse_list_in_place(items):
    """Reverse the input list `in place`.

    Reverse the input list given, but do it "in place" --- that is,
    do not create a new list and return it, but modify the original
    list.

    **Do not use** the python function `reversed()` or the method
    `list.reverse()`.

    For example::

        >>> orig = [1, 2, 3]
        >>> reverse_list_in_place(orig)
        >>> orig
        [3, 2, 1]

        >>> orig = ["cookies", "love", "I"]
        >>> reverse_list_in_place(orig)
        >>> orig
        ['I', 'love', 'cookies']
    """
    # using index to reassign item placement
    count = 0
    # looping over each item in items, starting with the last one
    for item in items[::-1]:
        # used list-slice assignment to make last item first, and so on
        items[count] = item
        # each time we cycle through, the count goes up
        count += 1
    return 


def duplicates(items):
    """Return list of words from input list which were duplicates.

    Return a list of words which are duplicated in the input list.
    The returned list should be in ascending order.

    For example::

        >>> duplicates(
        ...     ["apple", "banana", "banana", "cherry", "apple"]
        ... )
        ['apple', 'banana']

        >>> duplicates([1, 2, 2, 4, 4, 4, 7])
        [2, 4]

    You should do this without changing the original list::

        >>> orig = ["apple", "apple", "berry"]
        >>> duplicates(orig)
        ['apple']

        >>> orig
        ['apple', 'apple', 'berry']
    """
    # starting with empty list
    list_of_duplicates = []
    # looping through each item
    for item in items:
        # determining if there are duplicates of the item in the original list
        # with count built-in function
        if items.count(item) > 1:
            # there are duplicates! but is it already in our list of duplicates?
            # if yes, skip it!
            if item in list_of_duplicates:
                pass
            # if it's not already in there, then append it
            else:
                list_of_duplicates.append(item)
        # if there are no duplicates, do nothing to it
        else:
            pass
    return list_of_duplicates


def find_letter_indices(words, letter):
    """Return list of indices where letter appears in each word.

    Given a list of words and a letter, return a list of integers
    that correspond to the index of the first occurrence of the letter
    in that word.

    **DO NOT** use the `list.index()` method.

    For example::

        >>> find_letter_indices(['odd', 'dog', 'who'], 'o')
        [0, 1, 2]

    ("o" is at index 0 in "odd", is at index 1 in "dog", and at
    index 2 in "who")

    If the letter doesn't occur in one of the words, use `None` for
    that word in the output list. For example::

        >>> find_letter_indices(['odd', 'dog', 'who', 'jumps'], 'o')
        [0, 1, 2, None]

    ("o" does not appear in "jumps", so the result for that input is
    `None`.)
    """
    # empty list of the indeces
    list_of_indices = []
    # a counter to keep track of the index value while looping
    index_count = 0
    # for each word in the list provided
    for word in words:
        # the word either contains the letter or it does
        # if the letter is not in the word, just add none to the list
        if letter not in word:
            list_of_indices.append(None)
        # if the word does contain the letter
        elif letter in word:
            # for each letter in the word
            for each_letter in word:
                # determine if the letter of the word, starting at index 0
                # is the same as the letter variable provided
                # if yes
                if letter == word[index_count]:
                    # add that index_count to the list of indices
                    list_of_indices.append(index_count)
                    # reset the counter
                    index_count = 0
                    # break out of the loop
                    break
                # otherwise, add 1 to the counter and keep going
                else:
                    index_count += 1

    return list_of_indices

#####################################################################
# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
