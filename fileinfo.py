import pandas as pd
import numpy as np
from pandas import DataFrame,Series
from sklearn.cluster import KMeans
from sklearn.cluster import Birch
#读取文件
datafile = u'E:\\pythondata\\julei.xlsx'#文件所在位置，u为防止路径中有中文名称，此处没有，可以省略
outfile = u'E:\\pythondata\\julei_out.xlsx'#设置输出文件的位置
data = pd.read_excel(datafile)#datafile是excel文件，所以用read_excel,如果是csv文件则用read_csvd = DataFrame(data)d.head()



