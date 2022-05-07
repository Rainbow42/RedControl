from master_node.configure_input import ConfigurationInput
from master_node.controller import ControllerSSHServer

# host = input("Введите host: ")
# username = input("Введите username: ")
# password = input("Введите password: ")
# is_one_start = bool(input("Установлен ли на сервере демон?: "))

host = '192.168.3.15'
username = 'deployer'
password = 'Samsung'
is_one_start = True
key_file = '/Users/antonidamedvedeva/.ssh/id_rsa'
key_password = 'Tonya99'

config = ConfigurationInput(host=host,
                            username=username,
                            password=key_password,
                            is_one_start=is_one_start)

controller = ControllerSSHServer(
    host=config.host,
    username=config.username,
    password=config.password,
    use_keys=True,
    key_file=key_file,
)

controller.command_send('ll')
controller.close()
