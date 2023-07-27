import os
import gzip
os.mkdir('MinecraftLogs')
Log_Path=os.environ['appdata']+'\\.minecraft\\logs'
for CompressedLog in os.listdir(Log_Path):
    if CompressedLog.endswith('.gz'):
        with gzip.open(Log_Path+'\\'+CompressedLog, 'rb') as CompressedLogFile:
            with open('MinecraftLogs\\'+CompressedLog.replace('gz','txt'),'wb') as UncompressedLogFile:
                UncompressedLogFile.write(CompressedLogFile.read())
                UncompressedLogFile.close()
        CompressedLogFile.close()
# DrGecko 2023
