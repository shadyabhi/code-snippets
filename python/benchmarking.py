from contextlib import contextmanager
import time

@contextmanager

def timeblock(label):
  start = time.clock()
  try:
    yield
  finally:
    end = time.clock()
    print '{0} : {1}'.format(label, end - start)

with timeblock("just a test"):
  print "yippee"
