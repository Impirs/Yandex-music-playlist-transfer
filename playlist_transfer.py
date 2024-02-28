import scrapy
import logging

logging.getLogger('scrapy').setLevel(logging.WARNING)

class MySpider(scrapy.Spider):
    name = "song_listener"

    def start_requests(self):
        with open('list.txt', 'r', encoding='utf-8') as file:
            for line in file:
                url, playlist_name = line.strip().split(", ")
                yield scrapy.Request(url, callback=self.parse, meta={'playlist_name': playlist_name})

    def parse(self, response):
        playlist_name = response.meta.get('playlist_name')
        song_list = response.css("a.d-track__title.deco-link.deco-link_stronger::text").extract()
        song_artists = response.css("span.d-track__artists")
        song_main_artists = []
        
        for artist in song_artists: 
            first_artist = artist.css("a::text").extract_first()
            if first_artist:
                song_main_artists.append(first_artist)

        self.write_list_to_file(playlist_name, song_list, song_main_artists)

    def write_list_to_file(self, playlist_name, song_list, song_main_artists):
        file_name = f"{playlist_name}.txt"
        with open(file_name, "w", encoding="utf-8") as file:
            for song, group in zip(song_list, song_main_artists):
                file.write(f"{group} - {song}\n")
