# !/bin/bash

module=(Bubble CopyNumber Correlation Distribution Heatmap SpL_ratio VennDiagram Volcano)

if [ -f ~/.bashrc ];
then
    for i in ${module[@]}; 
    do
        Loc=`find "$(pwd)" -name "${i}.py"`;
        d="/alias ${i}='python ${Loc}'/d";
        sed -i $d ~/.bashrc;
    done
    echo "Installation is already finished";
else
    echo "Your .bashrc does NOT exist";
fi