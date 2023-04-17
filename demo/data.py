"""_summary_
"""

from dataclasses import dataclass, asdict


@dataclass
class DataModel:
    ID: str
    VALUE: int

    @property
    def as_dict(self):
        return asdict(self)


if __name__ == "__main__":
    dm = DataModel(ID=1, VALUE=2)

    print(dm)
    print(dm.as_dict)
