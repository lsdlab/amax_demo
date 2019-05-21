1. django/django-rest-framework 写两个 API，实现同样功能，接受 json，post create 到数据库，一个是普通同步请求，
另一个是收到数据后放入 celery task 中执行。
2. celery task 设置 autoscale 将会看到 celery worker 进程池的进程个数变化，启动时是最低并发进程+1，
请求变多后会自动 scale up，请求减少后会 scale down


检查 celery worker 进程池数量命令

```
celery -A apps.celeryconfig inspect stats
```

启动 gunicorn

```
export DJANGO_SETTINGS_MODULE=conf.production.settings
gunicorn --workers 3 --bind 0.0.0.0:9000 amax.wsgi:application
```

启动 celery worker

```
export DJANGO_SETTINGS_MODULE=conf.production.settings
celery -A apps.celeryconfig worker --loglevel=info --autoscale=4,2
```

启动 celery flower 监控 celery

```
flower -A apps.celeryconfig --basic_auth=user1:password1
```

**rabbitmq kafka 消息中间件对比**

1. kafka 性能最强，吞吐量最高，对消息的重复，丢失，错误没有严格要求，适合日志系统，无消息 ack 机制
2. rabbitmq erlang，基于AMQP协议，路由，负载均衡支持好，消息持久化，可将 MQ 作为存储使用，数据一致性/稳定性/可靠性最强，有消息 ack 机制
3. redis pub/sub 实时性最强，可靠性低，适合实时推送系统
