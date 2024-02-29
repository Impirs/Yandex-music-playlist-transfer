import scrapy
import logging

logging.getLogger('scrapy').setLevel(logging.WARNING)


class MySpider(scrapy.Spider):
    name = 'song_spider'
    start_urls = ['https://music.yandex.com/users/ArchieSofa/playlists/3'] 
    padding_top = 0
    padding_bottom = 164696
    songs_per_load = 100

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        song_divs = response.css("div.d-track.typo-track.d-track_selectable")
        song_list = response.css("a.d-track__title.deco-link.deco-link_stronger::text").extract()
        song_artists =response.css("span.d-track__artists")
        song_main_artists = []
        song_id = []

        #for div in song_divs:
        #    id = div.attrib['data_id']
        #    if id & id not in song_id:
        #        yield song_id.append(id)
        #    else:
        #        self.logger.info(f"ID {id} is already in the id list")

        for artist in song_artists: 
            first_artist = artist.css("a::text").extract_first()
            if first_artist:
                song_main_artists.append(first_artist)

        self.write_list_to_file( song_list, song_main_artists)
        
        self.padding_top += 8840

        if len(song_list) == self.songs_per_load:
            next_url = self.generate_next_url(response.url)
            yield scrapy.Request(next_url, callback=self.parse)

    def generate_next_url(self, current_url):
        next_padding = self.padding_top
        next_url = current_url + f'?padding_top={next_padding}'
        return next_url
    
    def write_list_to_file(self ,song_list, song_main_artists):
        with open("favorite.txt", "a", encoding="utf-8") as file:
            for  song, group in zip( song_list, song_main_artists):
                file.write(f"{group} - {song}\n")