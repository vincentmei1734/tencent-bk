# -*- coding: utf-8 -*-
"""
用于本地开发环境的全局配置
"""
from settings import APP_ID
from default import *

# ===============================================================================
# 数据库设置, 本地开发数据库设置
# # ===============================================================================
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',  # 默认用mysql
#         'NAME': APP_ID,                        # 数据库名 (默认与APP_ID相同)
#         'USER': 'test',                            # 你的数据库user
#         'PASSWORD': '123456',                        # 你的数据库password
#         'HOST': '',                            # 开发的时候，使用localhost
#         'PORT': '',                            # 默认3306
#     },
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}