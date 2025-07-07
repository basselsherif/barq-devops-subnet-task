# Subnet Analyzer Tool

This project is a **Subnet Analysis and Visualization Tool** developed as part of a DevOps Internship task with Barq Systems. It reads a dataset of IP addresses and subnet masks, performs subnet calculations, generates reports, and visualizes the number of usable hosts per subnet.

## 📁 Project Structure

```
barq-devops-subnet-task/
├── Dockerfile                # (container definition)
├── ip_data.xlsx              # (input dataset)
├── subnet_analyzer.py        # (main script)
├── subnet_report.csv         # (generated output)
├── network_plot.png          # (generated output)
├── libraries.txt             # (python dependencies)
├── report.md                 # (answers to the analysis questions)
└── README.md                 # (project instruction & how to run)
```

## 📌 Features

- Reads `ip_data.xlsx` file
- Calculates:
  - CIDR notation
  - Network address
  - Broadcast address
  - Usable hosts per subnet
- Groups IPs by subnet
- Exports a CSV summary report
- Visualizes usable hosts per subnet in a bar chart
- Containerized using Docker

---

## 🔧 Requirements

### ✅ Local Environment

- OS: Linux-based (e.g. CentOS, RHEL, Ubuntu)
- Python 3.6+
- pip3
- Docker (for containerized execution)

### ✅ Python Dependencies

Install the required packages:

```
pip3 install pandas matplotlib openpyxl
```



---

## 🚀 How to Run

### ▶️ Run Locally (on Host Machine)

1. **Install Python and Dependencies**
    ```bash
    sudo yum install -y python3 python3-pip
    pip3 install pandas matplotlib openpyxl
    ```

2. **Place files in the same folder** and run:
    ```bash
    python3 subnet_analyzer.py
    ```

3. **Output:**
    - `subnet_report.csv` — summary report
    - `network_plot.png` — visualization chart

**Status Before running**

![Image Alt](https://github.com/basselsherif/barq-devops-subnet-task/blob/master/images/Screenshot%20(751).png?raw=true)

**Output after running**

![Image Alt](https://github.com/basselsherif/barq-devops-subnet-task/blob/master/images/Screenshot%20(752).png?raw=true)

![Screenshot (753)](https://github.com/user-attachments/assets/7c7407c9-4494-40b1-8760-1f53c18cc77f)


---

### 🐳 Run with Docker

1. **Install Docker**

    On CentOS:
    ```bash
    sudo yum update -y
    sudo dnf -y install dnf-plugins-core
    sudo dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
    sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y
    sudo systemctl enable --now docker
    ```

2. **Create DockerFile**

    ![Screenshot (757)](https://github.com/user-attachments/assets/53b433d1-60c9-4b4b-aac4-217bf46c6cb0)

   **Note:** 

   Content of `libraries.txt` is python dependencies:

   ```bash
    pandas
    matplotlib
    openpyxl
   ```

3. **Build Docker Image**

    ```bash
    docker build -t subnet-analyzer-img .
    ```
    ![Screenshot (758)](https://github.com/user-attachments/assets/35218327-23fb-4e78-8993-fcc2e846de2a)

4. **Run Docker Container**

    Mount current working directory to the target folder inside the container (/task) to show output files:

    ```bash
    docker container run -v "$PWD":/task subnet-analyzer-img
    ```
    
    ![Screenshot (759)](https://github.com/user-attachments/assets/2b21d6a0-ab50-46f9-b659-305ab6fb96d2)

4. **Check Output**

    After execution, `subnet_report.csv` and `network_plot.png` will appear in your current directory.

    ![Screenshot (760)](https://github.com/user-attachments/assets/be385fe5-6dd9-48f6-b440-f02a48bf22b3)

    ![Screenshot (761)](https://github.com/user-attachments/assets/0fd19213-4168-4b4e-bfe7-d42dceefe85f)

5. **Container that was running**

    ![Screenshot (762)](https://github.com/user-attachments/assets/44e9ff14-0dab-4f10-9f06-61df27e37dbc)







