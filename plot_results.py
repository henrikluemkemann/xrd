import csv
import matplotlib.pyplot as plt

def plot_results(csv_file):
    users = []
    latencies = []

    # Read the CSV file
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            users.append(int(row[0]))
            latencies.append(float(row[1]) / 1000)  # Convert ms to seconds


    max_users = max(users)
    max_latency = max(latencies)
    user_limit = max_users * 1.1  # Extend x-axis slightly
    latency_limit = max_latency * 1.1  # Extend y-axis slightly


    plt.figure(figsize=(10, 6))
    plt.plot(users, latencies, marker='o', linestyle='-', color='b')
    plt.xlabel("Number of Users")
    plt.ylabel("Latency (seconds)")
    plt.title("Latency vs Number of Users")
    plt.grid(True)
    plt.xlim(0, user_limit)
    plt.ylim(0, latency_limit)
    plt.tight_layout()


    plt.savefig("latency_plot.png")
    plt.show()


plot_results("result.csv") # This file will be plotted, change file name accordingly