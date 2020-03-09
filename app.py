import argparse

from encoder.encoder import Base64EncoderStrategy
from minifyer.minifyer import Minifyer
from settings.settings import get_config

from web.app import start


def get_arguments():
    global args
    parser = argparse.ArgumentParser("Minify url")
    parser.add_argument("--url", type=str, help="Url to minify")
    parser.add_argument("--action", type=str, default="minify", choices=["minify", "deminify"])
    parser.add_argument("--config", type=str, default="dev.json", help="Config file")
    parser.add_argument("--http", type=bool, default=False, help="Start as webservice")
    args = parser.parse_args()

def cli():
    minifyier = Minifyer(Base64EncoderStrategy())

    actions_mapping = {
        "minify": minifyier.minify,
        "deminify": minifyier.deminify
    }

    result = actions_mapping[args.action](args.url)
    print(result)

def start_web_server():
    print("Start Flask")
    start()

if __name__ == "__main__":

    get_arguments()

    get_config(args.config)
    if args.http:
        start_web_server()
    else:
        cli()