import sys
from disco.core import Disco, result_iterator
from disco.settings import DiscoSettings

from disco import func

def map(line, params):
    """
    hackreduce:search:history format:
        None, timestamp, id, search, frequency?
    """
    from datetime import datetime, timedelta
    from disco.util import msg

    try: 
        unknown, timestamp, uid, query, frequency = line.split("','")
    except ValueError:
        print msg(line)

    # bad hack :-(
    time = timestamp.replace("'", "")
    date_obj = datetime.fromtimestamp(float(time[:-3])) # timestamp has milliseconds, shave em off
    nearest_minute = date_obj - timedelta(minutes=date_obj.minute % 1, seconds=date_obj.second, microseconds=date_obj.microsecond)

    yield (nearest_minute, {'unique_id': uid, 'query': query, 'frequency': frequency})

def reduce(iter, params):
    # This doesn't work at all, its from an old example.
    for unique_id, counts in kvgroup(sorted(iter)):
        yield unique_id, sum(counts)

disco = Disco(DiscoSettings()['DISCO_MASTER'])
print "Starting Disco job.."
print "Go to %s to see status of the job." % disco.master

"""
:clicks (ad id,people who clicked the ads)
"""
results = disco.new_job(name="bartekc",
        input=["tag://hackreduce:search:history"],
        map_input_stream=(
            func.map_input_stream,
            func.chain_reader,
        ),
        map=map, 
        reduce=reduce, 
        save=True).wait()

print "Job done. Results:"
for word, count in result_iterator(results):
    print word, count
