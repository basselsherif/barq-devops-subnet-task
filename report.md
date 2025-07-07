# Network Subnet Analysis Report

## Executive Summary

This report analyzes 25 IP addresses across various subnets to identify capacity utilization, potential overlaps, and optimization opportunities. The analysis reveals significant variations in subnet sizes and potential for IP address space optimization.

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

All subnets in the analysis are properly configured with distinct network address ranges. Each subnet maintains its own isolated address space without any conflicts or overlaps. This indicates good network planning and CIDR block allocation.

## Question 3: What is the smallest and largest subnet in terms of address space?

**Largest Subnets**: 
- **Size**: /22 subnets with 1,022 usable hosts each
- **Count**: 8 subnets
- **Address Space**: 1,024 total addresses per subnet (including network and broadcast)

**Smallest Subnets**:
- **Size**: /24 subnets with 254 usable hosts each
- **Count**: 14 subnets
- **Address Space**: 256 total addresses per subnet (including network and broadcast)

**Medium Subnets**:
- **Size**: /23 subnets with 510 usable hosts each
- **Count**: 3 subnets
- **Address Space**: 512 total addresses per subnet

## Question 4: Suggest a Subnetting Strategy that could reduce wasted IPs in this network.

### Current State Analysis
The network shows a binary approach to subnetting with only three subnet sizes:
- 8 × /22 subnets (1,022 hosts each) = 8,176 total hosts
- 3 × /23 subnets (510 hosts each) = 1,530 total hosts  
- 14 × /24 subnets (254 hosts each) = 3,556 total hosts
- **Total Available Host Addresses**: 13,262

### Optimization Recommendations

#### 1. **Implement Variable Length Subnet Masking (VLSM)**
Instead of using only /22, /23, and /24 subnets, implement a more granular approach:

- **Small Networks (1-30 hosts)**: Use /27 subnets (30 hosts)
- **Medium Networks (31-62 hosts)**: Use /26 subnets (62 hosts)
- **Large Networks (63-126 hosts)**: Use /25 subnets (126 hosts)
- **Very Large Networks (127-254 hosts)**: Use /24 subnets (254 hosts)
- **Enterprise Networks (255+ hosts)**: Use /23 or /22 only when justified

#### 2. **Conduct Host Utilization Assessment**
- Audit actual host count per subnet
- Monitor growth trends over 6-12 months
- Right-size subnets based on actual usage plus 20-30% growth buffer

#### 3. **Consolidation Strategy**
- **Merge underutilized /22 subnets**: If multiple /22 subnets have <200 active hosts, consider consolidating
- **Split oversized /24 subnets**: If /24 subnets consistently use <100 hosts, consider /25 or /26

#### 4. **Address Space Hierarchy**
Implement a structured approach by network class:

**Class A (10.x.x.x) - Internal Networks**:
- Reserve /22 for data centers and server farms
- Use /24-/25 for department networks
- Use /26-/27 for small branch offices

**Class B (172.16.x.x) - DMZ/External Services**:
- Use /24 for web servers and external services
- Use /26-/27 for specific service clusters

**Class C (192.168.x.x) - End-User Networks**:
- Use /25-/26 for office networks
- Use /27-/28 for small remote locations

#### 5. **Potential Savings**
With proper rightsizing, estimated IP address waste reduction:
- **Conservative estimate**: 30-40% reduction in allocated but unused addresses
- **Aggressive optimization**: 50-60% reduction with proper VLSM implementation

### Implementation Priority
1. **High Priority**: Audit current utilization rates
2. **Medium Priority**: Implement VLSM for new subnet assignments
3. **Low Priority**: Gradually migrate existing oversized subnets during maintenance windows

## Conclusion

The current network demonstrates good segregation practices with no overlapping subnets. However, the limited subnet size options (only /22, /23, /24) suggest significant potential for optimization. Implementing VLSM and conducting utilization audits could substantially reduce IP address waste while maintaining network performance and future growth capacity.

