# uwsgi-docker-logging
Logging configuration of a flask container with uWSGI and Nginx using Supervisor, Syslog-ng and FluentD.
The deployment collects both the Nginx and uWSGI (application) logs and separates between them by introducting `process` tag with either `uwsgi` or `nginx` values.
Nginx logs are parsed using FluentD Nginx parsing support. Python (uWSGI) exceptions (Traceback) multi-line logs are concatenated into a single log message.

# Configuration

## Output to Elasticsearch
Point FluentD container to Elasticsearch by setting the environment variables `ES_HOST` and `ES_PORT`
