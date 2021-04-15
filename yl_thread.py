#!/usr/bin/env python3
# coding:utf-8
# author:yl

from multiprocessing import cpu_count
from concurrent.futures import ThreadPoolExecutor


def run_in_threads(fn, *args, **kwargs):
    """
    将任务放在线程中并发执行，以提高工作效率
    线程池中最大活动线程数 = cpu核心数*2
    :param fn: 函数名
    :return: args: 函数fn的参数列表
    :param kwargs: 通过传递 timeout=N 来指定线程池超时时间
    :return: 返回 fn的返回值list
    :raise: concurrent.futures._base.TimeoutError
    """
    max_thread = cpu_count() * 2
    executor = ThreadPoolExecutor(max_thread)
    future = executor.map(fn, *args, **kwargs)
    return list(future)

