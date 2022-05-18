FROM centos:7

RUN yum update -y

# 기본 프로그램 설정
RUN yum install -y \
    wget \
    java-1.8.0-openjdk-devel.x86_64 \
    openssh-server \
    openssh-clients \
    openssh-askpass 

# ssh 설정
RUN ssh-keygen -t rsa -P '' -f ~/.ssh/id_dsa \
    && cat ~/.ssh/id_dsa.pub >> ~/.ssh/authorized_keys \
    && ssh-keygen -f /etc/ssh/ssh_host_rsa_key -t rsa -N "" \
    && ssh-keygen -f /etc/ssh/ssh_host_ecdsa_key -t ecdsa -N "" \
    && ssh-keygen -f /etc/ssh/ssh_host_ed25519_key -t ed25519 -N "" 

# hadoop 설치
ENV HADOOP_VERSION=3.1.1
# ENV HADOOP_URL=http://mirror.apache-kr.org/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz
ENV HADOOP_URL=https://archive.apache.org/dist/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz 
RUN wget "$HADOOP_URL" -O /tmp/hadoop.tar.gz \
    && tar -xvzf /tmp/hadoop.tar.gz -C /opt/ \
    && rm /tmp/hadoop.tar.gz

# 데이터 디렉토리 생성 및 설정 폴더의 심폴링 링크 생성
RUN ln -s /opt/hadoop-$HADOOP_VERSION /opt/hadoop \
    && mkdir /opt/hadoop/dfs \
    && ln -s /opt/hadoop-$HADOOP_VERSION/etc/hadoop /etc/hadoop \
    && rm -rf /opt/hadoop/share/doc

# 설정파일 복사
# COPY core-site.xml /etc/hadoop
# COPY yarn-site.xml /etc/hadoop
# COPY mapred-site.xml /etc/hadoop

# 환경변수 설정
ENV JAVA_HOME /usr/lib/jvm/java-1.8.0-openjdk-1.8.0.322.b06-1.el7_9.x86_64
ENV HADOOP_HOME /opt/hadoop
ENV HADOOP_CONFIG_DIR /etc/hadoop
ENV YARN_CONFIG_DIR /etc/hadoop
ENV MAPRED_HOME /etc/hadoop
ENV PATH $HADOOP_HOME/bin/:$PATH
ENV PATH $HADOOP_HOME/sbin/:$PATH
