import json
import random
import time
from datetime import datetime
from pathlib import Path

OUTPUT = Path("data/input")
OUTPUT.mkdir(parents=True, exist_ok=True)

APIS = ["login", "search", "checkout", "payment", "profile"]
STATUS = [200, 200, 200, 400, 401, 500]

def generate_event():
    return {
        "event_id": random.randint(1_000_000, 9_999_999),
        "timestamp": datetime.utcnow().isoformat(),
        "api_name": random.choice(APIS),
        "response_time_ms": abs(int(random.gauss(250, 120))),
        "status_code": random.choice(STATUS),
        "user_id": random.randint(1000, 5000)
    }

while True:
    batch = [generate_event() for _ in range(300)]
    file = OUTPUT / f"api_logs_{int(time.time())}.json"
    with open(file, "w") as f:
        for row in batch:
            f.write(json.dumps(row) + "\n")
    print(f"Wrote {len(batch)} events")
    time.sleep(3)
