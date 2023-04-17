from __init__ import *
from Check_file import *
from Organized_file import Organize_file
from Normalize import *
from Accessory import *

out_curr = os.getcwd()

Parser = argparse.ArgumentParser(
    prog='Heatmap',
    description='for visualizing protein or gene expressions by heatmap.'
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
    '-l','--label', default='', required=False, nargs='*', type=str,
    help='labels of addition colomns (default: non-label)'
    )
Parser.add_argument(
    '-d','--dendrogram', default='both', required=False, choices=['both', 'left', 'top', 'no'], type=str,
    help='whould you like to show dendrogram with heatmap? (default: both)'
    )
Parser.add_argument(
    '-dCol','--dendroColor', default='black', required=False, type=str,
    help='color of dendrogram line (default: black)'
    )
Parser.add_argument(
    '--Norm', default='noNorm', required=False, choices=['z-score', 'minMax', 'noNorm'], type=str,
    help='whould you like to normalize matrix? (default: no)'
    )
Parser.add_argument(
    '-lC','--labelC', default='level of expression', required=False, type=str,
    help='x-axis label (default: level of expression)'
    )
Parser.add_argument(
    '-mCol','--matrixColor', default='magma', required=False, type=str,
    help='color of matrixes inside heatmap (default: magma)'
    )
Parser.add_argument(
    '-cLab','--colorLabel', default='no', required=False, type=str, nargs='+',
    help='color pallettes of color labels, can input color follow the sort of first alphabet (example: "sex:{f}emale-{m}ale" ->  "sex:yellow-brown") (default: no)'
    )
Parser.add_argument(
    '--Title', default='Heatmap', required=False, type=str,
    help='the title of figure (default: Heatmap), if you do NOT want to show, you can input (no)'
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


def matrix_(data_path, annota, new):
    df_data = pd.read_csv(data_path[0])
    dict_val = [value for key, value in annota.items()]
    new_df = pd.DataFrame()
    if len(new) != 0:
        df_data['EXPRESSION'] = new
    elif len(new) == 0:
        pass
    for sample in dict_val[2]:
        get_df = df_data.loc[df_data['SAMPLE'] == sample]
        get_df.reset_index(drop=True, inplace=True)
        new_df[f'{sample}'] = get_df['EXPRESSION']

    new_df.to_csv(f'{data_path[0][:-10]}_matrix.csv', index=False)
    print(f">> Convert datafram to matrix <<")
    print(new_df)
    print("-------------------------------------------------------------------------------------------------------------------------------------")
    return(f'{data_path[0][:-10]}_matrix.csv')

def annotate_(data_path):
    df_data = pd.read_csv(data_path[0])
    list_label = data_path[1:]
    dict_label = {'Num_symbol': len(pd.unique(df_data['SYMBOL']))}
    dict_label['Symbol'] = pd.unique(df_data['SYMBOL'])
    dict_label['Sample'] = pd.unique(df_data['SAMPLE'])
    dict_sample = {}
    for col in list_label:
        dict_label[f'{capital_fromUp(col)}'] = pd.unique(df_data[f'{col}']).tolist()
        for i in dict_label['Sample']:
            df_g = df_data.loc[df_data['SAMPLE'] == i]
            lab_col = pd.unique(df_g[f'{col}']).tolist()
            if len(lab_col) != 1:
                print(f'**Error: Your label "{col}" is wrong')
            else:
                pass

            if f'{i}' not in dict_sample:
                dict_sample[f'{i}'] = []
            else:
                pass
            dict_sample[f'{i}'].append(lab_col[0])

    print(f">> Annotate and count all type of labels <<")
    for key, value in dict_label.items():
        print(f'{key}: {value}')
    print("-------------------------------------------------------------------------------------------------------------------------------------")
    print(f">> Classify individual sample information <<")
    for key, value in dict_sample.items():
        print(f'{key}: {value}')
    print("-------------------------------------------------------------------------------------------------------------------------------------")
    return(dict_label, dict_sample)

def scale_(data_list):
    exp_list = data_list
    min_ = round(min(exp_list), 0)
    max_ = round(max(exp_list), 0)
    scale_major = []
    scale_minor = []

    if abs(max_ - min_) % 2 == 0:
        scale_major.append(min_)
        scale_minor.append(min_)
        median_ = abs(max_ - min_) / 2
        if median_ % 2 == 0:
            half_median = median_ / 2
            scale_major.append(min_ + half_median)
            scale_major.append(min_ + median_)
            scale_major.append(max_ - half_median)
            scale_major.append(max_)
            scale_minor.append(min_ + half_median)
            scale_minor.append(min_ + median_)
            scale_minor.append(max_ - half_median)
            scale_minor.append(max_)

        elif median_ % 2 != 0:
            n = 3
            while n != 5:
                if median_ % n == 0:
                    cent = median_ / n
                    if n == 3:
                        scale_major.append(min_ + cent*2)
                        scale_major.append(max_ - cent*2)
                        scale_major.append(max_)
                        scale_minor.append(min_ + cent*2)
                        scale_minor.append(max_ - cent*2)
                        scale_minor.append(max_)
                    elif n == 5:
                        scale_major.append(min_ + cent*3)
                        scale_major.append(max_ - cent*3)
                        scale_major.append(max_)
                        scale_minor.append(min_ + cent*3)
                        scale_minor.append(max_ - cent*3)
                        scale_minor.append(max_)
                    break
                else:
                    pass
                n += 2

    elif abs(max_ - min_) % 2 != 0:
        scale_major.append(min_)
        scale_minor.append(min_)
        n = 3
        while n != 7:
            if abs(max_ - min_) % n == 0:
                cent = abs(max_ - min_) / n
                if n == 3:
                    scale_major.append(min_ + cent)
                    scale_major.append(min_ + cent*2)
                    scale_major.append(max_)
                    scale_minor.append(min_ + cent)
                    scale_minor.append(min_ + cent*2)
                    scale_minor.append(max_)
                elif n == 5:
                    scale_major.append(min_ + cent)
                    scale_major.append(min_ + cent*2)
                    scale_major.append(min_ + cent*3)
                    scale_major.append(min_ + cent*4)
                    scale_major.append(max_)
                    scale_minor.append(min_ + cent)
                    scale_minor.append(min_ + cent*2)
                    scale_minor.append(min_ + cent*3)
                    scale_minor.append(min_ + cent*4)
                    scale_minor.append(max_)
                elif n == 7:
                    scale_major.append(min_ + cent*2)
                    scale_major.append(min_ + cent*5)           
                    scale_major.append(max_)
                    scale_minor.append(min_ + cent*2)
                    scale_minor.append(min_ + cent*5)           
                    scale_minor.append(max_)
                break
            else:
                pass
            n += 2

        if len(scale_major) == 1 and len(scale_minor) == 1:
            two_decim = round(abs(max_ - min_), 0)
            if two_decim % 2 == 0:
                mid = two_decim / 2
                scale_major.append(min_ + mid)
                scale_major.append(max_)
                scale_minor.append(min_ + mid)
                scale_minor.append(max_)
            else:
                mid = (two_decim + 1) / 2
                scale_major.append(min_ + mid)
                scale_major.append(max_)
                scale_minor.append(min_ + mid)
                scale_minor.append(max_)
        else:
            pass

    scale_major_n = [(change_decim_021(i)) for i in scale_major]
    scale_minor_n = [(change_decim_021(j)) for j in scale_minor]
    print(f">> Normalize of expression score <<")
    print(f'Minimum values: {min_}')
    print(f'Maximum values: {max_}')
    print(f'Scale of expression score: {scale_minor_n}')
    print("-------------------------------------------------------------------------------------------------------------------------------------")
    return(scale_major_n, scale_minor_n)

def plot_(data_path, fig_name, save_fig, title, annot, xlab, mCol, cBar, dendro, label, scale):
    dict_figure = {
        'heat1': [
            [100,100], 
            [0.1, 0.1, 0.7, 0.7],
            [0.875, 0.65, 0.05, 0.15]
        ],
        'heat1_den': [
            [100,100], 
            [0.075, 0.775, 0.15, 0.05], 
            [0.3, 0.7, 0.6, 0.2], 
            [0.1, 0.1, 0.2, 0.6], 
            [0.3, 0.1, 0.6, 0.6]
        ],
        'heat2': [
            [100,120],

            [0.1, 0.1, 0.7, 0.65],

            [0.875, 0.7, 0.05, 0.15], 

            [[0.85, 0.55, 0.10, 0.1],
            [0.1, 0.77, 0.7, 0.03]],

            [[0.85, 0.55, 0.10, 0.1],
            [0.1, 0.77, 0.7, 0.03],
            [0.85, 0.4, 0.10, 0.1],
            [0.1, 0.81, 0.7, 0.03]],

            [[0.85, 0.55, 0.10, 0.1],
            [0.1, 0.77, 0.7, 0.02],
            [0.85, 0.4, 0.10, 0.1],
            [0.1, 0.8, 0.7, 0.02],
            [0.85, 0.25, 0.10, 0.1],
            [0.1, 0.83, 0.7, 0.02]]
        ],
        'heat2_den': [
            [120,120], 

            [],

            [],

            [[1], 
            [1], 
            [1],
            [1]],

            [[1], 
            [1], 
            [1],
            [1]],

            [[1], 
            [1], 
            [1],
            [1]]
        ]
    }

    key = [key for key, i in dict_figure.items()]
    fig_prop = [i for key, i in dict_figure.items()]

    def heat_1(data, fig_prop, figname, type_, title, xlab, ColMat, dict_lab, scale_):
        df_data = pd.read_csv(data)
        mat = np.shape(df_data)

        D = df_data.to_numpy()

        fig = plt.figure(figsize=(fig_prop[0][0],fig_prop[0][1]))
        plt.rcParams.update({'font.size': 130})
        if title != 'no':
            fig.suptitle(title, y=0.90, fontweight='bold', fontsize=300)
        else:
            pass
        plt.rcParams['lines.linewidth'] = 10

        idx1 = [indx for indx in range(mat[0])]
        idx2 = [indx for indx in range(mat[1])]
        D = D[idx1, :]
        D = D[:, idx2]

        #Heatmap
        Hmap = fig.add_axes(fig_prop[1])
        Hmap.spines['bottom'].set_linewidth(15)
        Hmap.spines['left'].set_linewidth(15)
        Hmap.spines['top'].set_linewidth(15)
        Hmap.spines['right'].set_linewidth(15)


        im = Hmap.matshow(D, aspect='auto', origin='lower', cmap=ColMat)
        Hmap.set_xticks([])
        Hmap.set_yticks([])

        sam = [dict_lab['Sample'][i] for i in idx2]
        Hmap.set_xticks(range(mat[1]))
        Hmap.set_xticklabels(sam, minor=False)
        Hmap.xaxis.set_label_position('bottom')
        Hmap.xaxis.tick_bottom()
        plt.xticks(rotation=25)

        sym = [dict_lab['Symbol'][j] for j in idx1]
        Hmap.set_yticks(range(mat[0]))
        Hmap.set_yticklabels(sym, minor=False)
        Hmap.yaxis.set_label_position('left')
        Hmap.yaxis.tick_left()

        plt.yticks(fontsize=50)
        plt.tick_params('both', pad=30)

        plt.rcParams["axes.linewidth"] = 10
        Cbar = fig.add_axes(fig_prop[2])
        norm = mpl.colors.Normalize(vmin=scale_[0][0], vmax=scale_[0][-1], clip=True)
        fig.colorbar(mappable=sm(norm=norm, cmap=ColMat), cax=Cbar, orientation='vertical')
        Cbar.set_xticks([])
        Cbar.set_yticks([])

        plt.tick_params('y', pad=30, length=30, width=10)
        Cbar.set_yticks(scale_[1])
        Cbar.set_yticklabels(scale_[0], minor=False)
        Cbar.yaxis.set_label_position('right')
        Cbar.yaxis.tick_right()
        Cbar.set_title(xlab, fontsize=120, fontweight='bold', pad=100)
        Cbar.get_title('center')

        plt.xticks(fontsize=100)

        plt.savefig(fname=f'{figname}.{type_}', format=type_)

    def heat_1den(data, fig_prop, figname, type_, title, xlab, ColMat, dict_lab, dend, scale_):
        df_data = pd.read_csv(data)
        mat = np.shape(df_data)

        D = df_data.to_numpy()

        fig = plt.figure(figsize=(fig_prop[0][0],fig_prop[0][1]))
        plt.rcParams.update({'font.size': 130})
        if title != 'no':
            fig.suptitle(title, y=0.95, fontweight='bold', fontsize=300)
        else:
            pass
        plt.rcParams['lines.linewidth'] = 10

        if dend == 'both':
            #Left-dendrogram
            Lden = fig.add_axes(fig_prop[3])
            Lden.spines['bottom'].set_linewidth(0)
            Lden.spines['left'].set_linewidth(0)
            Lden.spines['top'].set_linewidth(0)
            Lden.spines['right'].set_linewidth(0)
            Y = sch.linkage(D, method='centroid')
            Z1 = sch.dendrogram(Y, orientation='left', color_threshold=0, above_threshold_color='k')
            Lden.set_xticks([])
            Lden.set_yticks([])

            #Top-dendrogram
            Tden = fig.add_axes(fig_prop[2])
            Tden.spines['bottom'].set_linewidth(0)
            Tden.spines['left'].set_linewidth(0)
            Tden.spines['top'].set_linewidth(0)
            Tden.spines['right'].set_linewidth(0)
            Y = sch.linkage(D.T, method='single')
            Z2 = sch.dendrogram(Y, color_threshold=0, above_threshold_color='k')
            Tden.set_xticks([])
            Tden.set_yticks([])
        
            idx1 = Z1['leaves']
            idx2 = Z2['leaves']
            D = D[idx1, :]
            D = D[:, idx2]

        elif dend == 'left':
            #Left-dendrogram
            Lden = fig.add_axes(fig_prop[3])
            Lden.spines['bottom'].set_linewidth(0)
            Lden.spines['left'].set_linewidth(0)
            Lden.spines['top'].set_linewidth(0)
            Lden.spines['right'].set_linewidth(0)
            Y = sch.linkage(D, method='centroid')
            Z1 = sch.dendrogram(Y, orientation='left', color_threshold=0, above_threshold_color='k')
            Lden.set_xticks([])
            Lden.set_yticks([])

            idx1 = Z1['leaves']
            idx2 = [indx for indx in range(mat[1])]
            D = D[idx1, :]

        elif dend == 'top':
            #Top-dendrogram
            Tden = fig.add_axes(fig_prop[2])
            Tden.spines['bottom'].set_linewidth(0)
            Tden.spines['left'].set_linewidth(0)
            Tden.spines['top'].set_linewidth(0)
            Tden.spines['right'].set_linewidth(0)
            Y = sch.linkage(D.T, method='single')
            Z2 = sch.dendrogram(Y, color_threshold=0, above_threshold_color='k')
            Tden.set_xticks([])
            Tden.set_yticks([])

            idx1 = [indx for indx in range(mat[0])]
            idx2 = Z2['leaves']
            D = D[:, idx2]
        

        #Heatmap
        Hmap = fig.add_axes(fig_prop[4])
        Hmap.spines['bottom'].set_linewidth(15)
        Hmap.spines['left'].set_linewidth(15)
        Hmap.spines['top'].set_linewidth(15)
        Hmap.spines['right'].set_linewidth(15)


        im = Hmap.matshow(D, aspect='auto', origin='lower', cmap=ColMat)
        Hmap.set_xticks([])
        Hmap.set_yticks([])

        sam = [dict_lab['Sample'][i] for i in idx2]
        Hmap.set_xticks(range(mat[1]))
        Hmap.set_xticklabels(sam, minor=False)
        Hmap.xaxis.set_label_position('bottom')
        Hmap.xaxis.tick_bottom()
        plt.xticks(rotation=25)

        sym = [dict_lab['Symbol'][j] for j in idx1]
        Hmap.set_yticks(range(mat[0]))
        Hmap.set_yticklabels(sym, minor=False)
        Hmap.yaxis.set_label_position('right')
        Hmap.yaxis.tick_right()

        plt.yticks(fontsize=50)
        plt.tick_params('both', pad=30)

        plt.rcParams["axes.linewidth"] = 10
        Cbar = fig.add_axes(fig_prop[1])
        norm = mpl.colors.Normalize(vmin=scale_[0][0], vmax=scale_[0][-1], clip=True)
        fig.colorbar(mappable=sm(norm=norm, cmap=ColMat), cax=Cbar, orientation='horizontal')
        Cbar.set_xticks([])
        Cbar.set_yticks([])

        plt.tick_params('x', pad=30, length=30, width=10)
        Cbar.set_xticks(scale_[1])
        Cbar.set_xticklabels(scale_[0], minor=False)
        Cbar.xaxis.set_label_position('bottom')
        Cbar.xaxis.tick_bottom()
        Cbar.set_title(xlab, fontsize=125, fontweight='bold', pad=100)
        Cbar.get_title('center')

        plt.xticks(fontsize=100)

        plt.savefig(fname=f'{figname}.{type_}', format=type_)

    def heat_2(data, fig_prop, figname, type_, title, xlab, ColMat, dict_lab, cBar, scale_):
        df_data = pd.read_csv(data)
        mat = np.shape(df_data)
        dict_mat_lab = dict_lab[1]
        dict_lab = dict_lab[0]

        D = df_data.to_numpy()

        fig = plt.figure(figsize=(fig_prop[0][0],fig_prop[0][1]))
        plt.rcParams.update({'font.size': 130})
        if title != 'no':
            fig.suptitle(title, y=0.93, fontweight='bold', fontsize=300)
        else:
            pass
        plt.rcParams['lines.linewidth'] = 10

        idx1 = [indx for indx in range(mat[0])]
        idx2 = [indx for indx in range(mat[1])]
        D = D[idx1, :]
        D = D[:, idx2]

        #Heatmap
        Hmap = fig.add_axes(fig_prop[1])
        Hmap.spines['bottom'].set_linewidth(15)
        Hmap.spines['left'].set_linewidth(15)
        Hmap.spines['top'].set_linewidth(15)
        Hmap.spines['right'].set_linewidth(15)


        im = Hmap.matshow(D, aspect='auto', origin='lower', cmap=ColMat)
        Hmap.set_xticks([])
        Hmap.set_yticks([])

        sam = [dict_lab['Sample'][i] for i in idx2]
        Hmap.set_xticks(range(mat[1]))
        Hmap.set_xticklabels(sam, minor=False)
        Hmap.xaxis.set_label_position('bottom')
        Hmap.xaxis.tick_bottom()
        plt.xticks(rotation=25)

        sym = [dict_lab['Symbol'][j] for j in idx1]
        Hmap.set_yticks(range(mat[0]))
        Hmap.set_yticklabels(sym, minor=False)
        Hmap.yaxis.set_label_position('left')
        Hmap.yaxis.tick_left()

        plt.yticks(fontsize=50)
        plt.tick_params('both', pad=30)

        plt.rcParams["axes.linewidth"] = 10
        Cbar = fig.add_axes(fig_prop[2])
        norm = mpl.colors.Normalize(vmin=scale_[0][0], vmax=scale_[0][-1], clip=True)
        fig.colorbar(mappable=sm(norm=norm, cmap=ColMat), cax=Cbar, orientation='vertical')
        Cbar.set_xticks([])
        Cbar.set_yticks([])

        plt.tick_params('y', pad=30, length=30, width=10)
        Cbar.set_yticks(scale_[1])
        Cbar.set_yticklabels(scale_[0], minor=False)
        Cbar.yaxis.set_label_position('right')
        Cbar.yaxis.tick_right()
        Cbar.set_title(xlab, fontsize=120, fontweight='bold', pad=100)
        Cbar.get_title('center')

        plt.xticks(fontsize=100)

        new_dict_lab = dict_lab
        keys = ['Symbol', 'Sample', 'Num_symbol']
        for r in keys:
            del new_dict_lab[r]

        D_lab = gen_onehot(dict_mat_lab, new_dict_lab)
        dict_pallettes = gen_pallettes(cBar, new_dict_lab)
        k_li = [k.lower() for k, c in dict_pallettes.items()]
        c_li = [c for k, c in dict_pallettes.items()]

        if len(new_dict_lab) == 1:
            clab = mpl.colors.ListedColormap(c_li[0])
            #lab_1
            plt.rcParams["axes.linewidth"] = 0
            lab_1 = fig.add_axes(fig_prop[3][0])
            lab_1.set_title(k_li[0], fontsize=120, fontweight='bold', pad=100)
            lab_1.get_title('center')
            patch = []
            for indx, i in enumerate(sorted(new_dict_lab[k_li[0].capitalize()])):
                red_patch = mpl.patches.Patch(color=c_li[0][indx], label=i)
                patch.append(red_patch)

            plt.legend(handles=patch, loc='upper center', fontsize=120)
            lab_1.set_xticks([])
            lab_1.set_yticks([])

            #clab_1
            plt.rcParams["axes.linewidth"] = 10
            clab_1 = fig.add_axes(fig_prop[3][1])
            f = clab_1.matshow(D_lab, aspect='auto', origin='lower', cmap=clab)
            clab_1.set_xticks([])
            clab_1.set_yticks([])


        elif len(new_dict_lab) == 2:
            clab = (mpl.colors.ListedColormap(c_li[0]), mpl.colors.ListedColormap(c_li[1]))
            #lab_1
            plt.rcParams["axes.linewidth"] = 0
            lab_1 = fig.add_axes(fig_prop[4][0])
            lab_1.set_title(k_li[0], fontsize=120, fontweight='bold', pad=100)
            lab_1.get_title('center')
            patch = []
            for indx, i in enumerate(sorted(new_dict_lab[k_li[0].capitalize()])):
                red_patch = mpl.patches.Patch(color=c_li[0][indx], label=i)
                patch.append(red_patch)

            plt.legend(handles=patch, loc='upper center', fontsize=120)
            lab_1.set_xticks([])
            lab_1.set_yticks([])

            #clab_1
            plt.rcParams["axes.linewidth"] = 10
            clab_1 = fig.add_axes(fig_prop[4][1])
            f_1 = clab_1.matshow([D_lab[0, :]], aspect='auto', origin='lower', cmap=clab[0])
            clab_1.set_xticks([])
            clab_1.set_yticks([])

            #lab_2
            plt.rcParams["axes.linewidth"] = 0
            lab_2 = fig.add_axes(fig_prop[4][2])
            lab_2.set_title(k_li[1], fontsize=120, fontweight='bold', pad=100)
            lab_2.get_title('center')
            patch = []
            for indx, i in enumerate(sorted(new_dict_lab[k_li[1].capitalize()])):
                red_patch = mpl.patches.Patch(color=c_li[1][indx], label=i)
                patch.append(red_patch)

            plt.legend(handles=patch, loc='upper center', fontsize=120)
            lab_2.set_xticks([])
            lab_2.set_yticks([])

            #clab_2
            plt.rcParams["axes.linewidth"] = 10
            clab_2 = fig.add_axes(fig_prop[4][3])
            f_2 = clab_2.matshow([D_lab[1, :]], aspect='auto', origin='lower', cmap=clab[1])
            clab_2.set_xticks([])
            clab_2.set_yticks([])
            
        elif len(new_dict_lab) == 3:
            clab = (mpl.colors.ListedColormap(c_li[0]), mpl.colors.ListedColormap(c_li[1]), mpl.colors.ListedColormap(c_li[2]))
            #lab_1
            plt.rcParams["axes.linewidth"] = 0
            lab_1 = fig.add_axes(fig_prop[5][0])
            lab_1.set_title(k_li[0], fontsize=120, fontweight='bold', pad=100)
            lab_1.get_title('center')
            patch = []
            for indx, i in enumerate(sorted(new_dict_lab[k_li[0].capitalize()])):
                red_patch = mpl.patches.Patch(color=c_li[0][indx], label=i)
                patch.append(red_patch)

            plt.legend(handles=patch, loc='upper center', fontsize=120)
            lab_1.set_xticks([])
            lab_1.set_yticks([])

            #clab_1
            plt.rcParams["axes.linewidth"] = 10
            clab_1 = fig.add_axes(fig_prop[5][1])
            f_1 = clab_1.matshow([D_lab[0, :]], aspect='auto', origin='lower', cmap=clab[0])
            clab_1.set_xticks([])
            clab_1.set_yticks([])

            #lab_2
            plt.rcParams["axes.linewidth"] = 0
            lab_2 = fig.add_axes(fig_prop[5][2])
            lab_2.set_title(k_li[1], fontsize=120, fontweight='bold', pad=100)
            lab_2.get_title('center')
            patch = []
            for indx, i in enumerate(sorted(new_dict_lab[k_li[1].capitalize()])):
                red_patch = mpl.patches.Patch(color=c_li[1][indx], label=i)
                patch.append(red_patch)

            plt.legend(handles=patch, loc='upper center', fontsize=120)
            lab_2.set_xticks([])
            lab_2.set_yticks([])

            #clab_2
            plt.rcParams["axes.linewidth"] = 10
            clab_2 = fig.add_axes(fig_prop[5][3])
            f_2 = clab_2.matshow([D_lab[1, :]], aspect='auto', origin='lower', cmap=clab[1])
            clab_2.set_xticks([])
            clab_2.set_yticks([])

            #lab_3
            plt.rcParams["axes.linewidth"] = 0
            lab_3 = fig.add_axes(fig_prop[5][4])
            lab_3.set_title(k_li[2], fontsize=120, fontweight='bold', pad=100)
            lab_3.get_title('center')
            patch = []
            for indx, i in enumerate(sorted(new_dict_lab[k_li[2].capitalize()])):
                red_patch = mpl.patches.Patch(color=c_li[2][indx], label=i)
                patch.append(red_patch)

            plt.legend(handles=patch, loc='upper center', fontsize=120)
            lab_3.set_xticks([])
            lab_3.set_yticks([])

            #clab_3
            plt.rcParams["axes.linewidth"] = 10
            clab_3 = fig.add_axes(fig_prop[5][5])
            f_3 = clab_3.matshow([D_lab[2, :]], aspect='auto', origin='lower', cmap=clab[2])
            clab_3.set_xticks([])
            clab_3.set_yticks([])
            
        elif len(new_dict_lab) > 3:
            print('**Error: Sorry, now on our program can add 3 labels as maximum')
            exit()

        plt.savefig(fname=f'{figname}.{type_}', format=type_)

    def heat_2den(data, fig_prop, figname, type_, title, xlab, ColMat, dict_lab, dend, cBar, scale_):
        print('**Error: Sorry, this mode is still developing. now is unavailable !!')
        exit()


    if dendro == 'no':
        if label == '':
            heat_1(data_path, fig_prop=fig_prop[0], figname=fig_name, type_=save_fig, title=title, xlab=xlab, ColMat=mCol, dict_lab=annot[0], scale_=scale_)
        elif label != '' and cBar != 'no':
            heat_2(data_path, fig_prop=fig_prop[2], figname=fig_name, type_=save_fig, title=title, xlab=xlab, ColMat=mCol, dict_lab=annot, cBar=cBar, scale_=scale)
        else:
            print('**Error: You chose label mode, please input labels color')
            exit()
    else:
        if label == '':
            heat_1den(data_path, fig_prop=fig_prop[1], figname=fig_name, type_=save_fig, title=title, xlab=xlab, ColMat=mCol, dict_lab=annot[0], dend=dendro, scale_=scale)
        elif label != '' and cBar != 'no':
            heat_2den(data_path, fig_prop=fig_prop[3], figname=fig_name, type_=save_fig, title=title, xlab=xlab, ColMat=mCol, dict_lab=annot, dend=dendro, cBar=cBar, scale_=scale)
        else:
            print('**Error: You chose label mode, please input labels color')
            exit()

    print(f">> Successful: Heatmap is already generated at '{fig_name}.{save_fig}'")
    print("-------------------------------------------------------------------------------------------------------------------------------------")

if __name__ == "__main__":
    Head_prog()
    outdir = Check_outdir(args.outdir)
    file = Check_file_type(args.input, outdir)
    file_df_path = Organize_file(file, type_='heatmap', label=args.label)
    annota = annotate_(file_df_path)
    data_df = pd.read_csv(file_df_path[0])
    data_li = data_df['EXPRESSION'].values.tolist()

    if args.Norm == 'z-score':
        df_data = Zscore(data_list=data_li)
        scale = scale_(data_list=df_data)
        matrix = matrix_(file_df_path, annota[0], new=df_data)

    elif args.Norm == 'minMax':
        df_data = MinMax(data_list=data_li)
        scale = scale_(data_list=df_data)
        matrix = matrix_(file_df_path, annota[0], new=df_data)

    elif args.Norm == 'noNorm':
        scale = scale_(data_list=data_li)
        matrix = matrix_(file_df_path, annota[0], new=[])
        
    if args.Figname == '':
        plot_(
            matrix, annot=annota, fig_name=file[:-4], save_fig=args.saveFig, title=args.Title,
            xlab=args.labelC, mCol=args.matrixColor, cBar=args.colorLabel, dendro=args.dendrogram, label=args.label, scale=scale,
        )
    else:
        plot_(
            matrix, annot=annota, fig_name=f'{outdir}/{args.Figname}', save_fig=args.saveFig, title=args.Title,
            xlab=args.labelC, mCol=args.matrixColor, cBar=args.colorLabel, dendro=args.dendrogram, label=args.label, scale=scale
        )