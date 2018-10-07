import gwysearch as FG
import os
import sys

FG.SEARCH_FOR="gwyddion.exe"
FG.PATH_HINT="/"
GWYDDION_PATH=FG.find()

if (GWYDDION_PATH is not None):
    print (">>> Appending to 'sys.path'")
    sys.path.append(GWYDDION_PATH)
    print (">>> Importing MODULE 'gwy'")
    import gwy
else:
    sys.exit(">>> Gwyddion NOT found!")
