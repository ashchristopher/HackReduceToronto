# yield (nearest_minute, {'unique_id': uid, 'query': query, 'frequency': frequency})

def reduce(iter, params):
    from disco.util import kvgroup
    for nearest_minute, queries in kvgroup(sorted(iter)):
        yield nearest_minute, len(queries)