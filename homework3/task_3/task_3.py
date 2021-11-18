"""
# I decided to write a code that generates data filtering object from a list of
keyword parameters:

class Filter:
    \"""
        Helper filter class. Accepts a list of single-argument
        functions that return True if object in list conforms to some criteria
    \"""
    def __init__(self, functions):
        self.functions = functions

    def apply(self, data):
        return [
            item for item in data
            if all(i(item) for i in self.functions)
        ]

# example of usage:
# positive_even = Filter([lambda a: a % 2 == 0, lambda a: a > 0,
#                       lambda a: isinstance(a, int)])
# positive_even.apply(range(100)) should return only even numbers from 0 to 99


def make_filter(**keywords):
    \"""
        Generate filter object for specified keywords
    \"""
    filter_funcs = []
    for key, value in keywords.items():
        def keyword_filter_func(value):
            return value[key] == value
        filter_funcs.append(keyword_filter_func)
    return Filter(filter_funcs)


sample_data  =  [
     {
         "name": "Bill",
         "last_name": "Gilbert",
         "occupation": "was here",
         "type": "person",
     },
     {
         "is_dead": True,
         "kind": "parrot",
         "type": "bird",
         "name": "polly"
     }
]

# make_filter(name='polly', type='bird').apply(sample_data) should return only
second entry from the list

# There are multiple bugs in this code. Find them all and write tests for
faulty cases.

"""


class Filter:
    """
    Helper filter class. Accepts a list of single-argument
    functions that return True if object in list conforms to some criteria
    """
    def __init__(self, functions):
        self.functions = functions

    def apply(self, data):
        return [item for item in data if all(i(item) for i in self.functions)]


def make_filter(**keywords):
    """
    Generate filter object for specified keywords
    :param keywords: keyword arguments
    :return:  Filter object
    """
    filter_funcs = []
    for key, value in keywords.items():

        def keyword_filter_func(some_data, k=key, v=value):
            return some_data.get(k) == v

        filter_funcs.append(keyword_filter_func)
    return Filter(filter_funcs)
