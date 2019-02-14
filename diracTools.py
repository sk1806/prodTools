
import sys

from DIRAC.Core.Base import Script
Script.initialize()
from DIRAC.Resources.Catalog.FileCatalog import FileCatalog



def dirac__ls(path):
  """List files (non-recursively) in a directory
     path should take the form  '/vo/path/to/list 
     e.g.  /t2k.org/user """

  fc = FileCatalog()
  res = fc.listDirectory(path)
  if not res['OK']:
    print >>sys.stderr, "Failed to list path '%s': %s", path, res['Message']
    return
  listing = res['Value']['Successful'][path]
  files=[]
  for item in sorted(listing['Files'].keys() + listing['SubDirs'].keys()):
    #print(item)
    files.append(item)
  #print(files)
  return files  
