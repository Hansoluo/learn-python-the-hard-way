## Py小结 ##

### 开学任务 ###

- [作业仓库](https://github.com/Hansoluo/learn-python-the-hard-way)
- [py学习笔记](https://github.com/Hansoluo/learn-python-the-hard-way/blob/master/py%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0.md)
- [git操作教程](https://github.com/Hansoluo/learngit/blob/master/git.md)

### 过程 ###

年初接触过《LPTHW》，那时只是敲代码而已，没有太多思考。七月末决定报班，用一个周末时间把习题重做一遍。因为是第二遍，有点枯燥，在issue里看到有人提到反推代码。这样做下来，才体会到编程的乐趣。之后便是学习git操作花费了两个晚上的时间，遇到一些问题，但最终都解决了。

### 复盘 ###
1. 在练习LPTHW并没有遇到多少难题，反而是学习git操作挺折腾的。
学习git操作用的是[廖雪峰的git教程](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)。在[添加远程库](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/0013752340242354807e192f02a44359908df8a5643103a000)这步操作中运行下列命令时报错：
``$ git remote add origin git@github.con:Hansoluo/learngit.git``
``fatal: Could not read from remote repository``
2. 上网寻找解决措施，过程记录如下：
 - 删除SSHkey重新添加，却仍报错
 - 修改`.gitconfig`。这才发现配置信息不对
 - 把用户名改成`github`上的用户名：`$ git config --global github.user Hansoluo`
 - 重新连接`github`远程项目，报错`fatal:remote origin already exits.`
 - 输入`$ git remote rm origin`重新连接远程仓库
 - 执行`$ git push -u origin master`报错`failed to push some refs to..`
 - 输入`$ git pull origin master`，把文件拉下来再push上去
 - 关闭问题
3. 导致连接不上的原因有：
 - 配置信息和Github上不匹配
 - SSHkey有两个，一个生成的，一个安装PC版自动生成的
4. 遇到问题主要是去网上寻找帮助，此时可能会有很多种解决方法，但并不完全适用于个人的情况，这个时候需要自己去对问题进行分析，再结合网上的帮助资料尝试解决。
5. 定义问题这个阶段花费时间最长。一旦找准了问题定位，解决起来就很快。

### 感想 ###

- 明确感受到同侪压力，有很多优秀的同伴
- 输出是更残酷的输入
- 需要更规范的学习的流程

##  心流记录  ###
- 遇到比较简单和熟悉的东西，容易进入心流
- 遇到感兴趣的内容，容易进入心流
- 需要打很长的字符串、遇到不能理解的代码、只是单纯的输入代码时很难进入心流
- 为了更容易进入心流，应该尽量让编程变得有趣。可以在大脑中先预编码一遍，使得大脑兴奋起来，再逐步编程
- 为了更容易进入心流，应该尽量循序渐进学习，不要一开始啃硬骨头