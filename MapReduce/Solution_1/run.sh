#!/bin/bash

HADOOP_BIN="hadoop"

INPUT="/user/calvinxu/Input/*"

# 输出目录
OUTPUT="/user/calvinxu/Demo"
# 判断输出目录是否存在,存在则删除输出目录
${HADOOP_BIN} fs -test -e ${OUTPUT}
if [ $? -eq 0 ]; then
    ${HADOOP_BIN} fs -rm -r ${OUTPUT}
fi

# $HADOOP_BIN streaming \
hadoop jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -D mapred.job.map.capacity=1000 \
    -D mapred.job.reduce.capacity=100 \
    -D num.key.fields.for.partition=1 \
    -D stream.num.map.output.key.fields=1 \
    -D mapred.task.hce.accept.limit=30000 \
    -D mapred.job.priority="HIGH" \
    -D mapred.job.name="Demo" \
    -D mapred.map.tasks=10 \
    -D mapred.reduce.tasks=4 \
    -input ${INPUT} \
    -output ${OUTPUT} \
    -mapper "mapper.py" \
    -reducer "reducer.py" \
    -file "mapper.py" \
    -file "reducer.py" \
    -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner
