import pandas as pd
import ipaddress
import matplotlib.pyplot as plt


input_file = "ip_data.xlsx"
df = pd.read_excel(input_file)


summary = []

for index, row in df.iterrows():
    ip_str = row['IP Address']
    subnet_mask = row['Subnet Mask']

    network = ipaddress.IPv4Network(f"{ip_str}/{subnet_mask}", strict=False)


    cidr_notation = network.with_prefixlen
    network_address = str(network.network_address)
    broadcast_address = str(network.broadcast_address)
    num_usable_hosts = network.num_addresses - 2 if network.num_addresses > 2 else 0

    summary.append({
        "IP": ip_str,
        "Subnet Mask": subnet_mask,
        "Subnet/CIDR": cidr_notation,
        "Network Address": network_address,
        "Broadcast Address": broadcast_address,
        "Usable Hosts": num_usable_hosts
    })

summary_df = pd.DataFrame(summary)

grouped_df = summary_df.groupby("Subnet/CIDR").size().reset_index(name="grouped_ips_num")

summary_df = summary_df.merge(grouped_df, on="Subnet/CIDR", how="left")

summary_df.to_csv("subnet_report.csv", index=False)
print("subnet_report.csv done")



plt.figure(figsize=(10, 6))
plt.bar(grouped_df["Subnet/CIDR"], summary_df["Usable Hosts"], color='blue')
plt.xticks(rotation=90, ha='right')
plt.xlabel("Subnet")
plt.ylabel("Number of usable hosts")
plt.title("Number of usable hosts per Subnet")
plt.tight_layout()
plt.savefig("network_plot.png")
plt.show()
print("network_plot.png done")
