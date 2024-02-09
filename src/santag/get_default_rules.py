from santag.domain_model.rules import Rules, Substitution
from santag.settings.default_rules import SUBSTITUTIONS


def get_default_rules() -> Rules:
    return Rules(
        substitutions=[
            Substitution(*sub)
            for sub in SUBSTITUTIONS
        ]
    )
