03_包与模块
库：
    1.标准库：
        time datetime os sys json pickle config logging mock str random csv
    2.第三方库：
        xlrd MYSQLDB PYMYSQL selenium appium requests Django flask scrapy
库安装：
pip install 库名称==版本号

库卸载：
pip uninstall 库名称

离线安装的方式：
1.mysql*.whl
    python install mysql*.whl
2.python setup.py install

mysql:
1.根据链接地址，下载后进行安装应用程序  pip install Python-MySQL
2.下载时注意版本和系统版本

selenium：
selenium IDE selenium-server selenium1.0
webdriver+selenium1.0=selenium2.0   2.53.6  Firefox35   driver==Google
selenium3.0     driver==browser厂商       >Firefox48      ！firebug firepath
selenium3.11 >Firefox54
2016.10

appium  ios android

包和模块
一个py文件就是一个模块
类
函数
变量

模块与模块之间的调用

包与包之间的调用
from package.module import *
