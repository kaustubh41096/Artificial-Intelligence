import sys
import ucostsearch
import astarsearch

if len(sys.argv) == 4:
    ucostsearch.init_search(sys.argv[1], sys.argv[2], sys.argv[3])
elif len(sys.argv) == 5:
    astarsearch.init_search(sys.argv[1], sys.argv[4], sys.argv[2], sys.argv[3])
else:
    print("Invalid arguments")
