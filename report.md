# Network Subnet Analysis Report


## Data Overview

The network contains 25 IP addresses distributed across different subnet configurations:
- **Total Subnets Analyzed**: 25 unique IP addresses
- **Subnet Size Range**: /22 to /24 (1022 to 254 usable hosts)


## Question 1: Which subnet has the most hosts?

**Answer**: Multiple subnets have the largest capacity with **1,022 usable hosts each**.

The following /22 subnets have the maximum host capacity:
- `192.168.100.0/22` (IP: 192.168.100.7)
- `10.2.0.0/22` (IP: 10.2.1.56)
- `172.16.48.0/22` (IP: 172.16.50.1)
- `10.20.4.0/22` (IP: 10.20.4.6)
- `192.168.20.0/22` (IP: 192.168.20.44)
- `10.3.0.0/22` (IP: 10.3.3.9)
- `172.16.60.0/22` (IP: 172.16.60.30)
- `10.15.4.0/22` (IP: 10.15.5.50)

## Question 2: Are there any overlapping subnets?

**Answer**: No overlapping subnets were detected.

All subnets in the analysis are configured with distinct network address ranges. Each subnet maintains its own isolated address space without any conflicts or overlaps.

## Question 3: What is the smallest and largest subnet in terms of address space?

**Largest Subnets**: 
- **Size**: /22 subnets with 1,022 usable hosts each
- **Count**: 8 subnets
- **Address Space**: 1,024 total addresses per subnet (including network and broadcast)

**Smallest Subnets**:
- **Size**: /24 subnets with 254 usable hosts each
- **Count**: 14 subnets
- **Address Space**: 256 total addresses per subnet (including network and broadcast)


## Question 4: Suggest a Subnetting Strategy that could reduce wasted IPs in this network.

### Current State Analysis
The network shows a binary approach to subnetting with only three subnet sizes:
- 8 × /22 subnets (1,022 hosts each) = 8,176 total hosts
- 3 × /23 subnets (510 hosts each) = 1,530 total hosts  
- 14 × /24 subnets (254 hosts each) = 3,556 total hosts
- **Total Available Host Addresses**: 13,262

### Optimization Recommendations

#### 1. **Implement Variable Length Subnet Masking (VLSM)**
Instead of using only /22, /23, and /24 subnets:

- **Small Networks (1-30 hosts)**: Use /27 subnets (30 hosts)
- **Medium Networks (31-62 hosts)**: Use /26 subnets (62 hosts)
- **Large Networks (63-126 hosts)**: Use /25 subnets (126 hosts)
- **Very Large Networks (127-254 hosts)**: Use /24 subnets (254 hosts)
- **Enterprise Networks (255+ hosts)**: Use /23 or /22 only when justified


## Conclusion

The current network shows good practices with no overlapping subnets. However, the limited subnet size options (only /22, /23, /24) suggest significant potential for optimization. Implementing VLSM reduce IP address waste while maintaining network performance and future growth capacity.

