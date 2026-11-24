"""One-line pitch entry: a single sentence that invites a non-coder friend
to let an AI agent build their first app idea on make.fun."""

LINE = "Just tell me the app idea you've been carrying around, and I'll build you a first version to try for free, no coding needed and nothing to lose if it's not for you."


def main():
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
