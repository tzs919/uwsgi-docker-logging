# uwsgi-docker-logging
Logging configuration of a flask container with uWSGI and Nginx using Supervisor, Syslog-ng and FluentD.
The deployment collects both the Nginx and uWSGI (application) logs and separates between them by introducting `process` tag with either `uwsgi` or `nginx` values.
Nginx logs are parsed using FluentD Nginx parsing support. Python (uWSGI) exceptions (Traceback) multi-line logs are concatenated into a single log message.

# Configuration

## Output to Elasticsearch
Point FluentD container to Elasticsearch by setting the environment variables `ES_HOST` and `ES_PORT`


构建fluentd镜像并启动
docker-compose up --build fluentd

tutorial3的程序路径在：C:\python\tutorial3

运行前先docker-compose down
需要按以下顺序启动
docker-compose up -d elasticsearch kibana
docker-compose up -d fluentd
docker-compose up -d flask tutorial3
