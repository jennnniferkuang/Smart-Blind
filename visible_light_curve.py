import pandas as pd
import matplotlib.pyplot as plt


# Load the CSV file
file_path = "average_light_values.csv"  # update path if needed
df = pd.read_csv(file_path)

# Convert current_time column to datetime
df["current_time"] = pd.to_datetime(df["current_time"])

# Plot Visible curve
plt.figure(figsize=(10, 5))
plt.plot(df["current_time"], df["average_visible"], label="Average Visible", color="blue")

# Mark each value point with a red star
plt.scatter(df["current_time"], df["average_visible"], color="red", marker=".", s=50, label="Value Points")

plt.title("Visible Curve Over Time")
plt.xlabel("Time")
plt.ylabel("Visible Value")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()
