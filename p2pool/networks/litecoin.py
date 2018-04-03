from p2pool.bitcoin import networks

PARENT = networks.nets['litecoin']
SHARE_PERIOD = 15 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 3 # blocks
IDENTIFIER = 'e037d5b8c6923410'.decode('hex')
PREFIX = '7208c1a53ef629b0'.decode('hex')
P2P_PORT = 9326
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 9327
BOOTSTRAP_ADDRS = 'forre.st:9338 vps.forre.st:9338 litecoin-p2pool.com:9338 95.211.21.103:9338 37.229.117.57:9338 66.228.48.21:9338 180.169.60.179:9338 112.84.181.102:9338 74.214.62.115:9338 209.141.46.154:9338 78.27.191.182:9338 66.187.70.88:9338 88.190.223.96:9338 78.47.242.59:9338 158.182.39.43:9338 180.177.114.80:9338 216.230.232.35:9338 94.231.56.87:9338 62.38.194.17:9338 82.67.167.12:9338 183.129.157.220:9338 71.19.240.182:9338 216.177.81.88:9338 109.106.0.130:9338 113.10.168.210:9338 218.22.102.12:9338 85.69.35.7:54396 201.52.162.167:9338 95.66.173.110:8331 109.65.171.93:9338 95.243.237.90:9338 208.68.17.67:9338 87.103.197.163:9338 101.1.25.211:9338 144.76.17.34:9338 209.99.52.72:9338 198.23.245.250:9338 46.151.21.226:9338 66.43.209.193:9338 59.127.188.231:9338 178.194.42.169:9338 85.10.35.90:9338 110.175.53.212:9338 98.232.129.196:9338 116.228.192.46:9338 94.251.42.75:9338 195.216.115.94:9338 24.49.138.81:9338 61.158.7.36:9338 213.168.187.27:9338 37.59.10.166:9338 72.44.88.49:9338 98.221.44.200:9338 178.19.104.251:9338 87.198.219.221:9338 85.237.59.130:9310 218.16.251.86:9338 151.236.11.119:9338 94.23.215.27:9338 60.190.203.228:9338 176.31.208.222:9338 46.163.105.201:9338 198.84.186.74:9338 199.175.50.102:9338 188.142.102.15:9338 202.191.108.46:9338 125.65.108.19:9338 15.185.107.232:9338 108.161.131.248:9338 188.116.33.39:9338 78.142.148.62:9338 69.42.217.130:9338 213.110.14.23:9338 185.10.51.18:9338 74.71.113.207:9338 77.89.41.253:9338 69.171.153.219:9338 58.210.42.10:9338 174.107.165.198:9338 50.53.105.6:9338 116.213.73.50:9338 83.150.90.211:9338 210.28.136.11:9338 86.58.41.122:9338 70.63.34.88:9338 78.155.217.76:9338 68.193.128.182:9338 198.199.73.40:9338 193.6.148.18:9338 188.177.188.189:9338 83.109.6.82:9338 204.10.105.113:9338 64.91.214.180:9338 46.4.74.44:9338 98.234.11.149:9338 71.189.207.226:9338 crypto.office-on-the.net siberia.mine.nu'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-ltc'
VERSION_CHECK = lambda v: None if 100400 <= v else 'Litecoin version too old. Upgrade to 0.10.4 or newer!'
VERSION_WARNING = lambda v: None
SOFTFORKS_REQUIRED = set(['bip65', 'csv', 'segwit'])
MINIMUM_PROTOCOL_VERSION = 3301
NEW_MINIMUM_PROTOCOL_VERSION = 3301
SEGWIT_ACTIVATION_VERSION = 17
BLOCK_MAX_SIZE = 1000000
BLOCK_MAX_WEIGHT = 4000000
