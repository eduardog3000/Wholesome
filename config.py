import toml
from typing import Union, List

class Config:
    token: str
    prefix: Union[str, List[str]]
    colors: List[int]

    def __getitem__(self, item):
        raise KeyError

    def __setitem__(self, key, value):
        self.__dict__[key] = value

config: Config = toml.load('config.toml', _dict=Config)
