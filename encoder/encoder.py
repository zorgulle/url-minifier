import base64


class StringEncoding:
    @staticmethod
    def encode(to_encode):
        return to_encode.encode("utf-8")
    @staticmethod
    def decode(to_decode):
        return to_decode.decode("utf-8")


class Encoder:
    @staticmethod
    def encode(to_encode):
        raise NotImplementedError
    @staticmethod
    def decode(to_decode):
        raise NotImplementedError


class Base64EncoderStrategy(Encoder):
    @staticmethod
    def encode(to_encode):
        encoded_string = StringEncoding.encode(to_encode)
        base_64_encoded_id = base64.standard_b64encode(encoded_string)
        decoded_string = StringEncoding.decode(base_64_encoded_id)

        return decoded_string

    @staticmethod
    def decode(to_decode):
        encoded_string = StringEncoding.encode(to_decode)
        base_64_decoded_id = base64.standard_b64decode(encoded_string)
        decoded_string = StringEncoding.decode(base_64_decoded_id)

        return decoded_string