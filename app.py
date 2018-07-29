import argparse

from encoder.encoder import Base64EncoderStrategy
from minifyer.minifyer import Minifyer

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Minify url")
    parser.add_argument("--url", type=str, required=True, help="Url to minify")
    parser.add_argument("--action", type=str, default="minify", choices=["minify", "deminify"])
    args = parser.parse_args()

    minifyier = Minifyer(Base64EncoderStrategy())

    actions_mapping = {
        "minify": minifyier.minify,
        "deminify": minifyier.deminify
    }

    result = actions_mapping[args.action](args.url)
    print(result)