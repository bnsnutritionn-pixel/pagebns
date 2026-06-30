@echo off
cd /d "e:\LANDING PAGE BNS"
echo ================================================== >> sync_log.txt
echo [%date% %time%] Iniciando sincronizacao de precos... >> sync_log.txt
python sync_prices.py >> sync_log.txt 2>&1
echo [%date% %time%] Processo finalizado. >> sync_log.txt
echo ================================================== >> sync_log.txt
