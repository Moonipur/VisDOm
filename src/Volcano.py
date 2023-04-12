from __init__ import *
from Check_file import *
from Organized_file import Organize_file

out_curr = os.getcwd()

Parser = argparse.ArgumentParser(
    prog='Volcano plot',
    description='for visualizing protein or gene expressions by volcano plot.'
)
Parser.add_argument(
    '-i','--input', required=True,
    help='input path (should be .CSV or .XLSX file)'
    )
Parser.add_argument(
    '-o','--outdir', default=out_curr, required=False,
    help='outpur directory (default: current directory)'
    )
Parser.add_argument(
    '--ptype', choices=['P_value','logP_value'], required=True,
    help='type of p-value in input file (for chosing the choice of P_value, this program can calculate -logP_value)'
    )
Parser.add_argument(
    '--log2', default=2.0, required=False, type=float,
    help='log2 FoldChange use for classifying proteins or genes in Up-regulation or Down-regulation (default: 2.0)'
    )
Parser.add_argument(
    '--threshold', default=0.05, required=False, type=float,
    help='threshold are -log10 P-value of signicance level that use to be cut-off line, for easy to use, can input the significance level instead (default: 0.05)'
    )
Parser.add_argument(
    '--splitLine', choices=['yes','no'], default='yes', required=False,
    help='would you like to show baseline for cutting-off dots? it will show in dashed-line form (default: yes)'
    )
Parser.add_argument(
    '--gridLine', choices=['yes','no'], default='yes', required=False,
    help='would you like to show gridline of volcano plot? (default: yes)'
    )
Parser.add_argument(
    '-up','--upReguColor', default='black', required=False, type=str,
    help='color of dots that represent Up-regulation (default: black)'
    )
Parser.add_argument(
    '-down','--downReguColor', default='black', required=False, type=str,
    help='color of dots that represent Down-regulation (default: black)'
    )
Parser.add_argument(
    '--Title', default='Volcano plot', required=False, type=str,
    help='the title of figure (default: Volcano plot)'
    )
Parser.add_argument(
    '--saveFig', default='png', choices=['png','pdf','svg'], required=False, type=str,
    help='type of figure file (default: png)'
    )
args = Parser.parse_args()

def cal_log10P(df_path, outdir):
    df_nonlog = pd.read_csv(df_path)
    logP = []
    for i in range(len(df_nonlog['P_value'])):
        new_p = -math.log10(df_nonlog['P_value'][i])
        logP.append(new_p)
    
    df_nonlog['logP_value'] = logP
    df_nonlog.to_csv(f'{outdir}/logP_temp_file.csv', index=False)
    print('>> Calculation of log10 P_value <<')
    print(df_nonlog)
    print("-------------------------------------------------------------------------------------------------------------------------------------")
    return(f'{outdir}/logP_temp_file.csv')

def class_dot(data_path, log2, threshold):
    df_data = pd.read_csv(data_path)
    signif = -math.log10(threshold)
    class_ = []
    for i in range(len(df_data['logP_value'])):
        if df_data['logP_value'][i] > signif and df_data['Log2FC'][i] > log2:
            dot = 'UP'
            class_.append(dot)
        elif df_data['logP_value'][i] > signif and df_data['Log2FC'][i] < -log2:
            dot = 'DOWN'
            class_.append(dot)
        else:
            dot = 'NOT'
            class_.append(dot)

    df_data['Class'] = class_
    df_data.to_csv(f"{data_path[:-4]}_classDot.csv")
    print('>> Classification of expressions <<')
    print(df_data)
    print("-------------------------------------------------------------------------------------------------------------------------------------")
    re = [f"{data_path[:-4]}_classDot.csv", log2, signif]
    return(re)

def plot_(data_path, up, down, splitLine, grid, title, save_fig, fig_name):
    df_data = pd.read_csv(data_path[0])
    plt.figure(figsize=(100,100), )
    plt.rcParams.update({'font.size': 130})

    ax = plt.axes()

    ax.spines['bottom'].set_linewidth(15)
    ax.spines['left'].set_linewidth(15)
    ax.spines['top'].set_linewidth(15)
    ax.spines['right'].set_linewidth(15)


    groups = ('Up-regulation','Not significant','Down-regulation')
    dot_up = df_data.loc[df_data['Class'] == 'UP']
    dot_down = df_data.loc[df_data['Class'] == 'DOWN']
    dot_not = df_data.loc[df_data['Class'] == 'NOT']

    plt.scatter(x=dot_up['Log2FC'], y=dot_up['logP_value'], marker='o', s=2000, c=up)
    plt.scatter(x=dot_not['Log2FC'], y=dot_not['logP_value'], marker='o', s=2000, c='silver')
    plt.scatter(x=dot_down['Log2FC'], y=dot_down['logP_value'], marker='o', s=2000, c=down)

    x_label = '$log_{2} FoldChange$'
    y_label = '$-log_{10} (P-value)$'

    plt.title(title, fontweight='bold', fontsize=250, pad=250)
    plt.xlabel(x_label, labelpad=100, fontsize=170)
    plt.ylabel(y_label, labelpad=60, fontsize=170)
    plt.legend(groups)

    plt.tick_params(axis='both', direction='out', length=50, width=12)
    if grid == 'yes':
        plt.grid('both', linewidth=10, color='dimgrey', alpha=0.2)
    elif grid == 'no':
        pass
    
    if splitLine == 'yes':
        plt.axhline(y=data_path[2], linestyle='dashed', color='black', linewidth=12)
        plt.axvline(x=data_path[1], linestyle='dashed', color='black', linewidth=12)
        plt.axvline(x=-data_path[1], linestyle='dashed', color='black', linewidth=12)
    elif splitLine == 'no':
        pass

    plt.savefig(fname=f'{fig_name[:-4]}.{save_fig}', format=save_fig)
    print(f">> Successful: Volcano plot is already generated at '{fig_name[:-4]}.{save_fig}'")
    print("-------------------------------------------------------------------------------------------------------------------------------------")

if __name__ == "__main__":
    Head_prog()
    outdir = Check_outdir(args.outdir)
    file = Check_file_type(args.input, outdir)
    file_df_path = Organize_file(file, type_='volcano', p=args.ptype)
    if args.ptype == 'logP_value':
        path_df = class_dot(file_df_path, log2=args.log2, threshold=args.threshold)
        plot_(
            path_df, up=args.upReguColor, down=args.downReguColor, splitLine=args.splitLine, grid=args.gridLine,
            title=args.Title, save_fig=args.saveFig, fig_name=file
        )
    elif args.ptype == 'P_value':
        log10P_df = cal_log10P(file_df_path, outdir)
        path_df = class_dot(log10P_df, log2=args.log2, threshold=args.threshold)
        plot_(
            path_df, up=args.upReguColor, down=args.downReguColor, splitLine=args.splitLine, grid=args.gridLine,
            title=args.Title, save_fig=args.saveFig, fig_name=file
        )