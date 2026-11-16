Set WshShell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")
strPath = fso.GetParentFolderName(WScript.ScriptFullName)

' Open browser to http://localhost:3000
WshShell.Run "cmd /c start http://localhost:3000", 0, False

' Run node server.js silently in background without window
WshShell.CurrentDirectory = strPath & "\UniBo-Study-App"
WshShell.Run "node server.js", 0, False

