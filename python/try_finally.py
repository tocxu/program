import sys
import time
f=None
try:
    f=open("poem.txt")
    while True:
        line=f.readline()
        if len(line)==0:
            break
        print line,
        sys.stdout.flush()
        print "Press ctrl+c now"
        time.sleep(1)
except IOError:
    print "could not find file poem.txt"
except KeyboardInterrupt:
    print '!! You cancelled the reading from the file.'
finally:
    if f: f.close()
    print "(Cleaning up: Closing the file)"
print "done"


