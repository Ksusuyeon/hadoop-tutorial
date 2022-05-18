FROM hadoop-base:latest

# DataNode Web UI 응답 여부를 통해 Healthcheck
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3  CMD curl -f http://localhost:9870/ || exit 1

RUN mkdir /opt/hadoop/dfs/data
VOLUME /opt/hadoop/dfs/data

RUN mkdir -p /opt/hadoop/yarn/data
VOLUME /opt/hadoop/yarn/data

# COPY yarn-site.xml /etc/hadoop

ADD start.sh /start.sh
RUN chmod a+x /start.sh

# WebUI, 데이터전송
EXPOSE 9870 9864 8042

CMD ["/start.sh"]