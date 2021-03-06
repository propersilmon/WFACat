# -*- coding: utf-8 -*-

"""
WFACatPro.main
~~~~~~~~~~~~~~~~~~~
This is a main module.
"""


import json
import os

from modules import version


if __name__ == '__main__':
    version.print_version_info()
    print('You could use \'help\' command to get help!')
    print('If appear Python ERROR, please config correct configuration!')
    print('Warning! If you want store data to MySQL, you must set MySQL default charset is utf8mb4 first!!!')
    print(
        'Change MySQL chartset: find my.ini, change [mysql] and [mysqld], then change to utf8mb4, restart service.')
    print('')

    # 创建存放数据的文件夹
    if not os.path.exists('./WFACat_data'):
        os.makedirs('./WFACat_data')

    """
    第一次运行没有配置文件，会自动初始化一个 config.json
    """
    if not os.path.isfile('./WFACat_data/config.json'):
        with open('./WFACat_data/config.json', 'w', encoding='utf-8') as init_config_info_json_file:
            privacy_url_local = ' '
            person_name_local = ' '
            each_follower_count_local = 200
            set_level_local = 2
            db_host_local = 'localhost'
            db_port_local = '3306'
            db_user_local = 'root'
            db_user_password_local = '12345'
            db_charset_local = 'utf8mb4'

            init_config_info = {
                'PRIVACY_URL': privacy_url_local,
                'PERSON_NAME': person_name_local,
                'EACH_FOLLOWER_COUNT': each_follower_count_local,
                'SET_LEVEL': set_level_local,
                'DB_HOST': db_host_local,
                'DB_PORT': db_port_local,
                'DB_USER': db_user_local,
                'DB_USER_PASSWORD': db_user_password_local,
                'DB_CHARSET': db_charset_local}

            init_config_info_handle = json.dumps(init_config_info)
            init_config_info_json_file.write(init_config_info_handle)

    """
    读取配置
    """
    with open('./WFACat_data/config.json', 'r', encoding='utf-8') as config_file:
        config_file_handle = json.loads(config_file.read())
        PRIVACY_URL = config_file_handle['PRIVACY_URL']
        PERSON_NAME = config_file_handle['PERSON_NAME']

    """
    每次运行，判断是否进行了配置
    """
    if PRIVACY_URL == ' ':
        print('No configuration! Please setting! using command \'conf\' !')
    elif PERSON_NAME == ' ':
        print('No configuration! Please setting! using command \'conf\' !')

    """
    接受命令并运行对应的模块
    """
    this_file_path = os.path.abspath(__file__)[:-7]

    while True:
        cmd = input('> ')
        if cmd == 'help':
            os.system("\"" + this_file_path + "modules/help.py\"")
        elif cmd == 'conf':
            os.system("\"" + this_file_path + "modules/settings.py\"")
        elif cmd == 'get':
            os.system("\"" + this_file_path + "modules/get_data.py\"")
        elif cmd == 'tocsv':
            os.system("\"" + this_file_path + "modules/analysis_to_csv.py\"")
        elif cmd == 'tomysql':
            os.system("\"" + this_file_path + "modules/analysis_to_mysql.py\"")
        elif cmd == 'mysqld':
            os.system("\"" + this_file_path + "modules/mysql_query.py\"")
        elif cmd == 'tool':
            os.system("\"" + this_file_path + "modules/tools.py\"")
        elif cmd == 'fix':
            os.system("\"" + this_file_path + "modules/fixed.py\"")
        elif cmd == 'quit':
            exit('Bye ~')
