from __init__ import *
from Check_file import *
from Organized_file import Organize_file
from Normalize import *
from Accessory import *

out_curr = os.getcwd()

Parser = argparse.ArgumentParser(
    prog='Short per long ratio plot',
    description='for visualizing the non-normalized or normalized short per long ratio of cfDNA.'
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
    '--Norm', choices=['yes','no'], required=True, default='yse',
    help='would you like to normalize your SpL-ratio (default: yes)'
    )
Parser.add_argument(
    '--chrX', choices=['yes','no'], default='no', required=False,
    help='would you like to show xhromosome X? (default: no)'
    )
Parser.add_argument(
    '--gridLine', choices=['yes','no'], default='yes', required=False,
    help='would you like to show gridline of this plot? (default: yes)'
    )
Parser.add_argument(
    '-gain','--gainColor', default='black', required=False, type=str,
    help='color of gain bin (default: black)'
    )
Parser.add_argument(
    '-loss','--lossColor', default='black', required=False, type=str,
    help='color of loss bin (default: black)'
    )
Parser.add_argument(
    '-normal','--normalColor', default='black', required=False, type=str,
    help='color of dots that represent NOT significant (default: black)'
    )
Parser.add_argument(
    '--Title', default='Volcano plot', required=False, type=str,
    help='the title of figure (default: Volcano plot)'
    )
Parser.add_argument(
    '--Figname', default='', required=False, type=str,
    help='figure name file (default: same as name of input file)'
    )
Parser.add_argument(
    '--saveFig', default='png', choices=['png','pdf','svg'], required=False, type=str,
    help='type of figure file (default: png)'
    )
args = Parser.parse_args()

def Norm():
    pass

def plot_(fig_name, save_fig):
    plt.savefig(fname=f'{fig_name}.{save_fig}', format=save_fig)
    print(f">> Successful: Volcano plot is already generated at '{fig_name}.{save_fig}'")
    print("-------------------------------------------------------------------------------------------------------------------------------------")

if __name__ == "__main__":
    Head_prog()
    outdir = Check_outdir(args.outdir)
    file = Check_file_type(args.input, outdir)
    file_df_path = Organize_file(file, type_='volcano', p=args.ptype, inter=args.interest)
    if args.Figname == '':
        path_df = class_dot(file_df_path, log2=args.log2, threshold=args.threshold)
        plot_(
            path_df, up=args.upReguColor, down=args.downReguColor, non=args.nonSigniColor,
            splitLine=args.splitLine, grid=args.gridLine, top_dot=args.topRankLabel,
            title=args.Title, save_fig=args.saveFig, fig_name=file[:-4], interestG=args.interest
        )
    else:
        path_df = class_dot(file_df_path, log2=args.log2, threshold=args.threshold)
        plot_(
            path_df, up=args.upReguColor, down=args.downReguColor, non=args.nonSigniColor,
            splitLine=args.splitLine, grid=args.gridLine, top_dot=args.topRankLabel,
            title=args.Title, save_fig=args.saveFig, fig_name=f'{outdir}/{args.Figname}', interestG=args.interest
        )
