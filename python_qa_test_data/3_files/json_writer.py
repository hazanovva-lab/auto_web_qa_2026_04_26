import json

data = {
    "users": [
        {"name": "Anton", "skill": 200, "gold": 500},
        {"name": "Sergey", "skill": 250, "gold": 1000}
    ]
}

with open("example.json", "w") as f:
    json.dump(data, f, indent=4)