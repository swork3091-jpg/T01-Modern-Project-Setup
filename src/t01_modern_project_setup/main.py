import sys
import requests


def main() -> None:
    print("Hello from uv!")
    print(f"Python version: {sys.version}")
    print(f"Requests version: {requests.__version__}")
    print("T01 - Modern Project Setup with uv")


if __name__ == "__main__":
    main()