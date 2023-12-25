oh-my-posh init pwsh --config 'C:\Users\zzxxe\AppData\Local\Programs\oh-my-posh\themes\blue-owl.omp.json' | Invoke-Expression

# my code
function qqmusic {
	param (
		[Parameter(Mandatory=$false)]
		[string]$str1
	)
	$qqmusicpath = "D:\Program Files (x86)\Tencent\QQMusic\QQMusic2003.08.40.11\QQMusic.exe"
	if ($str1 -eq "--help") {
		echo "No music No life! Trun music on! "
	} else {
		Start-Process $qqmusicpath
		echo "QQMusic Started!"
	}
}