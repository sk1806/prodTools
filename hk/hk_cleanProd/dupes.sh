#!/bin/bash


echo 'wcsim'
sort wcsim_dfc_num.list  | uniq -d  > dupes_wcsim.list
echo 'fitqun'
sort fitqun_dfc_num.list  | uniq -d  >> dupes_fitqun.list

