import logging
import os
from enum import Enum

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


class DeviceHost(Enum):
    LINUX = 'linux'


class ControllerSSHServer:
    """Управление удаленным сервисом по ssh"""

    def __init__(self, host: str, username: str, password: str,
                 port: int = None, secret: str = None, **kwargs):
        self.net_connect = ConnectHandler(
            device_type=DeviceHost.LINUX.value,
            host=host,
            username=username,
            password=password,
            **kwargs,
            session_log="output.txt",
            # port=port,
            # secret=secret
        )

    def command_send(self, command: str):
        output = self.net_connect.send_command(command)
        mess_logg = f"OUTPUT COMMAND: {output}"
        logger.info(mess_logg)

    def close(self):
        self.net_connect.disconnect()
        mess_logg = "DISCONNECT SSH"
        logger.info(mess_logg)
