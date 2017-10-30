# Hadoop生态概况
Hadoop是一个由Apache基金会所开发的分布系统基础架构。用户可以在不了解分布式底层细节的情况下，开发分布式程度。充分利用集群的威力进行高速运算和存储。具有可靠、高效、可伸缩的特点。

## HDFS
Hadoop分布式文件系统，源自于Google的GFS论文，发表于2003年10月，HDFS是GFS克隆版。HDFS是Hadoop体系中数据存储管理的基础。它是一个高度容错的系统，能检测和应对硬件故障，用于在低成本的通用硬件上运行。HDFS简化了文件的一致性模型，通过流式数据访问，提供高吞吐量应用程序数据访问功能，适合带有大型数据集的应用程序。它提供一次写入多次读取的机制，数据以块的形式，同时分布在集群不同物理机器上。

## Yarn
Yarn是分布式资源管理器，Yarn是下一代MapReduce，即MRv2，是在第一代MapReduce基础上演变而来的，主要是为了解决原始Hadoop扩展性较差，不支持多计算框架而提出的。Yarn是下一代Hadoop计算平台，yarn是一个通用的运行时框架，用户可以编写自己的计算框架，在该运行环境中运行。用于自己编写的框架作为客户端的一个lib，在运用提交作业时打包即可。该框架为提供了以下几个组件：
- 资源管理：包括应用程序管理和机器资源管理
- 资源双层调度
- 容错性：各个组件均有考虑容错性
- 扩展性：可扩展到上万个节点

## Tachyon
Tachyon是分布式内存文件系统（Tachyon诞生于UC Berkeley的AMPLab），Tachyon是内存为中心的分布式文件系统，拥有高性能和容错能力，能够为集群框架（如Spark、MapReduce）提供可靠的内存级速度的文件共享服务。

## MapReduce
MapReduce是分布式计算框架，源自于Google的MapReduce论文，发表于2004年12月，Hadoop MapReduce是google MapReduce克隆版。MapReduce是一种分布式计算模型，用以进行大数据量的计算。它屏蔽了分布式计算框架细节，将计算抽象成map和reduce两部分，其中Map对数据集上的独立元素进行指定的操作，生成键-值对形式中间结果。Reduce则对中间结果中相同“键”的所有“值”进行规约，以得到最终结果。MapReduce非常适合在大量计算机组成的分布式并行环境里进行数据处理。

## HBase
HBase是分布式列存数据库，源自Google的Bigtable论文，发表于2006年11月，HBase是Google Bigtable克隆版，HBase是一个建立在HDFS之上，面向列的针对结构化数据的可伸缩、高可靠、高性能、分布式和面向列的动态模式数据库。HBase采用了Big Table的数据模型：增强的稀疏排序映射表(Key/Value)，其中，键由行关键字、列关键字和时间戳构成，HBase提供了对大规模数据的随机、实时读写访问，同时，HBase中保存的数据可以使用MapReduce来处理，它将数据存储和并行计算完美地结合在一起。

## Zookeeper
Zookeeper是分布式协作服务，源自Google的Chubby论文，发表于2006年11月，Zookeeper是Chubby克隆版。解决分布式环境下的数据管理问题：统一命名，状态同步，集群管理，配置同步等。Hadoop的许多组件依赖于Zookeeper，它运行在计算机集群上面，用于管理Hadoop操作。

## Hive
Hive是数据仓库，由facebook开源，最初用于解决海量结构化的日志数据统计问题。Hive定义了一种类似SQL的查询语言(HQL)，将SQL转化为MapReduce任务在Hadoop上执行。通常用于离线分析。HQL用于运行存储在Hadoop上的查询语句，Hive让不熟翻MapReduce开发人员也能编写数据查询语句，然后这些语句被翻译为Hadoop上面的MapReduce任务。

## Pig
Pig是ad-hoc脚本，由yahoo！开源，设计动机是提供一种基于MapReduce的ad-hoc(计算在query时发生)数据分析工具，Pig定义了一种数据流语言（Pig Latin），它是MapReduce编程的复杂性的抽象，Pig平台包括运行环境用于分析Hadoop数据集的脚本语言(Pig Latin)。

## Sqoop
Sqoop是SQL-to-Hadoop的缩写，主要用于传统数据库和Hadoop之间传输数据。数据的导入和导出本质上是MapReduce程序，充分利用了MR的并行化和容错性。Sqoop利用数据库技术描述数据架构，用于在关系数据库、数据仓库和Hadoop之间转移数据。

##  Flume
Flume是日志收集工具，Cloudera开源的日志收集系统，具有分布式、高可靠、高容错、易于定制和扩展的特点。它将数据从产生、传输、处理并最终写入目标的路径的过程抽象为数据流，在具体的数据流中，数据源支持在Flume中定制数据发送方，从而支持收集各种不同协议数据。同时Flume数据流提供对日志数据进行简单处理的能力，如过滤、格式转换等。此外，Flume还具有能够将日志写往各种数据目标（可定制）的能力。总得来说，Flume是一个可扩展、适合复杂环境的海量日志收集系统。当然也可以用于收集其他类型数据。
