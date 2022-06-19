from master_node.configure_input import ConfigurationInput
from master_node.controller import ControllerSSHServer
from master_node.new_demon_node import InitializationDemonNode


host = '192.168.3.15'
username = 'deployer'
password = '****'
is_one_start = True
key_file = '/Users/antonidamedvedeva/.ssh/id_rsa'
key_password = '****'

https_git = 'https://gitlab.com/service-analytics/discovery-failure.git'
token = '****'

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

InitializationDemonNode(controller).create_dir()
InitializationDemonNode(controller).create_database(host, username)
InitializationDemonNode(controller).git_clone()
controller.close()
