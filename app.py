from encoder.encoder import Base64EncoderStrategy
from minifyer.minifyer import Minifyer

if __name__ == "__main__":
    minifyier = Minifyer(Base64EncoderStrategy())

    x = minifyier.minify("www.google2.com")
    print(x)
    x = minifyier.deminify(x)
    print(x)