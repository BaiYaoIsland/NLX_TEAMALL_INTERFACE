import logging
import os
import datetime

class UserLog():
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        # # 控制台输出日志
        consle = logging.StreamHandler()
        self.logger.addHandler(consle)
        self.logger.debug("info")
        # 文件名字
        # 获取当前文件所在目录
        base_dir = os.path.dirname(os.path.abspath(__file__))
        print("This is base_dir :",base_dir)

        # 定义Log输出路径
        log_dir = os.path.join(base_dir, "logs")
        print("This is log_dir :",log_dir)

        # 定义Log名称格式
        log_file = datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
        print("This is log_file name :",log_file)

        # 定义完整路径目录
        log_name = log_dir + "/" + log_file
        print("This is laster log_name :",log_name)


        # 定义文件输出日志
        file_handle = logging.FileHandler(log_name, 'a', encoding='utf-8')

        # 定义日志输出的内容包括时间、文件名、函数名、行数、等级、信息
        formatter = logging.Formatter(
            '%(asctime)s %(filename)s----> %(funcName)s %(levelno)s %(levelname)s -----%(message)s'
        )

        file_handle.setFormatter(formatter)
        self.logger.addHandler(file_handle)
        self.logger.debug("teste1234")

        self.logger.removeHandler(file_handle)
        file_handle.close()

    def get_log(self):
        return self.logger

if __name__ == '__main__':
    user = UserLog()
    log = user.get_log()
    log.debug('test')