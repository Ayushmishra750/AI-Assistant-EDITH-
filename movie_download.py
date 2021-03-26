import requests
import subprocess
import sys
from bs4 import BeautifulSoup as soup

def main():
    movie_name = input("Enter the movie name:\n")
    print(f"Searching for {movie_name}")
    base_url = f"https://api.sumanjay.cf/torrent/?query={movie_name}"
    index = 1
    magnet = []
    try:
        torrent_results = requests.get(url=base_url).json()
        for result in torrent_results:
            print(index, ") ", result['name'], "-->", result['size'] , "Seeder -->" , result['seeder'])
            index += 1
            magnet.append(result['magnet']) 
        
        if magnet:
            choice = int(
                input("Enter the index of the movie which you want to stream\n"))
            try:
                magnet_link = magnet[choice-1]
                download = False
                stream_choice = int(
                    input("Press 1 to stream or Press 2 to download the movie\n"))
                if stream_choice == 2:
                    download = True

                webtorrent_stream(magnet_link, download)
            except IndexError:
                print("Incorrect Index entered")
        else:
            print(f"No results found for {movie_name}")
    except:
        url = ('https://yts.mx/browse-movies' + '' + movie_name)
        print(url)
        res = requests.get('https://yts.mx/browse-movies/' + '' + movie_name)

        s = soup(res.text,'lxml')
        titles=s.select('.browse-movie-title')
        rating = s.select('.rating')
        links = s.select('.browse-movie-link')
        if(len(rating)==0):
            print("No Movies Present with that name")

        else:
            li=[]
            for i in range(len(links)):
                print(i+1, end=" ")
                print(links[i].figure.img["alt"], end=" ")
                print(rating[i].text)
                li.append(titles[i]['href'])
     
        req=requests.get(li[i])
        se = soup(req.text, 'lxml')
        m=se.find("p",{"class":"hidden-md hidden-lg"}).a["href"]
        magnet.append(m)
        if magnet:
            try:
                download = False  # Default is streaming
                stream_choice = int(
                    input("Press 1 to stream or Press 2 to download the movie\n"))
                if stream_choice == 2:
                    download = True
                webtorrent_stream(m, download)
            except IndexError:
                print("Incorrect Index entered")
        else:
            print(f"No results found for {movie_name}")


def webtorrent_stream(magnet_link: str, download: bool):
    cmd = []
    cmd.append("webtorrent")
    cmd.append(magnet_link)
    
    if not download:
        cmd.append('--vlc')

    if sys.platform.startswith('darwin'):
        subprocess.call(cmd)
    elif sys.platform.startswith('linux'):
        subprocess.call(cmd)
    elif sys.platform.startswith('win32'):
        subprocess.call(cmd, shell=True)


if __name__ == "__main__":
    main()
