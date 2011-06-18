import sys
from disco.core import Disco, result_iterator
from disco.settings import DiscoSettings
import time


from mapper import map
from reducer import reduce

name = "ash-%s" % int(time.time())
disco = Disco(DiscoSettings()['DISCO_MASTER'])
print "Starting Disco job (%s).." % name
print "Go to %s to see status of the job." % disco.master
results = disco.new_job(name=name,
                        input=["tag://data:foobar"],
                        map=map,
                        reduce=reduce,
                        save=True).wait()
print "Job done. Results:"
for word, count in result_iterator(results):
    print word, count
