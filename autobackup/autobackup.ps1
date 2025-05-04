# Переменные
$7z = "$PSScriptRoot\7-Zip\7z.exe"
$Log7z = Join-Path $PSScriptRoot "log7z.log"
$Include = Join-Path $PSScriptRoot "include.txt"
$Exclude = Join-Path $PSScriptRoot "exclude.txt"
$Backups = Join-Path $PSScriptRoot "backups"
$CompressionLevel = 1
$CopiesToKeep = 7
$Password = "admin"
# Архивация
$Timestamp = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
$ArchiveName = "backup_$Timestamp.7z"
$ArchivePath = Join-Path $Backups $ArchiveName
& $7z a -t7z $ArchivePath "@$Include" "-xr@$Exclude" "-p$Password" "-mx$CompressionLevel" -scsWIN -ssw | Out-File $Log7z -Append
# Удаление устаревших архивов
Get-ChildItem $Backups\backup_*.7z | Sort-Object CreationTime -Descending | Select-Object -Skip $CopiesToKeep | Remove-Item -Force