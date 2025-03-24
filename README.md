# 🚀 agent-cli

**在终端中与 AI 对话，轻松解决你的问题！**

## 📖 简介

`agent-cli` 是一个命令行工具，允许你直接在终端中向 AI 提问。无论是代码解释、脚本生成，还是简单的问答，`agent-cli` 都能帮你快速获得答案。

## 🌟 功能亮点

- **灵活的模式选择**：支持对话模式、生成 shell 脚本、生成代码等多种模式。
- **丰富的输出选项**：可以将 AI 的输出保存到文件，或使用 `rich` 库渲染 markdown 格式的输出。
- **简洁易用**：通过管道或直接输入 prompt，快速获取 AI 的回答。
- **自定义插件**: 支持编写 python 插件，对 prompt 和 AI 回答进行处理。

## 🛠️ 帮助信息

```bash
usage: agent-cli.py [-h] [-m MODEL] [-a] [-iu] [-ia] [-c] [-sh] [-co] [-o OUTPUT] [-r] [prompt]

Ask any questions to AI

positional arguments:
  prompt                用户询问的 prompt

options:
  -h, --help            show this help message and exit
  -m MODEL, --model MODEL
                        用户选择的 model
  -a, --ahead           参数 prompt 是否拼接在管道 prompt 的前面, 默认为 true
  -iu, --ignore_user    不展示 user 输入的 prompt, 默认为 false
  -ia, --ignore_ai      不展示 ai 的模型信息, 默认为 false
  -c, --conversation    启用对话模式, 默认为 false
  -sh, --shell          启用生成`shell脚本`模式, 默认为 false
  -co, --code           启用生成`code代码`模式, 默认为 false
  -o OUTPUT, --output OUTPUT
                        将 AI 的输出写入指定文件
  -r, --rich            将 AI 的输出使用 rich 进行 markdown 渲染, 默认为 false
```

## 🚀 快速使用

在项目文件夹下创建一个 `.env` 文件，使用 `.env.example` 中的定义，将 `BASE_URL` 和 `API_KEY` 填写完成即可。

```bash
# 解释代码
cat agent-cli.py | ./agent-cli.py 'Help me explain this python code'

# 连续对话
echo 'hello' | ./agent-cli.py -c

# 使用file插件将README.md描述优化并输出到新文件；终端上使用 rich 库美化输出
./agent-cli.py '帮我优化这个 md 的描述 @file("README.md")' -r -o=README.md.new

# 生成 shell 脚本并执行
./agent-cli.py --shell '在终端输出 hello-world'

# 生成代码
./agent-cli.py --code '生成经典算法题 `接雨水` 的代码'
```

## 🛠️ 安装与使用

1. **安装依赖**：

   ```bash
   pip install -r requirements.txt
   ```

2. **运行工具**：

   ```bash
   ./agent-cli.py '你的问题或指令'
   ```

3. **帮助菜单**：

   ```bash
   ./agent-cli.py --help
   ```

4. **alias**

    ```bash
    chmod +x ./agent-cli.py
    alias ask="/home/work/agent-cli/agent-cli.py"
    ```

## 🔌 插件功能

在 plugins 文件夹下可以编写插件, 通过自定义 `before_ai_ask_hook` 和 `after_ai_ask_hook` 函数即可分别完成对 `prompt` 和 `AI回答` 的 hook。

内置的 plugin 有:

- `file.py` （使用 `@file('test.py')` 将文件的内容写入用户输入的 prompt）
- `fetch.py` （使用 `@fetch('https://www.baidu.com')` 将网页的内容写入用户输入的 prompt）
- `shell.py` （开启 `-sh 或 --shell` 参数后，用户选择是否执行 AI 生成的 shell 脚本）

## 👋 最后

立即体验 `agent-cli`，让 AI 成为你的终端助手！

*(该 README.md 使用 `agent-cli` & `DeepSeek-V3` 优化)*
