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

# Get the ID and security principal of the current user account
$myWindowsID=[System.Security.Principal.WindowsIdentity]::GetCurrent()
$myWindowsPrincipal=new-object System.Security.Principal.WindowsPrincipal($myWindowsID)
 
# Get the security principal for the Administrator role
$adminRole=[System.Security.Principal.WindowsBuiltInRole]::Administrator
 
# Check to see if we are currently running "as Administrator"
if ($myWindowsPrincipal.IsInRole($adminRole))
   {
   # We are running "as Administrator" - so change the title and background color to indicate this
   $Host.UI.RawUI.WindowTitle = $myInvocation.MyCommand.Definition + "(Elevated)"
   $Host.UI.RawUI.BackgroundColor = "DarkBlue"
   clear-host
   }
else
   {
   # We are not running "as Administrator" - so relaunch as administrator
   
   # Create a new process object that starts PowerShell
   $newProcess = new-object System.Diagnostics.ProcessStartInfo "PowerShell";
   
   # Specify the current script path and name as a parameter
   $newProcess.Arguments = $myInvocation.MyCommand.Definition;
   
   # Indicate that the process should be elevated
   $newProcess.Verb = "runas";
   
   # Start the new process
   [System.Diagnostics.Process]::Start($newProcess);
   
   # Exit from the current, unelevated, process
   exit
   }
 
# Run your code that needs to be elevated here
# Write-Host -NoNewLine "Press any key to continue..."
# $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")



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