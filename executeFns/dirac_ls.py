#!/usr/bin/env python

# gives an ls of dfc without recurisve behaviour 
# (i.e. doesnt recursively show the conetntes of folders in the given location)

# Usage:  $ ./dirac_list.py /t2k.org/user/

import sys

from DIRAC.Core.Base import Script
Script.initialize()
from DIRAC.Resources.Catalog.FileCatalog import FileCatalog

def list_dir(fc, path):
  res = fc.listDirectory(path)
  if not res['OK']:
    print >>sys.stderr, "Failed to list path '%s': %s", path, res['Message']
    return
  listing = res['Value']['Successful'][path]
  for item in sorted(listing['Files'].keys() + listing['SubDirs'].keys()):
    print item

def main():
  fc = FileCatalog()
  if len(sys.argv) < 2:
    print >>sys.stderr, "Usage: diracls.py <path> ..."
    sys.exit(1)
  for path in sys.argv[1:]:
    list_dir(fc, path)

if __name__ == '__main__':
  main()


