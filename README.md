# How to use this program

## 1. Set all you will need

0. First of all you should have puthon 3+ already installed on your computer.  
   If you don't have it yet, use this [website](https://www.python.org/downloads/) or find it in youtube, if it's easier for you)

1. After intalling python, install the script as zip, **save it on your desktop** and open the folder.

2. Create a new text file and name it as "list.txt".

3. Find any number of playlists you want to export and write full url and Title you want into our file like this:

``https://music.yandex.com/users/music-blog/playlists/2440, New Pop``

``https://music.yandex.com/users/music-blog/playlists/1624, This winter top``

1. After you create a txt file, last step you need to do is to install the speciall library for python, by using this commands:

**For Windows:**

``pip install Scrapy``

**For Linux:**

``sudo apt install python3-scrapy``

You can find full guide for the installation on [this website](https://docs.scrapy.org/en/latest/intro/install.html).

## 2. Use the script

After finishing first steps open you terminal (the way to do it depends on OS use use) and write this command:

``scrapy runspider playlist_transfer.py``

If you do everything right, you will find new files in this folder. Those will be named as playlists you wanted to create ("New Pop.txt" and "This winter top.txt" from example).  
Congrats! All you need to do then is to use a website like [this](https://soundiiz.com/), where you need to registrate and login to your spotify or anything else you want to use.  

All you need to do then is illustraded on the picture below:
![Screenshot from 2024-02-28 23-32-38](https://github.com/Impirs/Yandex-music-playlist-transfer/assets/90879703/57d29f4a-0b07-4a58-a205-bccd83d9a1b8)
