# Snailclimb/JavaGuide

Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发

## tools

- [API 网关基础知识总结](https://javaguide.cn/distributed-system/api-gateway.html)
- [Spring Cloud Gateway 常见知识点&面试题总结](./docs/distributed-system/spring-cloud-gateway-questions.md)

### 分布式 ID

- [分布式ID介绍&实现方案总结](https://javaguide.cn/distributed-system/distributed-id.html)
- [分布式 ID 设计指南](https://javaguide.cn/distributed-system/distributed-id-design.html)

### 分布式锁

- [分布式锁介绍](https://javaguide.cn/distributed-system/distributed-lock.html)
- [分布式锁常见实现方案总结](https://javaguide.cn/distributed-system/distributed-lock-implementations.html)

### 分布式事务

[分布式事务常见知识点&面试题总结](https://javaguide.cn/distributed-system/distributed-transaction.html)

### 分布式配置中心

[分布式配置中心常见知识点&面试题总结](./docs/distributed-system/distributed-configuration-center.md)

## 高性能

### 数据库优化

- [数据库读写分离和分库分表](./docs/high-performance/read-and-write-separation-and-library-subtable.md)
- [数据冷热分离](./docs/high-performance/data-cold-hot-separation.md)
- [常见 SQL 优化手段总结](./docs/high-performance/sql-optimization.md)
- [深度分页介绍及优化建议](./docs/high-performance/deep-pagination-optimization.md)

### 负载均衡

[负载均衡常见知识点&面试题总结](./docs/high-performance/load-balancing.md)

### CDN

[CDN（内容分发网络）常见知识点&面试题总结](./docs/high-performance/cdn.md)

### 消息队列

- [消息队列基础知识总结](./docs/high-performance/message-queue/message-queue.md)
- [Disruptor 常见知识点&面试题总结](./docs/high-performance/message-queue/disruptor-questions.md)
- [RabbitMQ 常见知识点&面试题总结](./docs/high-performance/message-queue/rabbitmq-questions.md)
- [RocketMQ 常见知识点&面试题总结](./docs/high-performance/message-queue/rocketmq-questions.md)
- [Kafka 常见知识点&面试题总结](./docs/high-performance/message-queue/kafka-questions-01.md)

## 高可用

[高可用系统设计指南](./docs/high-availability/high-availability-system-design.md)

### 冗余设计

[冗余设计详解](./docs/high-availability/redundancy.md)

### 限流

[服务限流详解](./docs/high-availability/limit-request.md)

### 降级&熔断

[降级&熔断详解](./docs/high-availability/fallback-and-circuit-breaker.md)

### 超时&重试

[超时&重试详解](./docs/high-availability/timeout-and-retry.md)

### 集群

相同的服务部署多份，避免单点故障。

### 灾备设计和异地多活

**灾备** = 容灾 + 备份。

- **备份**：将系统所产生的所有重要数据多备份几份。
- **容灾**：在异地建立两个完全相同的系统。当某个地方的系统突然挂掉，整个应用系统可以切换到另一个，这样系统就可以正常提供服务了。

**异地多活** 描述的是将服务部署在异地并且服务同时对外提供服务。和传统的灾备设计的最主要区别在于“多活”，即所有站点都是同时在对外提供服务的。异地多活是为了应对突发状况比如火灾、地震等自然或者人为灾害。

## Star 趋势

[![Star History Chart](https://star-history.dera.page/svg?repos=Snailclimb/JavaGuide&type=date&legend=top-left)](https://star-history.dera.page/#Snailclimb/JavaGuide&type=date&legend=top-left)

## 公众号

如果大家想要实时关注我更新的文章以及分享的干货的话，可以关注我的公众号。

<img src="https://oss.javaguide.cn/github/javaguide/gongzhonghao-javaguide.png" alt="JavaGuide 公众号"  style="zoom: 43%; display: block; margin: 0 auto;" />

<!-- #endregion home -->
