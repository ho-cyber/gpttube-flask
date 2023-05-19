import pickle
from typing import Optional

file_path = "data.json"

__cache = None


def init_cache():
    global __cache

    try:
        with open('data.pickle', 'rb') as f:
            __cache = pickle.load(f)
    except:
        __cache = dict(())


def cache_get(key: str) -> Optional[str]:
    global __cache

    if __cache is None:
        init_cache()

    try:
        return __cache[key]
    except:
        print(f"Error cache key: {key} not found!")
        return None


def cache_set(key: str, data: str) -> None:
    global __cache

    if __cache is None:
        init_cache()
        # __cache = dict(())

    __cache[key] = data

    with open('data.pickle', 'wb') as f:
        pickle.dump(__cache, f)
