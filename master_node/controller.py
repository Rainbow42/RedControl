import logging
import os

from netmiko import ConnectHandler


LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')
log_level = getattr(logging, LOG_LEVEL, logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(levelname)s [%(asctime)s] %(name)s: '
                                       '%(message)s', '%d-%m-%Y %H:%M:%S'))

logger = logging.getLogger("ControllerSSHServer")
logger.setLevel(log_level)
logger.addHandler(handler)
handler.setLevel(log_level)


class ControllerSSHServer:
    """Управление удаленным сервисом по ssh"""

    def __init__(self, host: str, username: str, password: str,
                 port: int = None, secret: str = None):
        self.net_connect = ConnectHandler(
            host=host,
            username=username,
            password=password,
            port=port,
            secret=secret
        )

    def command_send(self, command: str):
        output = self.net_connect.send_command(command)
        mess_logg = f"OUTPUT COMMAND: {output}"
        logger.info(mess_logg)
