#!/usr/bin/env python

import time
import rediswq
import os
import pandas as pd
import json

# TODO: Remove time.sleep() for actual applications

# Config variables
redis_wq_name = os.environ['REDIS_WQ_NAME']
redis_wq_host = os.environ['REDIS_WQ_HOST']
wordlist_file_path= os.environ['WORDLIST_FILE_PATH']
input_datasets_dir_path = os.environ['INPUT_DATASETS_DIR_PATH']
processed_datasets_dir_path = os.environ['PROCESSED_DATASETS_DIR_PATH']

# Initiate Redis
q = rediswq.RedisWQ(name=redis_wq_name, host=redis_wq_host)
print("Worker with sessionID: " +  q.sessionID())
print("Initial queue state: empty=" + str(q.empty()))

def wordcount_task(filename, pattern):
  input_filename = input_datasets_dir_path + "/" + filename
  output_filename = processed_datasets_dir_path + "/" + filename.replace("csv","json")
  col_names=['id', 'date', 'time', 'tweet', 'location'] 
  df = pd.read_csv(input_filename, names=col_names, encoding='utf-8')
  df = df[df['tweet'].str.contains(pattern, na=False)]
  if not df.empty:
      df1 = (df['tweet'].str.split(expand=True).stack().value_counts().rename_axis('vals').reset_index(name='count'))
      df1["count"] = pd.to_numeric(df1["count"])
      dict_format = dict(zip(df1["vals"], df1["count"]))
      with open(output_filename, 'w') as fp:
        json.dump(dict_format, fp)
      # For illustration purposes
      time.sleep(5)

def get_word_list_pattern():
  wordList = []
  with open(wordlist_file_path,'r') as file:
    lines = file.read().splitlines()
  print (str(lines))
  pattern = '|'.join([f'(?i){word}' for word in lines])
  return pattern

def main():
  pattern = get_word_list_pattern()
  while not q.empty():
    item = q.lease(lease_secs=30, block=True, timeout=2) 
    if item is not None:
      itemstr = item.decode("utf-8")
      print("Working on " + itemstr)
      # Work on task here
      wordcount_task(itemstr, pattern)
      q.complete(item)
    else:
      break
  print("Queue empty, exiting")

if __name__ == "__main__": 
  main()