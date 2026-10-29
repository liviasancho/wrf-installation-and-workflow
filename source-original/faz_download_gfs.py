import os
import time
import requests
import urllib3
from datetime import datetime, timedelta
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# --- INPUTS E CONFIGURAÇÕES NO INÍCIO ---
START_DATE = datetime(2022, 1, 1, 0)
END_DATE   = datetime(2022, 1, 31, 18)
INTERVAL_HOURS = 6

# 430 MB em bytes (Critério de arquivo íntegro)
MIN_SIZE_BYTES = 420 * 1024 * 1024

# Configurações do Monitor de Velocidade
LOW_SPEED_THRESHOLD = 500 * 1024  # 500 KB/s (Abaixo disso, ele reseta)
LOW_SPEED_TIMEOUT = 20            # Segundos de tolerância para velocidade baixa

# Silenciar avisos de SSL (Certificado expirado da RDA)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def download_file(url, ofile):
    session = requests.Session()
    # Retenta automaticamente em erros de servidor (500, 502, etc)
    retries = Retry(total=3, backoff_factor=2, status_forcelist=[500, 502, 503, 504])
    session.mount('https://', HTTPAdapter(max_retries=retries))

    print(f"🚀 Baixando {ofile}...", end=" ", flush=True)

    try:
        # verify=False ignora o erro de SSL do servidor
        with session.get(url, stream=True, timeout=(15, 45), verify=False) as r:
            r.raise_for_status()
            with open(ofile, 'wb') as f:
                start_time = time.time()
                downloaded_in_period = 0

                for chunk in r.iter_content(chunk_size=1024 * 1024): # 1MB chunks
                    if chunk:
                        f.write(chunk)
                        downloaded_in_period += len(chunk)

                        # Monitor de Performance
                        elapsed = time.time() - start_time
                        if elapsed > LOW_SPEED_TIMEOUT:
                            speed = downloaded_in_period / elapsed
                            if speed < LOW_SPEED_THRESHOLD:
                                raise Exception(f"Stalling detectado ({speed/1024:.1f} KB/s)")

                            # Reseta cronômetro para o próximo bloco de análise
                            start_time = time.time()
                            downloaded_in_period = 0

        print("concluído!")
        return True
    except Exception as e:
        print(f"\n⚠️ Falha na tentativa: {e}")
        # Remove arquivo parcial para não corromper a próxima tentativa
        if os.path.exists(ofile):
            os.remove(ofile)
        return False

# --- FLUXO DE EXECUÇÃO ---

# Gerar lista de URLs baseada nos inputs do topo
hours_diff = int((END_DATE - START_DATE).total_seconds() / 3600)
date_list = [START_DATE + timedelta(hours=x) for x in range(0, hours_diff + 1, INTERVAL_HOURS)]

filelist = []
for date in date_list:
    #url = (f"https://data-osdf.rda.ucar.edu/ncar/rda/d083003/{date.strftime('%Y')}/"
    #      f"{date.strftime('%Y%m')}/gdas1.fnl0p25.{date.strftime('%Y%m%d%H')}.f00.grib2")
    url = (f"https://osdf-director.osg-htc.org/ncar/gdex/d083003/{date.strftime('%Y')}/"
           f"{date.strftime('%Y%m')}/gdas1.fnl0p25.{date.strftime('%Y%m%d%H')}.f00.grib2")
    filelist.append(url)

print(f"--- Iniciando processamento de {len(filelist)} arquivos ---")

for url in filelist:
    ofile = os.path.basename(url)

    # Verificação de arquivo existente e tamanho
    if os.path.exists(ofile):
        file_size = os.path.getsize(ofile)
        file_size_mb = file_size / (1024 * 1024)

        if file_size >= MIN_SIZE_BYTES:
            print(f"✅ {ofile} já existe e está íntegro ({file_size_mb:.1f} MB). Pulando...")
            continue
        else:
            print(f"⚠️ {ofile} encontrado mas está incompleto ({file_size_mb:.1f} MB).")

    # Sistema de tentativas para vencer a lentidão do servidor
    success = False
    attempts = 0
    while not success and attempts < 5:
        attempts += 1
        success = download_file(url, ofile)
        if not success and attempts < 5:
            print(f"🔄 Reiniciando conexão (Tentativa {attempts+1}/5)...")
            time.sleep(3) # Pausa amigável para o servidor

print("--- Processo finalizado! ---")