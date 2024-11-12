import yt_dlp
import re

def baixar_reel_instagram(url):
    try:
        ydl_opts = {
            'format': 'mp4',
            'outtmpl': '%(title)s.%(ext)s',
            'merge_output_format': 'mp4',
        }
        
        pattern = re.compile(r'https://(www\.)?instagram\.com/reel/.+')
        if not pattern.search(url):
            print("Deu coiso na tua URL do Insta. Confere se é um reel público ou se é problema de BIOS.")
            return

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        print("Download concluído!")

    except Exception as e:
        print("Ocorreu um erro:", e)

url = ["https://www.instagram.com/reel/DCPr1cTSN9B/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA=="]
baixar_reel_instagram(url)
