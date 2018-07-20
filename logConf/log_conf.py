# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author  jakey
# Date 2017-12-01 18:00

import os
import sys
from datetime import date
def logging_conf(log_path):
    return {
        "loggers": {
            "mail": {
                "level": "CRITICAL",
                "propagate": False,
                "handlers": ["mail"]
            },
            "data": {
                "level": "DEBUG",
                "propagate": False,
                "handlers": ["data", "console"]
            }
        },
        "disable_existing_loggers": False,
        "handlers": {
            "data": {
                "formatter": "simple",
                "backupCount": 10,
                "class": "logging.handlers.RotatingFileHandler",
                "maxBytes": 10485760,
                "filename": os.path.join(log_path, "sc-" + date.today().isoformat() + ".log")
            },
            "console": {
                "formatter": "default",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout"
            },
            "mail": {
                "toaddrs": ["wanjie.wu@socialcredits.cn"],
                "mailhost": ["smtp.exmail.qq.com", 25],
                "fromaddr": "it@socialcredits.cn",
                "level": "CRITICAL",
                "credentials": ["it@socialcredits.cn", "cms.2016"],
                "formatter": "mail",
                "class": "logging.handlers.SMTPHandler",
                "subject": "文本情感分析异常"
            }
        },
        "formatters": {
            "default": {
                "datefmt": "%Y-%m-%d %H:%M:%S",
                "format": "%(asctime)s - %(levelname)s - %(module)s.%(name)s : %(message)s"
            },
            "simple": {
                "format": "%(asctime)s - %(levelname)s - %(message)s"
            },
            "mail": {
                "datefmt": "%Y-%m-%d %H:%M:%S",
                "format": "%(asctime)s : %(message)s"
            }
        },
        "version": 1
    }
