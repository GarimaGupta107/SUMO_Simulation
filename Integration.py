import traci
import time
from Script import generate_synthetic_data_limited  # your generator

SUMO_BINARY = "sumo-gui"   # or "sumo"
SUMO_CONFIG = "traffic.sumocfg"  # your SUMO config file

def run_integration():
    traci.start([SUMO_BINARY, "-c", SUMO_CONFIG])
    print("SUMO started successfully")

    vehicle_counter = 0

    try:
        # Run generator for 1 minutes (change as needed)
        for traffic_data in generate_synthetic_data_limited(run_minutes=1):
            print(f"\nInjecting traffic for {traffic_data['timestamp']}")

            for lane, vehicles in traffic_data["lanes"].items():
                # Map lanes to SUMO routes
                route_id = "route_WE" if lane == "W_E" else "route_EW"

                for vtype, count in vehicles.items():
                    for _ in range(count):
                        veh_id = f"{vtype}_{vehicle_counter}"
                        try:
                            traci.vehicle.add(
                                vehID=veh_id,
                                routeID=route_id,
                                typeID=vtype
                            )
                        except traci.TraCIException as e:
                            print(f"Error adding vehicle {veh_id}: {e}")
                        vehicle_counter += 1

            # advance SUMO for 30 simulated seconds
            for _ in range(30):
                traci.simulationStep()
                time.sleep(1)  # real-time delay (optional)

    finally:
        traci.close()
        print("SUMO closed")

if __name__ == "__main__":
    run_integration()
































