
## config

- hocon配置比较灵活，支持comment，引用，覆盖等
- 使用时候可以转成dict，然后再用pydantic转换，就有类型信息了
- 相对原始hocon这里增加了dot-style访问支持，使用pydantic后其实这个用不少了？

```py
params_dict = params.as_dict()
```

## hpyhrt_context

全局变量container，类似spring的bean container，用于不同模块wire

- get_config_inst
- get_global_context

## init_app_base

- 解析config
- init_app_default_configs: app特有缺省值
- init_base_default_configs: base缺省值
- `global_context.throttle = Throttle()`
- `IOUtil.maybe_make_dir`
- `log.setup_logging`

## log

- `log_config_default`: 缺省log配置
- `init_log_default_configs`: config可以对log进行一定配置，比如`log_dir`, `log_handlers`, `logger_levels`
- handlers: console, file, error file
- rollover on startup
- size based rotation
- logger level setup

## model

rest api model 定义

具体相应内容放到data字段，而error放到error字段

```py
    error: ErrorInfo | None = None
    data: DataType | None = None    
```

## utils

有些Util没用到，目前也没删除，后面择机删除

- CheckUtil: 测试验证结果
- CollectionUtil: dict等上操作
- ConfigUtil
- DebugUtil: 重置初始化
- FuncUtil: retry等功能
- IOUtil: 远端下载，本地文件操作等
- LogUtil
- MailUtil: 发送邮件
- ObjectUtil
- RandomUtil
- StrUtil: pprint打印json等
- Throttle: sina等有限速限制
- TimeUtil: 日期时间相关
