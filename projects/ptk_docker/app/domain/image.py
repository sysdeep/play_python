from dataclasses import dataclass


@dataclass
class Image:
    uid: str
    short_uid: str
    tags: list[str]
    size: int
    created: str
