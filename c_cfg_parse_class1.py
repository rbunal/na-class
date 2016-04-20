'''
8. Write a Python program using ciscoconfparse that parses this config file.
Note, this config file is not fully valid (i.e. parts of the configuration are
missing). The script should find all of the crypto map entries in the file
(lines that begin with 'crypto map CRYPTO') and for each crypto map entry
print out its children.

9. Find all of the crypto map entries that are using PFS group2

10. Using ciscoconfparse find the crypto maps that are not using AES
(based-on the transform set name). Print these entries and their corresponding
transform set name.
'''

from ciscoconfparse import CiscoConfParse

import re

cisco_cfg = CiscoConfParse("cisco_cfg_class1.txt")

crypto_map_line = cisco_cfg.find_objects(r"^crypto map CRYPTO")

for index, value in enumerate(crypto_map_line):
    print value.text
    c_child = crypto_map_line[index].children
    for c in c_child:
        print c.text

print "\nAll crypto map entries that are using PFS group2"

g2 = cisco_cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"group2")
                                   
for g in g2:
   print g.text

print "\nAll crypto map entries that are not using AES"

aes = cisco_cfg.find_objects_wo_child(parentspec=r"^crypto map CRYPTO", childspec=r"AES")
                                    
for a in aes:
   print a.text
   trans = a.all_children
   for t in trans:
       if ("transform-set") in t.text:
              t_name = re.search(r'transform-set (.*)$' , t.text)
              print "transform name %s" % t_name.group(1) 

           

