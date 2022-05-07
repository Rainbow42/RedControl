from master_node.configure_input import ConfigurationInput
from master_node.controller import ControllerSSHServer

host = input("Введите host: ")
username = input("Введите username: ")
password = input("Введите password: ")
is_one_start = bool(input("Установлен ли на сервере демон?: "))

config = ConfigurationInput(host=host,
                            username=username,
                            password=password,
                            is_one_start=is_one_start)
controller = ControllerSSHServer(**config.__dict__)
# controller.command_send()
