import csv
import os


def get_csvinfo():
    try:
        filename = [i for i in os.listdir(os.getcwd()) if '.csv' in i][0]
    except Exception as _:
        print("csv file not found or other error in csv file")
    else:
        with open(filename, encoding='utf-8-sig') as f:
            f_csv = csv.DictReader(f)
            newlist = []
            for row in f_csv:
                newdict = {}
                for k, v in row.items():
                    newdict[k.strip()] = v.strip()
                newlist.append(newdict)
            return newlist


def init_csvinfo():
    csv_info = get_csvinfo()
    name_thread_list = []
    ipadd_thread_list = []
    passwd_thread_list = []
    for i in csv_info:
        if "win" not in i['系统']:
            name_thread_list.append(i['名称'])
            ipadd_thread_list.append(i['IP地址'])
            passwd_thread_list.append(i['密码'])
    return name_thread_list, ipadd_thread_list, passwd_thread_list

if __name__ == "__main__":
    # res = init_csvinfo()
    # print(res)
    res = get_csvinfo()
    print(res)