import os

def deploy_to_network(network_name):
    print(f"Starting deployment process for {network_name}...")
    # Simulation of deployment logic
    status = "Success"
    return f"Deployment to {network_name}: {status}"

if __name__ == "__main__":
    networks = ["Base-Sepolia", "Ethereum-Mainnet", "Optimism"]
    for net in networks:
        print(deploy_to_network(net))
