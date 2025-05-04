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
# Создание задания
$action = New-ScheduledTaskAction -Execute $ScriptPath
$trigger = New-ScheduledTaskTrigger -Daily -At "12:00"
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -DontStopOnIdleEnd -RunOnlyIfNetworkAvailable
Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger -Settings $settings -Force | Out-Null