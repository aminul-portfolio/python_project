# data_empty_all.py

topics = [
    {
        'title': 'map()',
        'function': 'map(function, iterable)',
        'learn': 'Transform elements in a list using a function or lambda.',
        'reuse': 'Helpful in temperature conversion, formatting data, etc.',
        'examples': [
            {'code': 'def fahrenheit(c): return (9/5)*c + 32\nmap(fahrenheit, [0, 22.5, 40])', 'comment': 'Convert temps'},
            {'code': 'map(lambda x: x*x, [1, 2, 3])', 'comment': 'Square elements'},
            {'code': 'list(map(str.upper, ["a", "b"]))', 'comment': 'Uppercase strings'},
            {'code': 'map(len, ["hi", "hello"])', 'comment': 'Get length of strings'}
        ]
    },
    {
        'title': 'reduce()',
        'function': 'reduce(function, iterable)',
        'learn': 'Apply rolling computation.',
        'reuse': 'Use for sum/product/finding max.',
        'examples': [
            {'code': 'from functools import reduce\nreduce(lambda x,y: x+y, [1,2,3,4])', 'comment': 'Sum values'},
            {'code': 'reduce(lambda x,y: x*y, [1,2,3])', 'comment': 'Multiply values'},
            {'code': 'reduce(lambda a,b: a if a>b else b, [1,5,2])', 'comment': 'Max value'},
            {'code': 'reduce(lambda x,y: x+y, "abc")', 'comment': 'Concatenate string'}
        ]
    },
    {
        'title': 'filter()',
        'function': 'filter(function, iterable)',
        'learn': 'Filter items based on condition.',
        'reuse': 'Remove negatives, clean data.',
        'examples': [
            {'code': 'filter(lambda x: x > 0, [-1, 0, 1])', 'comment': 'Keep positives'},
            {'code': 'filter(None, [0, 1, "", "a"])', 'comment': 'Keep truthy values'},
            {'code': 'list(filter(lambda x: len(x)>3, ["cat", "tiger"]))', 'comment': 'Long words'},
            {'code': 'list(filter(str.isalpha, ["abc", "123", "!"]))', 'comment': 'Only alphabetic'}
        ]
    },
    {
        'title': 'zip()',
        'function': 'zip(iter1, iter2, ...)',
        'learn': 'Combine multiple iterables.',
        'reuse': 'Pair data, merge headers & rows.',
        'examples': [
            {'code': 'zip([1,2], ["a", "b"])', 'comment': 'Zip two lists'},
            {'code': 'dict(zip(["id", "name"], [101, "Alice"]))', 'comment': 'Create dictionary'},
            {'code': '[(x,y) for x,y in zip([1,2], [3,4])]', 'comment': 'List of tuples'},
            {'code': 'list(zip(*[[1,2],[3,4]]))', 'comment': 'Transpose matrix'}
        ]
    }
]

quiz_data = [
    {'question': "What does `map()` return?", 'answer': "map object", 'hint': "It’s not a list"},
    {'question': "What’s the result of `any([False, True])`?", 'answer': "true", 'hint': "At least one True"},
    {'question': "What’s used to reduce a list to a single value?", 'answer': "reduce", 'hint': "Think functools"},
    {'question': "Which function filters out unwanted values?", 'answer': "filter", 'hint': "Conditional inclusion"},
    {'question': "What does `zip()` do?", 'answer': "combine iterables", 'hint': "Pairs items together"}
]
