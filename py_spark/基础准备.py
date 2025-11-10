# 演示获取Pyspark的执行环境入库对象： sparkcontext
# 通过sparkcontext对象获取当前pyspark的版本

# 导包
from pyspark import SparkConf, SparkContext
# 创建Sparkconf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
# 基于Sparkconf类对象创建Sparkcontent对象
sc = SparkContext(conf=conf)
# 打印Pyspark的运行版本
print(sc.version)
# 停止pyspark程序
sc.stop()
# spark属于大数据领域，在环境搭建上有问题导致报错的同时我对大数据没兴趣，直接跳过本章