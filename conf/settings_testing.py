# -*- coding: utf-8 -*-
"""
用于测试环境的全局配置
"""
from settings import APP_ID


# ===============================================================================
# 数据库设置, 测试环境数据库设置
# ===============================================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 默认用mysql
        'NAME': APP_ID,                        # 数据库名 (默认与APP_ID相同)
        'USER': 'test',                            # 你的数据库user
        'PASSWORD': '123456',                        # 你的数据库password
        'HOST': '10.0.1.102',                            # 开发的时候，使用localhost
        'PORT': '',                            # 默认3306
    },
}
