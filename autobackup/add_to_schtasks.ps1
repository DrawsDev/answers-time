# Переменные
$TaskName = "autobackup"
$ScriptPath = Join-Path $PSScriptRoot "autobackup.ps1"
# Проверка прав администратора
if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    exit
}
# Проверка существования задания в планировщике
if (Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue) {
    exit
}
# Создание и запуск задания
$Action = New-ScheduledTaskAction -Execute "PowerShell.exe" -Argument "-File `"$ScriptPath`""
$Trigger = New-ScheduledTaskTrigger -Daily -At "12:00"
$Settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -DontStopOnIdleEnd -RunOnlyIfNetworkAvailable
Register-ScheduledTask -TaskName $TaskName -Action $Action -Trigger $Trigger -Settings $Settings -Force | Out-Null
Start-ScheduledTask -TaskName $TaskName