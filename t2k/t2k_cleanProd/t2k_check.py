#! /usr/bin/env python

import os
import sys
sys.path.append('../../libFns')


#from dirac_ls import *
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
    
    # read in each line, extract numbers
    # from ABCD-EFGH in filename
    # to   ABCD EFGH in output list
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





def extract_miss_rep( numList, misList, repList , startRun, endRun, startSub=0, endSub = 56):


    f_num = open(numList, "r")
    f_mis = open(misList,"w+")
    f_rep = open(repList,"w+")
    
#    startRun = 90910000
#    endRun   = 90910105 # excludes this numebr
#    startSub = 0
#    endSub   = 56  # excludes this number
    
    
    firstFind = [-99999999, -9999]
        
    
    # create a list, where each element is a line from the text file
    lines = f_num.readlines()
    n_lines = len(lines)
    print('# lines = '),
    print(n_lines)
    print(lines[0])
    print('')
    
    
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
 
    if( int(num[0]) < startRun ):
        print('First file run number is below loop range!! ')
        exit()
    if( int(num[1]) < startSub ):
        print('First file subrun number is below loop range!! ')
        exit()
    
    for i in range (startRun, endRun, 1):
        for k in range (startSub, endSub, 1):
            print(i, k)
            print('checking lines[lines_index] = '+  lines[lines_index])

            # check for repeated run codes     
            # check if line is the same as the one before
            # if it is then write this line to the rep file
            # then increase the line index (and hence 'num') 
            # so you can still do the other checks now you skipped to the next line
            # while keeping number i,k the same
            if( lines_index>0 and lines[lines_index] == lines[lines_index -1] ):
                print('Repeated entry:  ' +  lines[lines_index] )
                # write the line to the file (node the i,k because these are now ahead)
                code = str(num[0]).zfill(8) +' '+ str(num[1]).zfill(4)
                f_rep.write( code )
                f_rep.write('\n')
                #lines_index += 1
                lines_index += 1            
                # only need to update num when we increase the index
                # provided it isnt at the end
                if ( lines_index  != n_lines  ):
                    num = (  lines[lines_index].rstrip('\n')  ).split(' ', 1)  
                 
            # check if we exhausted list of files 
            # in which case just add to missing list
            if( lines_index  == n_lines  ):  
                #print('End of file')
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
                    #print('Found num = '),
                    #print(num)
            else:
                code = str(i).zfill(8) +' '+ str(k).zfill(4)
                f_mis.write( code )
                f_mis.write('\n')
                missing.append( (i,k) )
                missing_index += 1
                reread = False
                #print('--- MISSING num = i')
    
    #print( missing )


    f_num.close()
    f_mis.close()
    f_rep.close() 




########################################################
def search_codes(numList, inpList, outList):
########################################################
    """Takes a file containing number codes ABCD EFGH,
       adds the dash, and searches another list of files for these codes
       numList   = file containing list of numbers to search in form 'ABCD EFGH' (no dash)
       inpList   = file containing a list of files to search for the codes
       outList  = file containing a list of files that match the codes
     """

    if not ( os.path.isfile(numList) ):
       print >>sys.stderr, numList + ' does not exist'
       return
    if not ( os.path.isfile(inpList) ):
       print >>sys.stderr, inpList + ' does not exist'
       return

    print('Reading numbers from:  ' + numList)
    print('Searching files in:  ' + inpList)
    print('Preparing list::  ' + numList)

    f_num = open(numList, "r")
    f_inp = open(inpList, "r")
    f_out = open(outList, "w")

    nseek = 0
    # loop over file containing run codes
    for num in f_num:
        mod_0 = num.rstrip('\n')          # strip end of line
        mod_1 = mod_0.rsplit(' ', 1)       # remove space
        mod_2 = mod_1[0] +'-'+ mod_1[1]    # add dash
        #print('----------------------------------------')
        #print('')
        #print('Searching for:  ' + mod_2)
        # loop over list of files to search for run code matches
        # start at beggning each time
        # could be more clever and go back to the position of last find? 
        f_inp.seek(nseek)
        for line in f_inp:
            found = line.find(mod_2)
            #print('')
            #print('line = ' + line)
            #print('Found = ' + str(found))
            if(found != -1):
                #print('*** Found:  ' + line)
                f_out.write(line)
                # Assuming files are in order
                # the next search carries on from same place
                # minus 10 safety net for duplicates
                if(nseek>9):
                    nseek = f_inp.readline() - 10
                break

    f_num.close()
    f_inp.close()
    f_out.close()
########################################################




