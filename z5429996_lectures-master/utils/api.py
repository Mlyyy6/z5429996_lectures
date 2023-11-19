# from toolkit import config
# print(config.APIKEY)
"""
it is not valid because toolkit is not a module/package.
why it can run without rasing exception?
"""


# from config import APIKEY
# print(APIKEY)

# from config import APIKEY
# print(config.APIKEY)
"""
it is not valid because the name config is not added to the global namespace.
The only name from config.py added to the global namespace is APIKEY.
"""

# import config
# print(config.APIKEY)
# #before added the config.py inside the utils package, it print abc

# import config as cfg
# print(cfg.APIKEY)
# after added the config.py inside the utils package, it print 123

# from utils import config as cfg
# print(cfg.APIKEY)

# from utils.config import APIKEY
# print(APIKEY)

from config import APIKEY
print(APIKEY)