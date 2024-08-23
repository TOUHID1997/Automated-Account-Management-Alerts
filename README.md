# Automated Account Management Alerts

This project includes PowerShell and Python scripts to monitor account management activities in a Windows environment and send email alerts for significant events.

## Files
- `MonitorAccountManagement.ps1`: PowerShell script to monitor Windows Event Logs related to account management.
- `AnalyzeAndAlertAccountManagementLogs.py`: Python script to analyze logs and send email alerts.

## Setup
- Schedule the PowerShell script to run at regular intervals using Task Scheduler.
- Schedule the Python script to analyze logs and send alerts.

## Requirements
- Python 3.x
- pandas package (`pip install pandas`)
