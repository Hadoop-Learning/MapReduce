# MapReduce调试

## 执行run文件
![image](https://github.com/idKevin/Hadoop-Learning/blob/master/.picture/MR_URL.png)
注意事项：
这里用得是局域网集群，在windows系统中在C:\Windows\System32\drivers\etc\hosts文件中添加master和与其对应的关系，192.168.1.103   master，这样就可以在本地解析master域名。

## MR执行正确的结果
复制链接至Chrome浏览器，进入Hadoop管理页面，即可看到Map程序和Reduce程序的执行情况：
![image](https://github.com/idKevin/Hadoop-Learning/blob/master/.picture/MR_Executing.png)


### MR执行正确的结果
若执行正确，则可得到如下图所示的结果：
![image](https://github.com/idKevin/Hadoop-Learning/blob/master/.picture/MR_Successful.png)


### MR执行错误调试方法
1. 若执行错误，则可得到如下图所示的结果：
![image](https://github.com/idKevin/Hadoop-Learning/blob/master/.picture/MR_Failed_1.png)
2. 此样例中是Reduce程序出错，点击错误的链接，进入Reduce提示部分：
![image](https://github.com/idKevin/Hadoop-Learning/blob/master/.picture/MR_Failed_2.png)
3. 可以定位到错误的信息：
![image](https://github.com/idKevin/Hadoop-Learning/blob/master/.picture/MR_Failed_3.png)
