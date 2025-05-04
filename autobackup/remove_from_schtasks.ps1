# Переменные
$TaskName = "autobackup"
# Проверка прав администратора
if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    exit
}
# Проверка существования задания в планировщике
if (-not (Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue)) {
    exit
}
# Удаление задания
Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false