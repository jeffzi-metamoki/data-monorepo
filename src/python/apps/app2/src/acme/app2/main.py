import argparse
from .app2_module1 import app2_func1

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="app2")
    parser.add_argument("conf", metavar="conf", type=str, help="Config path")
    conf = parser.parse_args().conf
    print(f"Config file at {conf}")
    app2_func1()
