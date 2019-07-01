pika auto reconnect example
===========================

pika早期版本不支持多RabbitMQ Server Host支持, 以及对重联机制提供的信息不足够,最新的几个版本都已经解决这些问题.
该示例工程,主要是提供LifeCycle机制将RabbitMQ Client端以服务的形式管理起来,同时实现简便的重联机制.
需要的详细看看具体代码

lifecycle.py实际上是eclipse jetty java代码中组建, 其实java和python之间很多应用代码都在互相学习,比如这里的lifecycle.py, 还有类似StopWatch的实现等等.
