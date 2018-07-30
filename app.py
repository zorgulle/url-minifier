import argparse

from encoder.encoder import Base64EncoderStrategy
from minifyer.minifyer import Minifyer
from settings.settings import get_config


def get_arguments():
    global args
    parser = argparse.ArgumentParser("Minify url")
    parser.add_argument("--url", type=str, required=True, help="Url to minify")
    parser.add_argument("--action", type=str, default="minify", choices=["minify", "deminify"])
    parser.add_argument("--config", type=str, default="dev.json", help="Config file")
    args = parser.parse_args()


if __name__ == "__main__":
    get_arguments()

    get_config(args.config)

    minifyier = Minifyer(Base64EncoderStrategy())

    actions_mapping = {
        "minify": minifyier.minify,
        "deminify": minifyier.deminify
    }

    result = actions_mapping[args.action](args.url)
    print(result)