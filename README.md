# Datasets

Some datasets for recommendation

### Amazon
<http://jmcauley.ucsd.edu/data/amazon/>  
从该网站上下载数据集到本地，有`ratings only`和`reviews`两种，分别放在对应文件夹下（具体请看源代码，并可自行修改），然后运行
```
python run.py
```
`ratings only`使用`ratings`，`reviews`使用`reviews`  
通过`info`下的`info.csv`选中想要转换的数据集
```
python goncf.py --dataset name
```
将数据集转换为`NCF`形式

