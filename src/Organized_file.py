from __init__ import *

def heat(file_):
    pass

def venn(file_):
    pass

def volc(file_, p_type):
    df = pd.read_csv(f"{file_}")
    df.columns = df.columns.str.strip().str.upper()
    symbol = []
    log2fc = []
    p_val = []
    log_p_val = []

    for col in df.columns:
        if col == 'LOG2':
            log2fc.append('LOG2')
        elif col == 'LOG2FC':
            log2fc.append('LOG2FC')
        elif col == 'LOGFC':
            log2fc.append('LOGFC')
        elif col == 'SYMBOL':
            symbol.append('SYMBOL')
        elif col == 'GENE':
            symbol.append('GENE')
        elif col == 'PROTEIN':
            symbol.append('PROTEIN')
        elif col == 'NAME':
            symbol.append('NAME')
        elif col == 'P-VALUE':
            p_val.append('P-VALUE')
        elif col == 'PVALUE':
            p_val.append('PVALUE')
        elif col == 'P.VALUE':
            p_val.append('P.VALUE')
        elif col == 'LOGP-VALUE':
            log_p_val.append('LOGP-VALUE')
        elif col == 'LOGPVALUE':
            log_p_val.append('LOGPVALUE')
        elif col == 'LOG10P-VALUE':
            log_p_val.append('LOG10P-VALUE')
        elif col == 'LOG10PVALUE':
            log_p_val.append('LOG10PVALUE')
        elif col == 'LOGP':
            log_p_val.append('LOGP')
        elif col == 'LOG10':
            log_p_val.append('LOG10')
        elif col == 'LOG10P':
            log_p_val.append('LOG10P')
        else:
            pass
    
    if len(symbol) != 1:
        print("**Error: Your data has NOT SYMBOL or PROTEIN or GENE column")
        exit()
    
    if len(log2fc) != 1:
        print("**Error: Your data has NOT Log2FC column")
        exit()

    if p_type == 'P_value':
        if len(log2fc) != 1:
            print("**Error: Your data has NOT P_value column")
            exit()
    elif p_type == 'logP_value':
        if len(log2fc) != 1:
            print("**Error: Your data has NOT LogP_value column")
            exit()
    
    new_df = pd.DataFrame()
    new_df['SYMBOL'] = df[f'{symbol[0]}']
    new_df['Log2FC'] = df[f'{log2fc[0]}']

    if p_type == 'P_value':
        new_df['P_value'] = df[f'{p_val[0]}']
        new_df.to_csv(f"{file_[:-4]}_volc.csv", index=False)
        print(">> Data for volcano plot <<")
        print(new_df)
        print("-------------------------------------------------------------------------------------------------------------------------------------")
        print(">> Finished organized and Converted to DataFrame <<")
        print("-------------------------------------------------------------------------------------------------------------------------------------")
        return(f"{file_[:-4]}_volc.csv")

    elif p_type == 'logP_value':
        new_df['logP_value'] = df[f'{log_p_val[0]}']
        new_df.to_csv(f"{file_[:-4]}_volc.csv", index=False)
        print(">> Data for volcano plot <<")
        print(new_df)
        print("-------------------------------------------------------------------------------------------------------------------------------------")
        print(">> Finished organized and Converted to DataFarme <<")
        print("-------------------------------------------------------------------------------------------------------------------------------------")
        return(f"{file_[:-4]}_volc.csv")


def dist(file_):
    pass

def bubb(file_):
    pass

def box(file_):
    pass

def copy(file_):
    pass

def splr(file_):
    pass

def Organize_file(file_csv, type_, p):
    if type_ == 'heatmap':
        heat(file_csv)
    elif type_ == 'vennDiagram':
        venn(file_csv)
    elif type_ == 'volcano':
        df = volc(file_csv, p_type = p)
        return(df)
    elif type_ == 'distribution':
        dist(file_csv)
    elif type_ == 'bubble':
        bubb(file_csv)
    elif type_ == 'boxplot':
        box(file_csv)
    elif type_ == 'copyNumber':
        copy(file_csv)
    elif type_ == 'splRatio':
        splr(file_csv)
    else:
        print(f"**Error: The type '{type_}' is Unrecognized!")
        exit()