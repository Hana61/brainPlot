import nibabel as nib
from matplotlib import pyplot as plt
import matplotlib
from matplotlib.colors import Normalize, ListedColormap
import numpy as np


def bg_overlay_Color(bg_path, Color_path, output_path='result.png', Colormap_path=None, default_Colormap='viridis'):  
    
    bg = nib.load(bg_path)
    Color = nib.load(Color_path)

    z = bg.dataobj.shape[2]
    defaultCmap = default_Colormap  # 暂时仅支持ListedColormap
    invisibleThreshould = 0.09  # 要显示为透明的0的邻域范围

    # 检视3D图
    # OrthoSlicer3D(bg.dataobj).show()
    # OrthoSlicer3D(Color.dataobj).show()

    # 设置Colormap归一化方法，使其范围对应最小值到最大值
    vmin = Color.dataobj[:, :, :].min()
    vmax = Color.dataobj[:, :, :].max()
    norm = Normalize(vmin=vmin, vmax=vmax)

    # 按行读取txt文件，自定义Colormap
    if Colormap_path != None:
        colors = []
        for line in open("Colormap.txt"): 
            color = list(map(float, line.strip('\n').split('\t')))
            colors.append(color)
        customCmap = ListedColormap(colors=colors)
    else:
        customCmap = plt.get_cmap(defaultCmap).copy()
        
    # 阈值之内的色彩段alpha设为0，之外的设为1
    for i, color in enumerate(customCmap.colors):
        color.append(0 if 
                     256/(vmax - vmin)*(-invisibleThreshould - vmin) < 
                     i <= 
                     256/(vmax - vmin)*(invisibleThreshould - vmin) 
                     else 1)

    loc = 1  # 子图在图中的位置
    for i in range(15, z - 19, 3):
        # 横截面
        bg_arr = np.flip(bg.dataobj[:, :, i].T)
        Color_arr = np.flip(Color.dataobj[:, :, i].T)

        plt.subplot(4, 5, loc)

        plt.imshow(bg_arr, cmap='gray', zorder=0)  # 在下方
        plt.imshow(Color_arr, cmap='viridis' if Colormap_path == None else customCmap, zorder=1, norm=norm)  # 在上方
        plt.text(2., 107., 'z=%d' % (i), fontsize=7, color='white', weight='bold', zorder=2)

        # 隐藏坐标轴
        plt.axis('off')
        loc += 1
    
    # 在最后一张子图边上设置Colorbar
    plt.colorbar(matplotlib.cm.ScalarMappable(norm=norm, cmap='viridis' if Colormap_path == None else customCmap), 
                 orientation='vertical', 
                 pad=0, 
                 aspect=6,
                 shrink=2.5,
                 ticks=[vmin, -invisibleThreshould, invisibleThreshould, vmax],
                 ax=plt.subplot(4, 5, loc),
                 spacing='proportional')
    plt.axis('off')  # 隐藏坐标轴
    plt.tight_layout()  # 紧凑视图
    plt.subplots_adjust(wspace=0, hspace=0)  # 去掉子图间距
    plt.savefig(output_path)
    plt.show()
    pass

if __name__ == '__main__':
    bg_overlay_Color(bg_path='bg.nii', 
                     Color_path='Color.nii', 
                     output_path='result.png', 
                     Colormap_path='Colormap.txt', 
                    #  default_Colormap='viridis'  # 若未指定自定义Colormap路径则需要指定默认Colormap
                     )
