# yield (nearest_minute, { 'nerd' : <num>, 'sex' : <num>, ...})

def reduce(iter, params):
    from disco.util import kvgroup
    for nearest_minute, queries in kvgroup(sorted(iter)):
        results = {
            'nerd' : 0,
            'sex' : 0,
            'travel': 0,
            'cooking': 0,
        }
        for result_dict in queries:
            for key in results.keys():
                results[key] += result_dict[key]
        yield nearest_minute, results
