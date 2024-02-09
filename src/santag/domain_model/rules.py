from collections.abc import Sequence
from dataclasses import dataclass
from typing import NamedTuple


class Substitution(NamedTuple):
    old: str
    new: str


@dataclass(frozen=True)
class Rules:
    substitutions: Sequence[Substitution]
