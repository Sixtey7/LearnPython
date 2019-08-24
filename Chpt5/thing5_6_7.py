def doTheThing():
    from pprint import pprint
    #Thing 5
    print ('---Thing 5---')
    plain = {'a': 1, 'b': 2, 'c': 3}
    pprint(plain)
    print("Plain at b:", plain['b'])

    #Thing 6
    print ('---Thing 6---')
    from collections import OrderedDict
    fancy = OrderedDict({'a': 1, 'b': 2, 'c': 3})
    pprint (fancy)
    print ("Fancy at b:", fancy['b'])

    #Thing 7
    from collections import defaultdict
    dict_of_lists = defaultdict(list)
    dict_of_lists['a']
    dict_of_lists['a'].append('something for a')
    pprint(dict_of_lists)