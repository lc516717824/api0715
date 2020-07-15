"""
自定义日志 系统
"""
import logging
loger = logging.getLogger("cnodeapi")
loger.setLevel(logging.DEBUG)
# 格式化
format = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(funcName)s] %(message)s')

# 文件处理器
fl = logging.FileHandler(filename='C:/Users/51671/PycharmProjects/untitled1/logs/cnodeapi.log',mode='a')
fl.setLevel(logging.DEBUG)
fl.setFormatter(format)
# 控制台输出处理器
sl = logging.StreamHandler()
sl.setFormatter(format)
# 将文件处理器添加到日志中
loger.addHandler(fl)
# 将控制台输出添加到日志中
loger.addHandler(sl)

# loger.info('hello world')