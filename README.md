## 使用爬虫在[虎扑](https://nba.hupu.com/stats/players/pts/1)上爬取NBA球员的比赛数据

### 需要安装的包（调用pip3安装）：requests，parsel和pandas

### 运行方式：进入当前目录的命令提示符cmd，输入 __python NBA01.py__，运行成功后会在当前目录生成名为“NBA_Data”的csv文件

## 遇到的问题及解决方案

+ 生成的csv文件的中文显示乱码  
在生成csv文件的to_csv方法中加入encoding参数“encoding="utf_8_sig”，这可以让Unicode编码标准标识文件应采用哪种格式的编码（Ex：中文-gbk）
+ 
