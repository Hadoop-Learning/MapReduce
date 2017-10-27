# MapReduce应用

## MR是一套并行编程架构，它隐藏了并行计算的复杂的细节(如输入数据分割、任务调度、容错以及工作集群的内部通信等)，程序员只需要专注于数据处理以及结果化简就可以。程序员不需要有任何的分布式开发经验就可以使用分布式系统的资源。


### MR的执行流程
MR的执行流程我们这里通过统计每个单词出现次数的例子来说明(这里我们需要了解数据流这个概，数据是通过管道以流式的形式传输的)：
1. 原始的数据里有若干记录，每条记录有若干单词；
2. 这里的输入数据非常的大，我们首先进行分割，分割就对应下图中的Split(分割成多少份是通过参数指定)；
3. 每个分割完的数据块对应一个Map程序，每个Map程序分别处理对应的数据块，Map程序将数据块的每条记录中单词进行拆分，后面的1代表出现的次数(注：也可以在此阶段进行数据块里的单词统计，请参照Solution 2)；
4. 经过Map程序处理后输出的数据流会经过排序算法自动排序(也就是聚合)，对应图中的Sort部分，相同的数据被聚合在一起；
5. 排序完的数据流会输出到Reduce程序，每个Reduce程序将统计各自数据块里单词的数目；
6. 最后的结果数据流存储在数据库中(注：结果的数据也是以分布式的方式存储的)；


![image](https://github.com/ButBueatiful/dotvim/raw/master/screenshots/vim-screenshot.jpg)
**以上的执行流程等价于Shell程序: cat data | python3 mapper.py | sort -k1 | python3 reducer.py，因为该框架Mapper与Reduce程序都是并行执行的，所以效率大大的提升，这种分布式架构主要是分而治之的思想。下面以具体的统计单词数目的例子进一步说明：**

### Solution 1
#### MR的指定分块的数目
```
    -D mapred.map.tasks=3
    -D mapred.reduce.tasks=4
```

#### Map程序(关键代码部分)
将数据流以键-值对的形式输出
```
import sys

def main():
    """ handle data streaming. """
    for line in sys.stdin:
        words = line.rstrip().split(' ')
        for word in words:
            print(word, "1", sep="\t")
```

#### Reduce程序(关键代码部分)

```
import sys
from operator import itemgetter
from itertools import groupby

def read_data():
    for line in sys.stdin:
        yield line.rstrip().split('\t')

def main():
    """ count the number """
    data = read_data()
    for key, it in groupby(data, itemgetter(0)):
        print(key, len(list(it)), sep="\t")
```



### Solution 2



#### MR的指定分块的数目
```
    -D mapred.map.tasks=3
    -D mapred.reduce.tasks=4
```

#### Map程序(关键代码部分)
将数据流以键-值对的形式输出
```
import sys

def main():
    """ handle data streaming. """
    for line in sys.stdin:
        words = line.rstrip().split(' ')
        wordsDict = dict()
        for word in words:
            if word in wordsDict:
                wordsDict[word] += 1
            else:
                wordsDict[word] = 1
        
        for word in wordsDict:
            print(word, wordsDict[word], sep="\t")
```

#### Reduce程序(关键代码部分)
```
import sys
from operator import itemgetter
from itertools import groupby


def read_data():
    """ read the data. """
    for line in sys.stdin:
        yield line.rstrip().split('\t')


def main():
    """ count the number """
    data = read_data()
    for key, it in groupby(data, itemgetter(0)):
        s = 0
        for e in it:
            s += int(e[1])
        print(key, s, sep="\t")
```
