Function sed($Filename, $Oldvalue, $Newvalue)
{
    if (Test-Path $Filename) {
        $content = get-content $Filename
        clear-content $Filename
        foreach($line in $content) {
            $liner=$line.Replace($Oldvalue, $Newvalue)
            Add-content $Filename -Value $liner
        }
    }
}


pyside6-uic .\src\ui\application.ui -o .\src\ui\ui_application.py

pyside6-rcc .\src\ui\resource.qrc -o .\src\ui\ui_resource.py
sed "./src/ui/ui_application.py" "import resource_rc" "import ui.ui_resource"