#!/usr/bin/env python3

grid = """
   H 
 WWW 
H    
"""

final_grid = [x for x in grid if x != "\n"]

import pprint
pprint.pprint(final_grid)
print("grid size = {}".format(len(final_grid)))
