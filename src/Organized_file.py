from __init__ import *

def heat(file_, labels):
    df = pd.read_csv(f"{file_}")
    df.columns = df.columns.str.strip().str.upper()
    symbol = []
    expression = []
    sam = []
    label_g = [x.upper() for x in labels]
    
    for col in df.columns:
        if col == 'SYMBOL':
            symbol.append('SYMBOL')
        elif col == 'GENE':
            symbol.append('GENE')
        elif col == 'PROTEIN':
            symbol.append('PROTEIN')
        elif col == 'NAME':
            symbol.append('NAME')
        elif col == 'EXPRESSION':
            expression.append('EXPRESSION')
        elif col == 'EXP':
            expression.append('EXP')
        else:
            sam.append(col)
    
    if label_g != '':
        sample = list(set(sam).difference(label_g))
    else:
        sample = sam
    
    if len(symbol) != 1:
        print("**Error: Your data has NOT SYMBOL or PROTEIN or GENE column")
        exit()

    if len(expression) != 1:
        print("**Error: Your data has NOT EXPRESSION column")
        exit()

    if len(sample) < 1:
        print("**Error: Your data has NOT sample column")
        exit()
    elif len(sample) > 1:
        print("**Error: Your data has sample column more than 1, Please add labels if you have")
        exit()


    new_df = pd.DataFrame()
    new_df['SYMBOL'] = df[f'{symbol[0]}']
    new_df['EXPRESSION'] = df[f'{expression[0]}']
    new_df['SAMPLE'] = df[f'{sample[0]}']
    d = [f"{file_[:-4]}_heatm.csv"]
    for i in label_g:
        new_df[i] = df[i]
        d.append(i)

    new_df.to_csv(f"{d[0]}", index=False)
    print(">> Data for heatmap <<")
    print(new_df)
    print("-------------------------------------------------------------------------------------------------------------------------------------")
    print(">> Finished organized and Converted to DataFrame <<")
    print("-------------------------------------------------------------------------------------------------------------------------------------")
    return(d)

def venn(file_):
    pass

def volc(file_, p_type, inter):
    df = pd.read_csv(f"{file_}")
    df.columns = df.columns.str.strip().str.upper()
    symbol = []
    log2fc = []
    p_val = []
    log_p_val = []
    interest = []

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
        elif col == 'INTEREST':
            interest.append('INTEREST')
        elif col == 'INTERESTGENE':
            interest.append('INTERESTGENE')
        elif col == 'INTEREST_GENE':
            interest.append('INTEREST_GENE')
        elif col == 'INTERESTPROTEIN':
            interest.append('INTERESTPROTEIN')
        elif col == 'INTEREST_PROTEIN':
            interest.append('INTEREST_PROTEIN')
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

    if inter == 'have':
        new_df['INTEREST'] = df[f'{interest[0]}']
    elif inter == 'not_have':
        pass

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

def copy(file_):
    pass

def splr(file_):
    df = pd.read_csv(f"{file_}")
    df.columns = df.columns.str.strip().str.upper()
    chr = []
    pos = []
    SpL = []

    for col in df.columns:
        if col == 'CHROMOSOME':
            chr.append('CHROMOSOME')
        elif col == 'POSITION':
            pos.append('POSITION')
        elif col == 'SHORT_LONG':
            SpL.append('SHORT_LONG')
        else:
            pass

    if len(chr) != 1:
        print("**Error: Your data has NOT Chromosome column")
        exit()
    
    if len(pos) != 1:
        print("**Error: Your data has NOT Position column")
        exit()

    if len(SpL) != 1:
        print("**Error: Your data has NOT Short_Long column")
        exit()

    new_df = pd.DataFrame()
    new_df['CHROMOSOME'] = df[f'{chr[0]}']
    new_df['POSITION'] = df[f'{pos[0]}']
    new_df['SHORT_LONG'] = df[f'{SpL[0]}']

    print(">> Locations of NOT a number (NaN) in your input file <<")
    n = 1
    for index in range(len(new_df['POSITION'])):
        if pd.isna(new_df['CHROMOSOME'][index]) == True:
            print(f'Position {n}: {index + 1}')
            new_df['SHORT_LONG'][index] = float('nan')
            if len(new_df['POSITION'][index]) == len(new_df['POSITION'][index + 1]):
                new_df['CHROMOSOME'][index] = new_df['CHROMOSOME'][index + 1]
            else:
                new_df['CHROMOSOME'][index] = new_df['CHROMOSOME'][index - 1]
            n += 1
        else:
            pass
    if n == 1:
        print("-NOT have NaN")
    print("-------------------------------------------------------------------------------------------------------------------------------------")

    new_df.to_csv(f"{file_[:-4]}_spl.csv", index=False)

    print(">> Data for short per long ratio plot <<")
    print(new_df)
    print("-------------------------------------------------------------------------------------------------------------------------------------")
    print(">> Finished organized and Converted to DataFrame <<")
    print("-------------------------------------------------------------------------------------------------------------------------------------")
    return(f"{file_[:-4]}_spl.csv")

def corr(file_):
    pass

def Organize_file(file_csv, type_, p='', inter='', label=[]):
    if type_ == 'heatmap':
        df = heat(file_csv, labels=label)
        return(df)
    elif type_ == 'vennDiagram':
        venn(file_csv)
        return(df)
    elif type_ == 'volcano':
        df = volc(file_csv, p_type = p, inter=inter)
        return(df)
    elif type_ == 'distribution':
        df = dist(file_csv)
        return(df)
    elif type_ == 'bubble':
        df = bubb(file_csv)
        return(df)
    elif type_ == 'copyNumber':
        df = copy(file_csv)
        return(df)
    elif type_ == 'splRatio':
        df = splr(file_csv)
        return(df)
    elif type_ == 'correlation':
        df = corr(file_csv)
        return(df)
