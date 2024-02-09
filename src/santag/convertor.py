from collections.abc import Iterable

from santag.domain_model.rules import Rules


def convert(lines: Iterable[str], rules: Rules) -> Iterable[str]:
    for line in lines:
        new_line = line
        for sub in rules.substitutions:
            new_line = new_line.replace(sub.old, sub.new)
        yield new_line
