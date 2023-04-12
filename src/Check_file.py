from __init__ import *

def Check_file_type(filepath, outdir):
    if os.path.isfile(filepath):
        file_p = filepath
        file_n = file_p.split('/', -1)
        if file_p[-4:] == ".csv":
            print("-------------------------------------------------------------------------------------------------------------------------------------")
            print(f"**Pass: Your file '{file_n[-1]}' is .CSV file")
            print("-------------------------------------------------------------------------------------------------------------------------------------")
            return(f'{file_p}')
        elif file_p[-5:] == ".xlsx":
            print("-------------------------------------------------------------------------------------------------------------------------------------")
            print(f"**Pass: Your file '{file_n[-1]}' is .XLSX file")
            print("-------------------------------------------------------------------------------------------------------------------------------------")
            print(">> Start to convert .XSLX file to .CSV file <<")
            print("-------------------------------------------------------------------------------------------------------------------------------------")
            df = pd.read_excel(f"{file_p}")
            df.to_csv(f'{outdir}/{file_n[-1][:-5]}.csv', index=False)
            print(">> Converting is alraedy finished! <<")
            print("-------------------------------------------------------------------------------------------------------------------------------------")
            return(f'{outdir}/{file_n[-1][:-5]}.csv')
        else:
            print(f"**Error: Your file '{file_n[-1]}' is NOT .CSV or .XLSX type")
            exit()
    else:
        print(f"**Error: Your file path '{filepath}' is NOT exist")
        exit()

def Check_outdir(outpath):
    if os.path.isdir(outpath):
        print("-------------------------------------------------------------------------------------------------------------------------------------")
        print(f"**Pass: Your outdir '{os.path.dirname(outpath)}' is exist")
        return(os.path.dirname(outpath))
    else:
        print("-------------------------------------------------------------------------------------------------------------------------------------")
        print(f"**Error: Your outdir path '{outpath}' is NOT exist")
        print("-------------------------------------------------------------------------------------------------------------------------------------")
        exit()