# -*- encoding: utf-8 -*-

"""
@version: 0.1
@author: Clark.wang
@contact: Clark.wang@liulishuo.com
@file: log_manager.py
@time: 09/11/2017 2:50 PM
used to take care of all the manager
TODO: record all the traceback information
"""

import logging
import os
import time
import sys


def self_hook_function(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    sys.__excepthook__(exc_type, exc_value, exc_traceback)
    get_traceback_logger().error("Traceback", exc_info=(exc_type, exc_value, exc_traceback))
    return


sys.excepthook = self_hook_function


import conf
from data_processing import BColors


CI_TAG = "CI"
DEV_TAG = "DEV"
TRACEBACK_TAG = "TRACEBACK"

DEFAULT_LOG_DIR ='/opt/resource/data/log'


def get_logging_level(tag):
    default_level = logging.INFO
    # default_level = logging.ERROR

    if conf.CI_MODE:
        if tag == CI_TAG:
            return default_level
        else:
            return logging.INFO

    return default_level


def get_console_handler(mono=False):
    if mono:
        console_format = '[%(asctime)s %(name)s]' + '[%(levelname)s]' + ' %(message)s'
    else:
        console_format = BColors.BCYAN + '[%(asctime)s %(name)s]' + BColors.ENDC + \
                         BColors.OKBLUE + '[%(levelname)s]' + BColors.ENDC + ' %(message)s'
    console = logging.StreamHandler(sys.stdout)
    console.setFormatter(logging.Formatter(console_format))
    return console


def get_file_handler(tag='', traceback=False):
    dir_file = DEFAULT_LOG_DIR
    if not os.path.exists(dir_file):
        try:
            os.mkdir(dir_file)
        except:
            dir_file = './test_log'
            if not os.path.exists(dir_file):
                os.mkdir(dir_file)

    prefix = dir_file + '/log_err-' if traceback else dir_file + '/log-'
    logging_file = prefix + time.strftime('%Y-%m-%d-%H%M%S',time.gmtime(time.time() + 28800)) + '.log'
    file_format = '%(asctime)s {0} : %(levelname)s :%(message)s'.format(tag)

    log_file = logging.FileHandler(logging_file, mode='w', encoding='UTF8')
    log_file.setFormatter(logging.Formatter(file_format))
    return log_file


CI_LOGGER = None
DEBUG_LOGGER = None
TRACEBACK_LOGGER = None


def get_ci_logger(mono=False):
    global CI_LOGGER
    if CI_LOGGER:
        return CI_LOGGER

    # initial CI_LOGGER
    CI_LOGGER = logging.getLogger(CI_TAG)
    logging_level = get_logging_level(CI_TAG)
    CI_LOGGER.setLevel(logging_level)

    console = get_console_handler(mono=mono)
    CI_LOGGER.addHandler(console)

    if conf.OPEN_LOG_FILE:
        file_handler = get_file_handler(CI_TAG)
        CI_LOGGER.addHandler(file_handler)
    return CI_LOGGER


def get_debug_logger(mono=False):
    global DEBUG_LOGGER
    if DEBUG_LOGGER:
        return DEBUG_LOGGER

    # initial Debug_LOGGER
    DEBUG_LOGGER = logging.getLogger(DEV_TAG)
    logging_level = get_logging_level(DEV_TAG)
    DEBUG_LOGGER.setLevel(logging_level)

    console = get_console_handler(mono=mono)
    DEBUG_LOGGER.addHandler(console)
    return DEBUG_LOGGER


def get_traceback_logger():
    global TRACEBACK_LOGGER
    if TRACEBACK_LOGGER:
        return TRACEBACK_LOGGER

    TRACEBACK_LOGGER = logging.getLogger(TRACEBACK_TAG)
    TRACEBACK_LOGGER.setLevel(logging.ERROR)
    file_handler = get_file_handler(TRACEBACK_TAG, traceback=True)
    TRACEBACK_LOGGER.addHandler(file_handler)
    return TRACEBACK_LOGGER


if __name__ == '__main__':
    import threading
    class mythread(threading.Thread):
        def run(self):
            ci = get_ci_logger()
            ci.info("test...")
            return

    threads = []
    for i in xrange(10):
        threads.append(mythread())

    for thre in threads:
        thre.start()

    get_ci_logger().info("xxxxxx")
