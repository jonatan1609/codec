from setuptools import setup
from distutils.sysconfig import get_python_lib
from shutil import copy

SITE_PACKAGES = get_python_lib()
copy("my_custom_codec.pth", SITE_PACKAGES + "/" + "my_custom_codec.pth")
setup(
    name="my_custom_codec",
)
