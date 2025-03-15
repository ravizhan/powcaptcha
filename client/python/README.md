## Python 客户端

### 安装

```bash
pip install powcaptcha
```

### 接入

```python
from powcaptcha import PowCaptcha
captcha = PowCaptcha("http://localhost:8000") # 填写服务端地址，实例化类
token = captcha.solve() # 自动完成验证码，成功返回token否则为None
```