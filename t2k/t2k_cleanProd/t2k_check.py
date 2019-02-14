#! /usr/bin/env python

import os



from dirac_ls import *
from diracTools import* 
# included in dirac_ls
#from DIRAC.Core.Base import Script
#Script.initialize()
#from DIRAC.Resources.Catalog.FileCatalog import FileCatalog

fc = FileCatalog()
path = '/t2k.org/user/'
res = fc.listDirectory(path)
print(res)

print('')
fileList = dirac__ls(path)

#help(dirac__ls)
#list_dir(fc, '/t2k.org/user/k/sophie.king/')

# t2k
# f = 'oa_nt_beam_90910104-0055_vxgqz23zqgzm_numc_000_magnet201508waterrun9.root'
#  8 numbers - 4 numbers
# to get number   [11:][:13]

#print(f[11:])
#print( f[11:][:13] )
#print( (f[11:][:13]).split('-', 1) )



########################################################
def dfc_list(local_path, dfc_path, type_dir, type_name):
########################################################
    """Generates a DFC list (including full path
       local path = local dir for output lists (e.g.  ./cleanUp/runX/')
       dfc_path   = parent dir on dfc   (e.g. '/t2k.org/whatever')
       type_dir   = sub dir(s) on dfc   (e.g. '/numc/')
       type_name  = name for list       (e.g. 'numc')
       NOTE:  Can also return a list object
 """


    mklocal = 'mkdir -p ' + local_path
    os.system(mklocal)
    
    dfc_list = dirac__ls(dfc_path + type_dir)
    
    file_name = local_path + '/'+ type_name + '_dfc.list'
    
    f = open(file_name, "w+")
    returnList = []

    for line in dfc_list:
        returnList.append(line)
        text = line + '\n'
        f.write(text)
########################################################




#########################################
def extract_num_list(inList, outList):
#########################################
    
    # read in each line, extract numbers in form: ABCD_EFGH
    # write to a new file
    
    f_in  = open(inList, "r")
    f_num = open(outList, "w+")
    
   # if not (  os.path.isfile(inList)   ):
   #    print >>sys.stderr, "extract_number_list :: In file list does not exist"  
   #    return
    
    for line in f_in:
        mod_0 = line.rstrip('\n')                    # strip end of line
        mod_1 = mod_0.rsplit('/', 1)                 # remove directory structure
        mod_2 = mod_1[1][11:][:13]                   # extract number code
        mod_3 = mod_2.split('-',1)                   # split into two numbers
        mod_4 = mod_3[0] + ' ' + mod_3[1]  + '\n'    # write numbers with space and end of line
        f_num.write(mod_4)
    
    f_in.close()
    f_num.close()
#########################################





def extract_miss_rep( numList, misList, repList ):


    f_num  = open(numList, "r")
    f_mis = open(misList,"w+")
    f_rep = open(repList,"w+")
    
    startRun = 90910000
    endRun   = 90910105 # excludes this numebr
    startSub = 0
    endSub   = 56  # excludes this number
    
    
    firstFind = [-99999999, -9999]
        
    
    # create a list, where each element is a line from the text file
    lines = f_num.readlines()
    n_lines = len(lines)
    
    
    # to find repeated lines, you just need to check each line compared to the line above
    # should sort first  = 0
    
    
    # add missing file codes (ABCD_EFGH) to text file
    # f_miss
    
    # also add missing file codes  (ABCD_EFGH) to a list
    missing=[]
    missing_index = 0
    
    # check which file codes are in the list
    # once a code is matched, move to th next line
    lines_index = 0
    
    # loop though the list of desired codes
    # if it matches the current code from the file, move to the next
    # if it does not match, add to missing list
    
    num = (  lines[lines_index].rstrip('\n')  ).split(' ', 1)
    
    for i in range (startRun, endRun, 1):
        for k in range (startSub, endSub, 1):
    
            # check if we exhausted list of files 
            # in which case just add to missing list
            if( lines_index  == n_lines  ):  
                code = str(i).zfill(8) +' '+ str(k).zfill(4)
                f_mis.write( code )
                f_mis.write('\n')
                missing.append( (i,k) )
                missing_index += 1
                continue
    
            if( (i,k) == ( int(num[0]), int(num[1]) ) ):
                lines_index += 1            
                # only need to update num when we increase the index
                # provided it isnt at the end
                if ( lines_index  != n_lines  ):
                    num = (  lines[lines_index].rstrip('\n')  ).split(' ', 1)  
                    print('num = i'),
                    print(num)
            else:
                code = str(i).zfill(8) +' '+ str(k).zfill(4)
                f_mis.write( code )
                f_mis.write('\n')
                missing.append( (i,k) )
                missing_index += 1
                reread = False
    
    print( missing )


    f_num.close()
    f_mis.close()
    f_rep.close() 



 
clean = 'runX_name'
local_path = './cleanUp/' + clean

dfc_path = '/t2k.org/nd280/production006/L/mcp/neut/2015-08-water/magnet/run9/'
type_dir  = '/numc/'  # i.e. subfolder(s)
type_name = 'numc'    # file type name 


dfc_list(local_path, dfc_path, '/numc/', 'numc')
dfc_list(local_path, dfc_path, '/logf/', 'logf')
dfc_list(local_path, dfc_path, '/cata/', 'cata')
#dfc_list(local_path, dfc_path, '/cnfg/', 'cnfg')

l_in  = './cleanUp/runX_name/numc_dfc.list'
l_out = './cleanUp/runX_name/numc_dfc_num.list'

extract_num_list( l_in, l_out)

extract_miss_rep( './cleanUp/runX_name/numc_dfc_num.list', './cleanUp/runX_name/numc_dfc_mis.list', './cleanUp/runX_name/numc_dfc_rep.list' )
