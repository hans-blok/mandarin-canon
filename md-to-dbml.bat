@echo off
:: md-to-dbml.bat — Convert a Mandarin .md erDiagram to DBML
::
:: Usage:
::   md-to-dbml.bat                                 (uses default: tdm_mandarin.md)
::   md-to-dbml.bat path\to\model.md
::   md-to-dbml.bat path\to\model.md --output path\to\output.dbml

python "%~dp0scripts\md_to_dbml.py" %*
