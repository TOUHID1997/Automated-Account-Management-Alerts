# MonitorAccountManagement.ps1

# Define the path to save the log file
$logFilePath = "C:\Logs\AccountManagementLogs.csv"

# Define the Event IDs related to account management:
$eventIDs = @(4720, 4726, 4732, 4728, 4723)

# Get the account management events
Get-WinEvent -FilterHashtable @{
    LogName = 'Security'
    Id = $eventIDs
} | Select-Object TimeCreated, Id, LevelDisplayName, Message |
    Export-Csv -Path $logFilePath -NoTypeInformation

Write-Host "Account management events have been logged to $logFilePath"
