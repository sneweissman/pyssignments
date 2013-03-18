"""
The class below (which intentionally uses poorly named variables) is broken.
Your task is to examine the docstrings and tests.py to see how we expect
the class to work, and then make changes to the code below so the tests will
pass.

You should not modify tests.py.

Extra credit: after you run the program, examine the working directory and look
at the .pyc files. How do they differ from the .py files, and why? What happens
if you delete them and run the program again?
"""


class Transformalizer(object):
    """
    The transformalizer is a silly class with methods to transform individual
    objects and lists of objects.
    """
    def __init__(self, transformer):
        """
        Instantiate with a ``transformer`` function that takes an object and
        returns a brand new object.

        What kind of new object does the transformer return? Only the developer
        knows! You could turn strings into ints, ints into strings, strings into
        slightly longer strings. Your imagination is the limit.
        """
        self.transformer = transformer

    def transform(self, item):
        """
        Use ``self.transformer`` on the supplied ``item`` and give the caller
        the transformed object.
        """
        return self.transformer(item)

    def bulk_transform(self, items):
        """
        Takes a list of ``items``, modifies each item, and returns a new list
        with the modified items.
        """
        return [self.transform(item) for item in items]

