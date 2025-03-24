from pathlib import Path
from re import finditer

# 正则表达式匹配 @file("file_path")
FILE_PATTERN = r"""@file\(['"]?([^'"]+)['"]?\)"""


def get_file_content(file_path: str) -> str:
    """读取文件内容并返回"""
    file = Path(file_path)
    if file.exists() and file.is_file():
        return file.read_text(encoding="utf-8")
    raise FileNotFoundError(f"File not exist: {file_path}")


def before_ai_ask_hook(user_input: str, _: str) -> str:
    """在用户输入传递给AI之前，处理包含@file("file_path")的输入"""
    matches = finditer(FILE_PATTERN, user_input)
    for _match in matches:
        file_func = _match.group(0)
        file_path = _match.group(1)
        file_content = get_file_content(file_path)
        user_input = user_input.replace(file_func, file_content)
    return user_input
