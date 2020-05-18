#!/bin/bash
if [ ! -d /mnt/ceph-filesystem/input_datasets ]; then
  mkdir -p /mnt/ceph-filesystem/input_datasets;
fi
if [ ! -d /mnt/ceph-filesystem/processed_datasets ]; then
  mkdir -p /mnt/ceph-filesystem/processed_datasets;
fi
if [ ! -d /mnt/ceph-filesystem/reduced_output ]; then
  mkdir -p /mnt/ceph-filesystem/reduced_output;
fi
if [ ! -d /mnt/ceph-filesystem/wordlist ]; then
  mkdir -p /mnt/ceph-filesystem/wordlist;
fi
if [ ! -d /mnt/ceph-filesystem/wordcloud_image ]; then
  mkdir -p /mnt/ceph-filesystem/wordcloud_image;
fi