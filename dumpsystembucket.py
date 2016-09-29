# download system bucket
import os

from marvin_scaler_lib.bucket.list import list_system_bucket
from marvin_scaler_lib.bucket.download import download_from_system_bucket

sb_keys = [x for x in list_system_bucket()]
sb_install = [x for x in sb_keys if 'install' in x]
for x in sb_install:
    dir = os.path.dirname(x)
    if not os.path.exists(dir):
        os.makedirs(dir)
        
[download_from_system_bucket(keyname=x, filepath=x) for x in sb_install]
