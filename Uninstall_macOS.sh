# !/bin/zsh

if [ -f ~/.zshrc ];
then
    grep -n 'VisualizationOmicsData-VOD/src' ~/.zshrc > .meta_1;
    line=`sed 's/:.*//g' .meta_1| sed -e 's/\n/d;/g'`;
    sed 's/.*alias //g' .meta_1 | sed 's/=.*//g' > .meta_2;
    
    sed -i ${line} ~/.zshrc;

    for i in `cat .meta_2`;
    do
        Loc=`find "$(pwd)" -name "${i}.py"`;
        echo ">> ${i}: uninstalling with path ${Loc}";
    done

    rm .meta_1 .meta_2;
    echo "Installation is already finished";
    
else
    echo "Your .bashrc does NOT exist";
fi
