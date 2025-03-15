# PoW 验证码系统

## 简介

这是一个基于工作量证明（Proof of Work，简称 PoW）的验证码系统。该系统旨在通过工作量证明机制，有效防止恶意攻击和自动化操作，为各类应用场景提供安全保障。

## 功能特点

- **工作量证明机制**：采用 PoW 算法，要求客户端完成一定计算任务，验证其真实性，增加攻击者成本。
- **多语言客户端支持**：提供多种语言的客户端实现，方便不同开发环境下的集成和使用。(TODO)
- **简单易用**：设计简洁，易于集成到各类应用中，无论是网站、移动应用还是其他系统，都能快速部署和使用。
- **资源消耗可控**：通过调整工作量证明的难度，可以在安全性和性能之间取得平衡。

## 技术架构

- **服务端**：使用 Python 编写，负责生成验证码、验证结果等工作。
- **客户端**：支持多种编程语言，包括但不限于 JavaScript、Java、C++ 等，方便不同平台的开发者进行集成。

## 项目结构

```
├─client 客户端
│  ├─golang
│  ├─javascript
│  └─python
└─server 服务端
```

## 使用方法

### 服务端

安装依赖，本项目使用 uv 管理依赖，推荐优先选择 uv

- 使用 `uv`

  ```bash
  uv sync
  ```

- 使用 `pip`

  ```bash
  pip install -r pyproject.toml
  ```

  或者

  ```bash
  pip install -r requirements.txt
  ```

配置文件

```json
{
  "secret": "a-string-secret-at-least-256-bits-long",
  "redis": {
    "host": "127.0.0.1",
    "port": "6379",
    "db": 1,
    "password": ""
  },
  "difficulty": 42
}
```

- redis：redis服务器地址、端口、数据库、密码
- difficulty：验证码难度，数字越大，难度越高，解答越慢
- secret：JWT签名密钥，请设置32位数以上的随机字符串

### 客户端

请查看各语言客户端的README

客户端基本流程如下所示：

```sequence
客户端->服务端: 请求challenge
服务端-->服务端: 生成challenge，写入redis
服务端-->客户端: 响应challenge
客户端->客户端: 计算结果
客户端->服务端: 提交结果
服务端-->服务端: 查询redis，验证结果
服务端-->客户端: 生成并响应token
客户端->业务服务器: 携带token发送自定义业务请求
业务服务器->服务端: 验证token
服务端-->业务服务器: 响应验证结果
业务服务器->客户端: 响应业务请求
```

## 贡献

欢迎各位开发者为本项目贡献代码、提出改进建议或报告问题。你可以通过以下方式参与：

1. **提交 Issue**：如果您发现任何问题或有任何改进建议，可以在 [Issues](https://github.com/yourusername/pow-captcha/issues) 页面提交。
2. **提交 Pull Request**：如果您想要直接参与代码改进，可以 fork 本项目，完成您的修改后提交 Pull Request。

## 许可证

本项目采用 [AGPLv3 License](LICENSE) 许可证。