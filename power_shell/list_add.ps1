# Set-ExecutionPolicy RemoteSigned
# /cygdrive/c/Users/ya/AppData/Roaming/Microsoft/Windows/SendTo
# %SystemRoot%\system32\WindowsPowerShell\v1.0\powershell.exe -File C:\Users\ya\Desktop\cygwin\home\work\script\power_shell\list_add.ps1

$item_list = "list.txt"
foreach ($item in $args) {
    $file = get-item $item
    $length = [math]::round($file.length / 1024 / 1024)
    $record = $file.name + "`t" + $file.fullname + "`t" + $length

    write-output $record >> $item_list
}

