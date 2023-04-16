# Visualization of Omics Data (VOD)

  Suite-software packages of python script for visualizing omics data.
  Currently, our packages is developing and only volcano plots and heatmaps are available. 

# Requirement of packages

  Python (version >= 3.10)
  
  Pandas, Numpy, Matplotlib, Openpyxl, Scipy
  
# Initial installation step by step

  Create conda environment
    
    conda create -n VOD python=3.10
    
    conda activate VOD
    
    pip install pandas numpy matplotlib openpyxl scipy
    
  Download VOD suite-packages with git-clone
    
    git clone https://github.com/Moonipur/VisualizationOmicsData-VOD.git
    
    cd VisualizationOmicsData-VOD/
    
    chmod +x *.sh
    
    ./Install.sh
    
    source ~/.bashrc
    
  Check and update the latest version

    cd VisualizationOmicsData-VOD/
    
    chmod -x *.sh
    
    git pull origin main
    
    chmod +x *.sh
    
    ./Update.sh
    
    source ~/.bashrc
    
# Developed by

    Songphon Sutthitthasakul (Moonipur)

    e-mail: songphon_sutthittha@cmu.ac.th
  
  **Please contact with us if you have any problem with our program
