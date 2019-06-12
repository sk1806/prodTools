
#/hyperk.org/beam/miniprod/A/1e22_HK_Tochibora_LBL2019Mar/pos/0000_0000-0019_9999/wcs/wcsim_out_pos_1e22_HK_Tochibora_LBL2019Mar_0019_0506.root

#f_i = open("0_pos_wcsim_dfc.list", "r")
#f_o = open("0_pos_wcsim_dfc.num", "w+")

fs = ["0_pos_fitqun_dfc", "2_pos_fitqun_dfc", "4_pos_fitqun_dfc", "4_pos_fitqun_dfc", "8_pos_fitqun_dfc", 
      "0_neg_fitqun_dfc", "2_neg_fitqun_dfc", "4_neg_fitqun_dfc", "4_neg_fitqun_dfc", "8_neg_fitqun_dfc",
      "0_pos_wcsim_dfc" , "2_pos_wcsim_dfc" , "4_pos_wcsim_dfc" , "4_pos_wcsim_dfc" , "8_pos_wcsim_dfc", 
      "0_neg_wcsim_dfc" , "2_neg_wcsim_dfc" , "4_neg_wcsim_dfc" , "4_neg_wcsim_dfc" , "8_neg_wcsim_dfc",
      "0_pos_vect_qm"   , "2_pos_vect_qm"   , "4_pos_vect_qm"   , "4_pos_vect_qm"   , "8_pos_vect_qm",
      "0_neg_vect_qm"   , "2_neg_vect_qm"   , "4_neg_vect_qm"   , "4_neg_vect_qm"   , "8_neg_vect_qm" ]


for name in fs:
    f_i = open(name + ".list", "r")
    f_o = open(name + ".num.score", "w+")

    for line in f_i:
        mod = line.rstrip('\n')
        mod = mod.rstrip('.root') # remove ('.root')
        mod = mod.rstrip('.dat')  # remove ('.dat')
        #print(mod)
        mod = mod[-9:]  # keep last 9 ('ABCD_EFG') 
        #print(mod)
        mod = mod + '\n' # add end of line 
        f_o.write(mod)
        #exit()
