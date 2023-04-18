# !/bin/bash

module=(Bubble CopyNumber Correlation Distribution Heatmap SpL_ratio VennDiagram Volcano)

if [ -f ~/.bashrc ];
then
    for i in ${module[@]}; 
    do
        Loc=`find "$(pwd)" -name "${i}.py"`;
        echo ">> ${i}: installing with path ${Loc}";
        echo "alias ${i}='python ${Loc}'" >> ~/.bashrc;
    done
    echo "Installation is already finished";

else
    echo "Your .bashrc does NOT exist";
fi