def load_json(json_path):
    import json
    file = open(json_path, encoding="utf8")
    config = json.load(file)
    return config

    