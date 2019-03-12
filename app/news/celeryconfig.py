# coding=utf-8
BROKER_URL = 'amqp://zoucongchao:''@localhost/myvhost'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/6'
#将序列化消息反序列化
CELERY_TASK_SERIALIZER = 'msgpack'
#使用可读性高的json读取任务结果
CELERY_RESULT_SERIALIZER = 'json'
#任务失效时间，不直接写86400
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24
#指定接受的内容类型
CELERY_ACCEPT_CONTENT = ['json', 'msgpack']
