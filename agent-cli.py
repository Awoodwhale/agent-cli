#!/usr/bin/env python3
from sys import stdout

from agents import Agent
from cli import cli_args
from env import env_config
from plugins import after_ai_ask, before_ai_ask

MODELS = {
    "chatgpt": "gpt-4o",
    "4O": "gpt-4o",
    "V3": "deepseek-chat",
    "R1": "deepseek-reasoner",
    "claude": "claude-3-7-sonnet-20250219",
}


def main():
    model = MODELS.get(cli_args.model, cli_args.model)
    assert model in MODELS.values(), f"Model not exist {cli_args.model} !"

    agent = Agent(
        cli_args,
        model,
        env_config,
        output_io=stdout,
        before_ai_ask_hook=before_ai_ask,
        after_ai_ask_hook=after_ai_ask,
    )
    try:
        agent.run()
    except KeyboardInterrupt:
        pass
    except Exception:
        from traceback import print_exc

        print_exc()


if __name__ == "__main__":
    main()
