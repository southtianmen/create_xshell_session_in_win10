import shutil
import time
from yl_thread import run_in_threads
from yl_conf import rcf
from yl_xshell import xshell_secret
from yl_csv import init_csvinfo

"""
该脚本适合密码相同的主机也适合不同的密码，批量做操作
"""

def get_time(func):
    def warpper(*args,**kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()
        print("程序运行用时%s秒" % str(end_time-start_time))
        return result
    return warpper

def GetArgs():
    import argparse
    parser = argparse.ArgumentParser(description='input you password')
    parser.add_argument('-p', '--password', required=False,action='store')
    args = parser.parse_args()
    return args

@get_time
def main(filename,ipaddr,ps):
    '''
        如果执行命令的时候没有传递password给程序，则读取csv文件中的密码，
        一旦指定 -p [yourpassword]，就认定你需要创建的session的密码即主机的密码是相同的
        示例 python main.py -p Aa123456

    '''
    try:
        filename = filename + "%s" % ".xsh"
        shutil.copy("template.ini", filename)
        fob = rcf(filename)
        fob.update_conf("CONNECTION", 'Host', ipaddr)
        passwd = xshell_secret().encrypt_string(ps)
        fob.update_conf("CONNECTION:AUTHENTICATION", 'Password', passwd)
    except Exception as e:
        print(str(e))



if  __name__ == "__main__":
    out, ipaddr, pw = init_csvinfo()
    result = GetArgs()
    if result.password:
        pw = [result.password] * len(ipaddr)
    run_in_threads(main, out, ipaddr, pw)
