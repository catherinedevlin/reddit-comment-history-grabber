# -*- coding: utf-8 -*-
import configparser


def get_config():
    config = configparser.ConfigParser()
    config.read("config.ini")
    config.read("config.secret.ini")
    user_agent = "{platform}:{qualified_name}:v{version} (by /u/{author})".format(
        **config["REDDIT"]
    )
    return config
