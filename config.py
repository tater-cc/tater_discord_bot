import argparse
from util.env import Env
from version import __version__

class Config(object):
    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls) -> 'Config':
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            parser = argparse.ArgumentParser(description=f"Graham NANO/BANANO TipBot v{__version__}")
            parser.add_argument('-p', '--prefix', type=str, help='Command prefix for bot commands', default='!')
            parser.add_argument('-l', '--log-file', type=str, help='Log file location', default='/tmp/graham_tipbot.log')
            parser.add_argument('-s', '--status', type=str, help="The bot's 'playing status'", default=None, required=False)
            parser.add_argument('-t', '--token', type=str, help='Discord bot token', required=True)
            parser.add_argument('-u', '--node-url', type=str, help='URL of the node', default='[::1]')
            parser.add_argument('-np', '--node-port', type=int, help='Port of the node', default=7072 if Env.banano() else 7076)
            parser.add_argument('-w', '--wallet', type=str, help='ID of the wallet to use on the node/wallet server', required=True)
            parser.add_argument('--debug', action='store_true', help='Runs in debug mode if specified', default=False)
            options = parser.parse_args()

            # Parse options
            cls.command_prefix = options.prefix
            if len(cls.command_prefix) != 1:
                print("Command prefix can only be 1 character")
                exit(1)
            cls.log_file = options.log_file
            cls.debug = options.debug
            cls.playing_status = f"{cls.command_prefix}help for help" if options.status is None else options.status
            cls.bot_token = options.token
            cls.wallet = options.wallet

            cls.node_url = options.node_url
            cls.node_port = options.node_port
        return cls._instance