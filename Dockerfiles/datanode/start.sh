#!/bin/sh

$HADOOP_HOME/bin/hdfs --config $HADOOP_CONFIG_DIR datanode 
# $HADOOP_HOME/bin/hdfs --config $HADOOP_CONFIG_DIR datanode &
# $HADOOP_HOME/bin/yarn --config $YARN_CONFIG_DIR nodemanager
