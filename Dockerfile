# 基础镜像使用指定引用官方提供的ubuntu:16.04
FROM ubuntu:16.04

# 作者信息
LABEL maintainer "1025621226@qq.com"

RUN apt-get update -y

RUN apt-get -y install python

RUN sudo apt-get install python-pip

# 绑定宿主机5000端口
EXPOSE 5000

# 创建app目录
RUN mkdir /app

# 指定工作目录为app
WORKDIR /app

# 复制所有内容到/app目录下
COPY . /app

# 复制本地requirements.txt到容器/app下
#COPY requirements.txt /app/requirements.txt

# 容器内运行命令,安装依赖包
RUN pip install -r requirements.txt



# 使用python解释器运行run
CMD ["python", "run.py"]