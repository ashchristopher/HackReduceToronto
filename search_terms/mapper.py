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

    yield (nearest_minute, {'unique_id': uid, 'query': query, 'frequency': frequency})
