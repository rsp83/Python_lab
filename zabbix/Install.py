# Import the necessary libraries
import os
import subprocess

# Set the Zabbix repository URL
repo_url = "http://repo.zabbix.com/zabbix/4.2/rhel/7/x86_64/zabbix-release-4.2-1.el7.noarch.rpm"

# Install the Zabbix repository
subprocess.run(["yum", "install", "-y", repo_url])

# Install the Zabbix agent
subprocess.run(["yum", "install", "-y", "zabbix-agent"])

# Set the Zabbix server hostname or IP address
server_host = "zabbix.example.com"

# Set the Zabbix server port
server_port = "10051"

# Set the Zabbix hostname for the new host
hostname = "newhost.example.com"

# Set the Zabbix agent configuration file path
agent_config_path = "/etc/zabbix/zabbix_agentd.conf"

# Set the Zabbix agent log file path
agent_log_path = "/var/log/zabbix/zabbix_agentd.log"

# Set the Zabbix agent pid file path
agent_pid_path = "/var/run/zabbix/zabbix_agentd.pid"

# Set the Zabbix agent configuration options
config_options = {
    "Server": server_host,
    "ServerActive": server_host + ":" + server_port,
    "Hostname": hostname,
    "LogFile": agent_log_path,
    "PidFile": agent_pid_path
}

# Write the Zabbix agent configuration options to the configuration file
with open(agent_config_path, "w") as config_file:
    for key, value in config_options.items():
        config_file.write(key + "=" + value + "\n")

# Start the Zabbix agent
subprocess.run(["systemctl", "start", "zabbix-agent"])

# Enable the Zabbix agent to start on boot
subprocess.run(["systemctl", "enable", "zabbix-agent"])