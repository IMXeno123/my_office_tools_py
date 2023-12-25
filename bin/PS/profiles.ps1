oh-my-posh init pwsh --config 'C:\Users\username\AppData\Local\Programs\oh-my-posh\themes\blue-owl.omp.json' | Invoke-Expression

# my code!
function music {
	param (
		[Parameter(Mandatory=$false)]
		[string]$str1
	)
	$qqmusicpath = ".\Music.exe"
	if ($str1 -eq "--help" -or $str1 -eq "--h" -or $str1 -eq "help") {
		echo "No music No life! Trun music on! "
	} else {
		Start-Process $qqmusicpath
		Write-Output "Music Started!"
		return $true
	}
}