from codecs import register, CodecInfo
from encodings import utf_8
from .codec.codec import IncrementalDecoder, decode


def search_function(encoding):
    if encoding == "my_custom_encoding":
        return CodecInfo(
            name="my_custom_encoding",
            encode=utf_8.encode,
            decode=decode,
            incrementaldecoder=IncrementalDecoder
        )


register(search_function)
