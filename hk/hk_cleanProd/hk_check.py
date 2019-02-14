#! /usr/bin/env python





# File list to strip to number code
#str_f_in


#################################
######## Extract numbers ########
#################################


f_in  = open('wcsim_dfc.list', "r")
f_num = open('wcsim_dfc_num.list', "w+")


# read in each line, extract numbers in form: ABCD_EFGH
# write to a new file

for line in f_in:
    mod_0 = line.rstrip('\n')
    mod_1 = mod_0.rstrip('.root')
    mod_2 = mod_1[-9:] + '\n'
    #print(' mod_2 = ' + mod_2 )
    f_num.write(mod_2)

f_in.close()
f_num.close()



#################################
#### Extract missing numbers ####
#################################

f_num  = open('wcsim_dfc_num.list', "r")
f_miss = open('wcsim_dfc_missing.list',"w+")

startRun = 0
endRun   = 100
startSub = 0
endSub   = 600


firstFind = [-9999, -9999]
    

# create a list, where each element is a line from the text file
lines = f_num.readlines()
n_lines = len(lines)

#firstLine = lines[0]
#print('firstLine = ' + firstLine)
#firstLine = firstLine.rstrip('\n')
#print('firstLine = ' , firstLine)
#firstLineNum = firstLine.split('_',1)
#print('firstLineNum[0] = ' + firstLineNum[0]  )
#print('firstLineNum[1] = ' + firstLineNum[1]  )
#
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

num = (  lines[lines_index].rstrip('\n')  ).split('_', 1)

for i in range (startRun, endRun, 1):
    for k in range (startSub, endSub, 1):

        # check if we exhausted list of files 
        # in which case just add to missing list
        if( lines_index  == n_lines  ):  
            code = str(i).zfill(4) +'_'+ str(k).zfill(4)
            f_miss.write( code )
            f_miss.write('\n')
            missing.append( (i,k) )
            missing_index += 1
            continue

        if( (i,k) == ( int(num[0]), int(num[1]) ) ):
            lines_index += 1            
            # only need to update num when we increase the index
            # provided it isnt at the end
            if ( lines_index  != n_lines  ):
                num = (  lines[lines_index].rstrip('\n')  ).split('_', 1)  
        else:
            code = str(i).zfill(4) +'_'+ str(k).zfill(4)
            f_miss.write( code )
            f_miss.write('\n')
            missing.append( (i,k) )
            missing_index += 1
            reread = False

print( missing )


# nes_index  == n_lines  ):
#           indexLine += 1
#        else:
#        if( [i,k] == lines[ indexLine ]
#            firstFind = [i,k]
#            break
#        else:
#            missing[ missing_index ] = (i,j)
#            missing_index += 1
#
#if( firstFind == [-9999, -9999] ):
#    print('WARNING:  No file numbers found in given range !!!' )
#
#for i in range( firstF
##
#
#



        #else:
        #    print('missing ' , i , k )



#              break
#
#if( firstFind == [-9999, -9999] ):
#    print('WARNING:  No numbers match the range !!!')
#
#
#startPos = firstFind
#
#for i in range (startRun, endRun, 1):
#    for k in range (startSub, endSub, 1):
#
#    if(  [i,k] != startPos ):
#        missing = 
#
#    for line in fNumIN:
#        num = line.split(',',1)
# 





#    if 'begin' in line:
#        if countEvents != 0:
#             f.close()
#        countEvents += 1
#        print( 'Event ', countEvents)
#        countFiles += 1
#        filename = 'file' + str(countFiles) + '.dat'
#        f = open(filename, "a+")
#        f.write(line)
#
#    else:
#        f.write(line)
#
#
