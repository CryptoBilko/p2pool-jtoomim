import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


#P2P_PREFIX = 'f9beb4d9'.decode('hex') # disk magic and old net magic
P2P_PREFIX = 'e4e8e9e5'.decode('hex') # new net magic
P2P_PORT = 5556
ADDRESS_VERSION = 0
RPC_PORT = 6666
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            
            (yield bitcoind.rpc_getblockchaininfo())['chain'] == 'main'
        ))
SUBSIDY_FUNC = lambda height: 50*100000000 >> (height + 1)//210000
POW_FUNC = data.hash256
BLOCK_PERIOD = 600 # s
SYMBOL = 'DEM'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Bitcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Bitcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.eMark'), 'eMark.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://185.194.142.165:3001/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://185.194.142.165:3001/ext/getaddress/'
TX_EXPLORER_URL_PREFIX = 'http://185.194.142.165:3001/tx/'
SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**32 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 0.001e8
