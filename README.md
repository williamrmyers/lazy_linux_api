# lazy_linux_api
###Create APIs the lazy way. Dump files in a folder, and the filenames are output to in JSON.

This program provides a way to create dynamic content on your own website with minimal effort. If you need to create a photo gallery for a club, or other organisation. You can simple dump the photos into a folder, then set the `path_to_gallery` variable to path.

The program then outputs the filenames JSON encoded. You can itegrate that with a dynamic app that excepts an unlimited number of filenames, and instead of updating the database, you just have upload the files.

Its designed to work with basic CGI on Linux Servers. Its currently written in Python 2.7.
