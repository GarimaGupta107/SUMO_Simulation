import time
import random
from datetime import datetime, timedelta

def generate_synthetic_data_limited(intersection_id="id1", run_minutes=1):
    """
    Generate synthetic traffic data every 30 seconds for a limited time (run_minutes).
    """
    start_time = datetime.strptime("00:00", "%H:%M")
    end_time = start_time + timedelta(minutes=run_minutes)

    current_time = start_time

    while current_time < end_time:
        next_time = current_time + timedelta(seconds=30)
        
        data = {
            "intersection_id": intersection_id,
            "timestamp": f"{current_time.strftime('%H:%M:%S')} - {next_time.strftime('%H:%M:%S')}",
            "lanes": {
                "W_E": {
                    "car": random.randint(0, 10),
                    "bus": random.randint(0, 2),
                    "truck": random.randint(0, 3),
                    "ambulance": random.randint(0, 1)
                },
                "E_W": {
                    "car": random.randint(0, 10),
                    "bus": random.randint(0, 2),
                    "truck": random.randint(0, 3),
                    "ambulance": random.randint(0, 1)
                }
            }
        }

        yield data
        current_time = next_time
        time.sleep(30)  # wait 5 sec before generating next

# ---------------- Example Usage ----------------
if __name__ == "__main__":
    # Run for 2 minutes
    for traffic_data in generate_synthetic_data_limited(run_minutes=1):
        print(traffic_data)






































