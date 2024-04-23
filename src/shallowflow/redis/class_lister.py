from typing import List, Dict


def list_classes() -> Dict[str, List[str]]:
    return {
        "shallowflow.api.actor.Actor": [
            "shallowflow.redis.sinks",
            "shallowflow.redis.sources",
            "shallowflow.redis.standalones",
            "shallowflow.redis.transformers",
        ],
    }
