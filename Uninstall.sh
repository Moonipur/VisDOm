# !/bin/bash

if [ -f ~/.bashrc ];
then
    grep -n 'VisualizationOmicsData-VOD/src' ~/.bashrc > .meta_1;
    line=`sed 's/:.*//g' .meta_1| sed -z 's/\n/;/g'`;
    sed 's/.*alias //g' .meta_1 | sed 's/=.*//g' > .meta_2;
    
    sed -i ${line} ~/.bashrc;

    for i in `cat .meta_2`;
    do
        Loc=`find "$(pwd)" -name "${i}.py"`;
        echo ">> ${i}: uninstalling with path ${Loc}";
    done

    rm .meta_1;
    echo "Installation is already finished";
else
    echo "Your .bashrc does NOT exist";
fi