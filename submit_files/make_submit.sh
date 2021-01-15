#!/bin/bash
input="list_sf"
outputFile="submitJobs_14Jan21.sh"
echo "#!/bin/bash" >> $outputFile

while IFS= read -r line
do
    echo "$line"
    line2=${line#"submit_"}
    line3=${line2%".py"}
    echo "farmoutRandomSeedJobs $line3 50000 500 /afs/hep.wisc.edu/home/ms/monoHiggs_signal_sample/CMSSW_10_2_18 /afs/hep.wisc.edu/home/ms/monoHiggs_signal_sample/CMSSW_10_2_18/src/gensim_config_files/$line --vsize-limit=10000 --site-requirements='OpSysAndVer == \"CENTOS7\"' " >> $outputFile
    printf "\n" >> $outputFile
    #sed 's/test_fragment_py_LHE_GEN_SIM.py/'${line}'/' $outputFile >> $outputFile

done < "$input"
