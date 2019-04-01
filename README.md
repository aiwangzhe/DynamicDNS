###该项目使用阿里云云解析SDk，实现动态域名解析的功能
####使用方法:
#####1. 安装阿里云python-sdk: sudo pip install aliyun-python-sdk-alidns
#####2. 编辑AliRequest.py文件，将被标注TODO的代码内容替换为自己的信息
#####3. 执行sh UpdateIP.sh命令，执行域名将被映射到自己机器所在的公网ip
#####4. 如果需要将脚步加入定时任务，修改CheckIpTask.cron文件，将脚本路径修改为自己机器上文件路径