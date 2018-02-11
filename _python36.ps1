# REM https://www.technlg.net/windows/download-windows-resource-kit-tools/
# REM echo @off
# pathman /rs C:\Python27\
# pathman /rs C:\Python27\Scripts\
# echo "done"
# $path.Split(";") | where {$_ -like "*Python*"}
# $path = ($env:Path)  
# $path = ($path.Split(";") | where {$_ -NotLike "*Python*"}) -join ";"
# $env:Path = $path
# https://stackoverflow.com/questions/39010405/powershell-how-to-delete-a-path-in-path-environment-variable
# Get it
$path = [System.Environment]::GetEnvironmentVariable(
'PATH',
'Machine'
)
# Remove unwanted elements
$path = ($path.Split(';') | Where-Object { $_ -NotLike "*Python*" }) -join ';'

$path = $path+";C:\Python27\;C:\Python27\Scripts\;"

# Set it
[System.Environment]::SetEnvironmentVariable(
'PATH',
$path,
'Machine'
)

$path.Split(";") 