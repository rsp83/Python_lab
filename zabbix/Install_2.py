# Import the necessary libraries
import os
import subprocess

# Set the Zabbix repository URL
repo_url = "http://repo.zabbix.com/zabbix/6.0/rhel/7/x86_64/zabbix-release-6.0-1.el7.noarch.rpm"

# Install the Zabbix repository
subprocess.run(["yum", "install", "-y", repo_url])

# Install the Zabbix agent version 6
subprocess.run(["yum", "install", "-y", "zabbix-agent-6.0"])

# Set the Zabbix server hostname or IP address
server_host = "zabbix.copacol.com.br"

# Set the Zabbix hostname for the new host
hostname = "HOSTNAME_SERVIDOR"

# Set the Zabbix agent configuration file path
agent_config_path = "/etc/zabbix/zabbix_agentd.conf"

# Set the Zabbix agent log file path
agent_log_path = "/var/log/zabbix/zabbix_agentd.log"

# Set the Zabbix agent pid file path
agent_pid_path = "/run/zabbix/zabbix_agentd.pid"

# Set the Zabbix agent listen port
listen_port = "11050"

# Set the number of Zabbix agents to start
start_agents = "3"

# Set the Zabbix agent configuration options
config_options = {
    "Server": server_host,
    "Hostname": hostname,
    "PidFile": agent_pid_path,
    "LogFile": agent_log_path,
    "ListenPort": listen_port,
    "StartAgents": start_agents
}

# Write the Zabbix agent configuration options to the configuration file
with open(agent_config_path, "w") as config_file:
    for key, value in config_options.items():
        config_file.write(key + "=" + value + "\n")

# Start the Zabbix agent
subprocess.run(["systemctl", "start", "zabbix-agent"])

# Enable the Zabbix agent to start on boot
subprocess.run(["systemctl", "enable", "zabbix-agent"])
