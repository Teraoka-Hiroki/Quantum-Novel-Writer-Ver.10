# Gunicorn configuration file
import multiprocessing

# タイムアウトを120秒に設定（Renderの強制タイムアウト100秒に対応するため）
timeout = 120

# ワーカー数（CPUコア数 * 2 + 1 が推奨だが、メモリ制限のある無料枠では少なめに調整）
workers = 2
threads = 4

# ログ出力設定
accesslog = '-'
errorlog = '-'
loglevel = 'info'