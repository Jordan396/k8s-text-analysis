#!/usr/bin/env python

import time
import rediswq
import os
import json

# Config variables
redis_wq_name = os.environ['REDIS_WQ_NAME']
redis_wq_host = os.environ['REDIS_WQ_HOST']
input_datasets_dir_path = os.environ['INPUT_DATASETS_DIR_PATH']
reduced_output_filename = os.environ['REDUCED_OUTPUT_FILENAME']

# Initiate Redis
q = rediswq.RedisWQ(name=redis_wq_name, host=redis_wq_host)
print("Worker with sessionID: " +  q.sessionID())
print("Initial queue state: empty=" + str(q.empty()))

def main():
  reduced_output_dict = {}
  while not q.empty():
    _, task_key = q.dequeue()
    task_name = task_key.decode("utf-8")
    input_filename = input_datasets_dir_path + "/" + task_name
    # print(input_filename)
    with open(input_filename) as json_file:
      data = json.load(json_file)
      for key, value in data.items():
        # print(key + ":" + str(value))
        if key in reduced_output_dict:
          # print("key exists. Adding value of key...")
          reduced_output_dict[key] = reduced_output_dict[key] + value
        else:
          # print("key does not exist. Adding key...")
          reduced_output_dict[key] = value
    # print(reduced_output_dict)
  with open(reduced_output_filename, 'w') as fp:
    json.dump(reduced_output_dict, fp)

if __name__ == "__main__": 
  main()