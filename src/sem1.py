# @author: Wayne Yeo <fishnsotong>
# @date:   2017-08-17T04:31:49+08:00
# @email:  wayne.yeo.wei.zhong.2017@vjc.sg
# @last modified by:   fishnsotong
# @last modified time: 2017-08-17T04:51:53+08:00


import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, imshow, axis
from matplotlib.image import imread
import datetime as dt

# read an image
list_of_files = ['../img/0.5.tif', '../img/1.tif', '../img/2.tif', '../img/3.tif','../img/5.tif']

# define and execute image function
def showImagesHorizontally(list_of_files):
    fig = figure()
    number_of_files = len(list_of_files)
    for i in range(number_of_files):
        a=fig.add_subplot(1,number_of_files,i+1)
        image = imread(list_of_files[i])
        imshow(image,cmap='Greys_r')
        axis('off')



showImagesHorizontally(list_of_files)
plt.xlabel("wt. % concentration of surfactant")

now = str(dt.datetime.today())
plt.savefig("../figs/sem1"+ now +".png")

plt.show()
