from setuptools import setup, find_packages

setup(
    name="big_vision",
    version="1.0.0",
    author="Google-Research",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.26",
        "absl-py",
        # "CommonLoopUtils @ git+https://github.com/google/CommonLoopUtils",
        "distrax",
        "einops",
        "flax",
        "optax",
        "flaxformer @ git+https://github.com/google/flaxformer",
        "panopticapi @ git+https://github.com/akolesnikoff/panopticapi.git@mute",
        "overrides",
        "protobuf",
        "sentencepiece",
        "tensorflow-cpu",
        "tfds-nightly",
        "tensorflow-text",
        "tensorflow-gan"
    ]
)
