# %SystemRoot%\system32\WindowsPowerShell\v1.0\powershell.exe -NoExit -File C:\Users\ya\Desktop\cygwin\home\work\script\power_shell\list_get.ps1

$item_list = "list.txt"
$desktop = [Environment]::GetFolderPath("Desktop")

foreach ($line in get-content $item_list) {

    $array = $line.split("`t")

    $filename = $array[0]
    $filepath = $array[1]
    $length   = $array[2]

    $log = "start copy " + $filename + " " + $length + "MB"
    write-output $log
    copy-item -Path $filepath -Destination $desktop 
}

remove-item -Path $item_list
