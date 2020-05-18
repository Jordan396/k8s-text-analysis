#!/usr/bin/env python

import time
import os
import rediswq

# Config variables
redis_wq_name = os.environ['REDIS_WQ_NAME']
redis_wq_host = os.environ['REDIS_WQ_HOST']
keys_dir_path = os.environ['KEYS_DIR_PATH']

# Initiate Redis
q = rediswq.RedisWQ(name=redis_wq_name, host=redis_wq_host)

# Get all filenames of input datasets
keys = [f for f in os.listdir(keys_dir_path) if os.path.isfile(os.path.join(keys_dir_path, f))]
print (str(keys))

for key in keys:
  q.enqueue(key)
