def map(line, params):
    """
    hackreduce:search:history format:
        None, timestamp, id, search, frequency?
    """
    from datetime import datetime, timedelta
    from disco.util import msg

    time_grouping = 30

    try: 
        unknown, timestamp, uid, query, frequency = line.split("','")
    except ValueError:
        msg(line)

    # bad hack :-(
    time = timestamp.replace("'", "")
    date_obj = datetime.fromtimestamp(float(time[:-3])) # timestamp has milliseconds, shave em off
    nearest_minute = date_obj - timedelta(
            minutes=date_obj.minute % time_grouping, 
            seconds=date_obj.second, 
            microseconds=date_obj.microsecond)


    # Give a score if the words within each query are in any of the 4 lists.
    sex = ('cockrings', 'sex', 'tits', 'naked', 'girls', 'fuck', 'suck', 'teen', 
                'hot', 'cum', 'topless', 'nude', )

    travel = ('fly', 'flight', 'plane', 'drive', 'europe', 'america', 'tours', 
                'map', 'hotel', 'cheap', 'asia', )

    nerd = ('java ', 'c ', 'c++', 'php', 'visual basic', 'perl', 
            'python', 'c#', 'javascript', 'ruby', 'erlang', 'lisp', )

    cooking = ('ice', 'cream', 'recipe', 'pasta', 'sauce', 'soup', 'meat', )


    score = {'sex': 0, 'nerd': 0, 'travel': 0, 'cooking': 0}

    for word in query.split():
        for key in score.keys():
            score[key] += int(word.lower() in locals()[key])

    yield (nearest_minute, score)
