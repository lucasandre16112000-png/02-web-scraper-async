' ============================================================================
' Web Scraper PRO V4 - Launcher VBScript
' Clique 2 vezes e tudo funciona sem mostrar console!
' ============================================================================

Set objShell = CreateObject("WScript.Shell")
Set objFSO = CreateObject("Scripting.FileSystemObject")

' Configurações
strUserProfile = objShell.ExpandEnvironmentStrings("%USERPROFILE%")
strProjectDir = strUserProfile & "\02-web-scraper-async"
strBatFile = strProjectDir & "\RODAR_WEB_SCRAPER.bat"

' Verificar se a pasta existe
If objFSO.FolderExists(strProjectDir) Then
    ' Rodar arquivo batch em background (sem mostrar console)
    objShell.Run strBatFile, 0, False
Else
    ' Se não existe, clonar primeiro
    strCloneCmd = "cmd /c cd " & strUserProfile & " && git clone https://github.com/lucasandre16112000-png/02-web-scraper-async.git && " & strBatFile
    objShell.Run strCloneCmd, 0, False
End If

' Aguardar mais tempo para evitar duplicacao
WScript.Sleep(8000)
