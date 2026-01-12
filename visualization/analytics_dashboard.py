import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_parquet("data/gold")

for api in df["api_name"].unique():
    subset = df[df["api_name"] == api]
    plt.plot(subset["window"]["start"], subset["avg_latency"], label=api)

plt.legend()
plt.title("API Latency Trends")
plt.show()
