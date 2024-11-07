import yt_dlp

def baixar_video(url):
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': '%(title)s.%(ext)s'
        }
        
        if not url.startswith("https://www.youtube.com/watch"):
            print("Tá dando ruim aqui, testando a url correta.")
            return

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        print("Download concluído!")

    except Exception as e:
        print("Deu um erro:", e)

url = "https://www.youtube.com/watch?v=EF889gHjZu8"
baixar_video(url)
 
# test url video below
# https://www.youtube.com/watch?v=EF889gHjZu8