


count = 0
with open('gridpack_list_gg') as gpfile:
    for gp in gpfile:
        #output file to write the result to
        count += 1
        gp = gp.strip()
        print(gp)
        sampleName = gp.split('/')[-1]
        sampleName = sampleName.split('_slc6')[0]
        print(sampleName)
        fin = open("../monoHiggsTauTau_2017GS.py", "rt")
        fout = open("../gensim_config_files/"+sampleName+".py", "wt")
        #for each line in the input file
        for line in fin:
            #read replace the string and write to output file
            if 'substitute_path_to_grid_pack' in line:
                print('found line')
                fout.write(line.replace('substitute_path_to_grid_pack', gp ))
            else:
                fout.write(line)
                #close input and output files
        fout.close()
        fin.close()
        


