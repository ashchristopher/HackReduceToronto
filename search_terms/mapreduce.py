import sys
import json

from disco.core import Disco, result_iterator
from disco.settings import DiscoSettings

from disco import func
import time


from mapper import map
from reducer import reduce

name = "gap-%s" % int(time.time())
disco = Disco(DiscoSettings()['DISCO_MASTER'])
print "Starting Disco job (%s).." % name
print "Go to %s to see status of the job." % disco.master

results = disco.new_job(name=name,
        input=["tag://gap:1million"],
        map_input_stream=(
            func.map_input_stream,
            func.chain_reader,
        ),
        map=map, 
        reduce=reduce, 
        save=True).wait()

print "Job done. Results:"
f = open('data.js', 'w')
for time_of_day, scores in result_iterator(results):
    str_time = time_of_day.strftime("%Y-%m-%d %H:%M")
    s = json.dumps({
        'time': str_time,
        'scores': scores
    })

    f.write(s + ",\n")

f.close()

