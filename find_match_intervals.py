import sys
import re
import random

if len(sys.argv) != 4:
    print "Usage: python condense_interval.py [hotspot] [nothot] [outfile]"
    sys.exit()

hotspot = sys.argv[1]
nothot = sys.argv[2]
outfile = sys.argv[3]


with open(hotspot, "r")as fin, open(hotspot, "r")as fin1, open(outfile, "w")as fout:

    col = {}
    for l0 in fin:
        if l0.startswith("#"):
            
            l0 = re.sub("#", "", l0)
            l0 = l0.strip()
            
            col_names =l0.split("\t")
        else:
            continue

    i = 0
    for name in col_names:
        if name not in col:
            col[name] = i
            i = i+1



    hot = 0
    for l1 in fin1:
        if l1.startswith("#"):
            l1 = re.sub("#", "", l1)
            fout.write("hotspot"+"\ttype\t"+l1)
        
        else:
            hot = hot + 1
            l1 = l1.strip()
            
            hotspot = l1.split("\t")

            SegDup_ct = hotspot[col["SegDup_ct"]]
            SegDup_bp = hotspot[col["SegDup_bp"]]
            SNP = hotspot[col["SNP"]]
            GC = hotspot[col["GC"]]
            gene_ct = hotspot[col["gene_ct"]]
            gene_bp = hotspot[col["gene_bp"]]
            exon_bp = hotspot[col["exon_bp"]]
            DNA_ct = hotspot[col["DNA_ct"]]
            DNA_bp = hotspot[col["DNA_bp"]]
            LTR_ct = hotspot[col["LTR_ct"]]
            LTR_bp = hotspot[col["LTR_bp"]]
            LINE_ct = hotspot[col["LINE_ct"]]
            LINE_bp = hotspot[col["LINE_bp"]]
            SINE_ct = hotspot[col["SINE_ct"]]
            SINE_bp = hotspot[col["SINE_bp"]]




            with open(nothot, "r")as fin2:
                list1 = []
                for line in fin2:
                    if not line.startswith("#"):
                        non_hotspot = line.split("\t")
                        
                        hotspot_value = float(exon_bp)
                        non_hotspot_value = float(non_hotspot[col["exon_bp"]])
                    
                        if hotspot_value == 0 :
                            if non_hotspot_value == 0:
                                list1.append(line)
                      
                      
                        else:
                            if abs((hotspot_value - non_hotspot_value)/hotspot_value) < 0.1:
                                list1.append(line)
            
 
                list2 = []
                for line in list1:
                    if not line.startswith("#"):
                        non_hotspot = line.split("\t")
                        
                        hotspot_value = float(GC)
                        non_hotspot_value = float(non_hotspot[col["GC"]])
                        
                        if hotspot_value == 0 :
                            if non_hotspot_value == 0:
                                list2.append(line)
                    
                        else:
                            if abs((hotspot_value - non_hotspot_value)/hotspot_value) < 0.1:
                                list2.append(line)


                list3 = []
                for line in list2:
                    if not line.startswith("#"):
                        non_hotspot = line.split("\t")
                        
                        hotspot_value = float(SegDup_bp)
                        non_hotspot_value = float(non_hotspot[col["SegDup_bp"]])
                        
                        if hotspot_value == 0 :
                            if non_hotspot_value == 0:
                                list3.append(line)
                    
                        else:
                            if abs((hotspot_value - non_hotspot_value)/hotspot_value) < 0.1:
                                list3.append(line)




                list4 = []
                for line in list3:
                    if not line.startswith("#"):
                        non_hotspot = line.split("\t")
                        
                        hotspot_value = float(SNP)
                        non_hotspot_value = float(non_hotspot[col["SNP"]])
                        
                        if hotspot_value == 0 :
                            if non_hotspot_value == 0:
                                list4.append(line)
                    
                        else:
                            if abs((hotspot_value - non_hotspot_value)/hotspot_value) < 0.1:
                                list4.append(line)
         

                list5 = []
                for line in list4:
                    if not line.startswith("#"):
                        non_hotspot = line.split("\t")
                        
                        hotspot_value = float(SINE_bp)
                        non_hotspot_value = float(non_hotspot[col["SINE_bp"]])
                        
                        if hotspot_value == 0 :
                            if non_hotspot_value == 0:
                                list5.append(line)
                    
                        else:
                            if abs((hotspot_value - non_hotspot_value)/hotspot_value) < 0.1:
                                list5.append(line)

                list6 = []
                for line in list5:
                    if not line.startswith("#"):
                        non_hotspot = line.split("\t")
                
                        hotspot_value = float(LINE_bp)
                        non_hotspot_value = float(non_hotspot[col["LINE_bp"]])
                        
                        if hotspot_value == 0 :
                            if non_hotspot_value == 0:
                                list6.append(line)
                
                        else:
                            if abs((hotspot_value - non_hotspot_value)/hotspot_value) < 0.1:
                                list6.append(line)
        
                list7 = []
                for line in list6:
                    if not line.startswith("#"):
                        non_hotspot = line.split("\t")
                        
                        hotspot_value = float(DNA_bp)
                        non_hotspot_value = float(non_hotspot[col["DNA_bp"]])
                        
                        if hotspot_value == 0 :
                            if non_hotspot_value == 0:
                                list7.append(line)
                    
                        else:
                            if abs((hotspot_value - non_hotspot_value)/hotspot_value) < 0.1:
                                list7.append(line)




                if len(list7) < 1:
                    print str(hot) + "\t" + "doesn't have enough match"
                else:
                    fout.write(str(hot) + "\thotspot\t" + l1.strip() + "\n")

                    match = random.sample(list7, 1)
                    for item in match:
                        fout.write(str(hot) + "\thotspot_match\t" + item)







                        
    
