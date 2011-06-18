import sys
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

"""
:clicks (ad id,people who clicked the ads)
"""
results = disco.new_job(name=name,
        input=["tag://data:gap:100000"],
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

