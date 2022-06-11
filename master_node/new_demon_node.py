import logging
import os
import subprocess

from master_node.controller import ControllerSSHServer

LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')
log_level = getattr(logging, LOG_LEVEL, logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(levelname)s [%(asctime)s] %(name)s: '
                                       '%(message)s', '%d-%m-%Y %H:%M:%S'))

logger = logging.getLogger("InitializationDemonNode")
logger.setLevel(log_level)
logger.addHandler(handler)
handler.setLevel(log_level)


class CommandsDemonNode:
    @staticmethod
    def create_root_dir() -> str:
        return 'mkdir redcontrol'

    @staticmethod
    def create_settings_dir() -> str:
        return 'mkdir redcontrol/settings'

    @staticmethod
    def create_tmp_dir() -> str:
        return 'mkdir redcontrol/tmp'

    @staticmethod
    def create_bin_dir() -> str:
        return 'mkdir redcontrol/bin'

    @staticmethod
    def create_projects_dir():
        return 'mkdir redcontrol/projects'

    @staticmethod
    def create_database() -> str:
        return 'docker-compose up -d'

    @staticmethod
    def cd_dir_bin() -> str:
        return 'cd redcontrol/bin'

    @staticmethod
    def rsync_files(file_out, ip, username, dir_to) -> str:
        """Синхронизация файлов с компьютера на котором запущен мастер
        для удаленного сервиса"""
        # rsync -avz ./docker/ deployer@192.168.3.15:/home/deployer
        rsync = 'rsync -rlpgoDvc ' + file_out + ' ' \
                + username + '@' + ip + ':' + dir_to
        return rsync


class InitializationDemonNode:
    """Предоставляет список команд для инициализации демона
    на удаленном сервере"""

    def __init__(self, controller: ControllerSSHServer):
        self.controller = controller

    def create_dir(self):
        """Создаем рабочую директорию для работы программы"""
        init_dir = [
            CommandsDemonNode.create_root_dir(),
            CommandsDemonNode.create_projects_dir(),
            CommandsDemonNode.create_settings_dir(),
            CommandsDemonNode.create_tmp_dir(),
            CommandsDemonNode.create_bin_dir(),
        ]
        self.controller.commands_send(init_dir)
        self.controller.command_send('chmod 777 redcontrol')
        mess_logg = "INIT WORK DIR"
        logger.info(mess_logg)

    def install_docker_compose(self, ver: str = '1.29.2'):
        docker_install = f'sudo curl -L ' \
                         f'"https://github.com/docker/compose/releases/' \
                         f'download/{ver}/docker-compose-$(uname -s)-' \
                         f'$(uname -m)" -o /usr/local/bin/docker-compose'
        dir_chmod_docker_compose = 'sudo chmod +x /usr/local/bin/docker-compose'
        self.controller.commands_send([docker_install,
                                       dir_chmod_docker_compose])

    def create_database(self, ip: str, username: str):
        """
        1. Передадим конфиги для разворачивания бд для этого ПО
        2. Поднимем дб в контейнере
        """
        self.controller.command_send('cd')
        self.controller.command_send('chmod 777 redcontrol/bin')
        self.controller.command_send(CommandsDemonNode.cd_dir_bin(),
                                     strip_prompt=False,
                                     strip_command=False,
                                     expect_string='~/redcontrol/bin')
        self.controller.command_send('mkdir docker')
        self.controller.command_send('mkdir docker/scripts')

        self.controller.command_send('chmod 777 docker')
        self.controller.command_send('chmod 777 docker/scripts')

        try:
            self.controller.command_send('docker ps -a')
        except:
            self.install_docker_compose()
        pwd = subprocess.check_output('pwd')
        docker = str(pwd.decode('utf-8')).rstrip() + '/docker/'

        os.system(CommandsDemonNode.rsync_files(docker, ip, username, 'redcontrol/bin/docker/'))
        self.up_docker()

    def up_docker(self):
        self.controller.command_send('docker-compose -f docker/docker-compose.yml up', read_timeout=100)
        self.controller.command_send('docker-compose -f docker/docker-compose.yml ps -a')

