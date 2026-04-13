@echo off
:: conv-to-graphml.bat — Volledige pipeline: .md → .dbml → .graphml
::
:: Gebruik:
::   conv-to-graphml.bat path\to\model.md
::
:: Stap 1: md_to_dbml.py   — selecteert het mermaid classDiagram-blok en schrijft <naam>.dbml
:: Stap 2: dbml_to_graphml.py — leest <naam>.dbml en schrijft <naam>.graphml
:: Beide bestanden landen naast het invoerbestand.

SET "SCRIPTS=%~dp0scripts"

IF "%~1"=="" (
    echo Gebruik: conv-to-graphml.bat path\to\model.md
    exit /b 1
)

SET "SOURCE=%~1"
FOR %%F IN ("%SOURCE%") DO SET "DBML=%%~dpnF.dbml"

python "%SCRIPTS%\md_to_dbml.py" "%SOURCE%"
IF ERRORLEVEL 1 GOTO :error

python "%SCRIPTS%\dbml_to_graphml.py" "%DBML%"
IF ERRORLEVEL 1 GOTO :error

GOTO :end

:error
echo.
echo [FOUT] Pipeline gestopt.
exit /b 1

:end
