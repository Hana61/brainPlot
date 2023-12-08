# brainPlot
BUPT Intelligent Medical Plot homework
北邮智能医学图像处理与系统课程小作业

## 作业要求

你发给我的程序只需要一个函数 bg_overlay_Color('bg.nii.gz', 'Color.nii.gz')，输出的结果为一个图片，类似Result.tif （图片格式不限）.你用你熟悉的语言写，推荐使用 Python或者Matlab，也可以选择其它语言。

附件数据说明:
1. 背景图像为bg.nii.gz，着色图像为 Color.nii.gz；

2. 附件的Data.tif 为上述两个数据的截图显示，左侧为bg.nii.gz，右侧为Color.nii.gz，都只是显示了Z轴方向（人站立时与脊椎垂直的方向）从下往上第46层；Result.tif 为我需要你用程序实现显示的图像效果。
 
3. Result.tif的几个要点：
   (1) 显示多层。我这里显示了19层，从头下方z=16层开始，每3层显示一层；
   (2) bg.nii.gz作为背景，Color.nii.gz作为着色，在Color.nii.gz为0的区域为透明（这样才能看到背景）；
      Color.nii.gz中正值从大到小红色-黄色渐变，负值从小到大蓝色-青色渐变。
   (3) 每个小图左上角的'z=xxmm'为位置，你显示的时候可以简单显示为各层的层数，比如z=16, z=19 ...
   (4)最后一格为Colorbar，标出上述着色的正负两种颜色的阈值，Colorbar上的数值为Color.nii.gz 里正/负值的区间。


提示：
1. 颜色映射表Colormap（或者称Color Table）你可以做一个，也可以直接采用我给你的Colormap.txt文件。
2. Result.tif图片是 4×5 个小图片拼成的，采用subplot方法（Python或Matlab）循环19次容易实现（最后一个单独画），最重要的是每一个子图如何画出来。
3. nii.gz 为NIFTI的压缩格式文件，可以简单解压为.nii格式的NIFTI，NIFTI文件为公开格式文件，可以采用Matlab工具包读写，https://ww2.mathworks.cn/matlabcentral/fileexchange/8797-tools-for-nifti-and-analyze-image?requestedDomain= ； 也可以采用Python工具包读写，网上容易找到。
