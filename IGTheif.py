import yt_dlp
import re

def baixar_reel_instagram(url):
    try:
        ydl_opts = {
            'format': 'mp4',
            'merge_output_format': 'mp4',
            'outtmpl': '%(title)s.%(ext)s',
            'quiet': True,
            'skip_download': True,
        }
        
        pattern = re.compile(r'https://(www\.)?instagram\.com/reel/.+')
        if not isinstance(url, str) or not pattern.search(url):
            print("Deu coiso na tua URL do Insta. Confere se é um reel público ou se é problema de BIOS.")
            return

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            titulo = info.get('description', '').split('\n')[0]

        if not titulo:
            print("Não deu pra pegar o título do reel.")
            return

        ydl_opts['outtmpl'] = f"{titulo}.mp4"
        ydl_opts['skip_download'] = False

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print(f"Download concluído: {titulo}.mp4")

    except Exception as e:
        print("Ocorreu um erro:", e)

urls = ["https://www.instagram.com/reel/DCPr1cTSN9B/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA=="]

for url in urls:
    baixar_reel_instagram(url)
