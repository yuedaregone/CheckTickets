#! /bin/sh
platform_win=window_mingw
platform_linux=linux
platform=$platform_win

export INCLUDE_PATH=/usr/local/include
export LIBRARY_PATH=/usr/local/lib
export BINARY_PATH=/usr/local/bin

pkg_folder=~/program/package

lua_folder=lua-5.3.3
lua_pkg_name=$lua_folder.tar.gz
lua_url=http://www.lua.org/ftp/$lua_pkg_name

zlib_folder=zlib-1.2.8
zlib_pkg_name=$zlib_folder.tar.gz
zlib_url=http://zlib.net/$zlib_pkg_name

libpng_folder=libpng-1.6.25
libpng_pkg_name=$libpng_folder.tar.gz
libpng_url=ftp://ftp.simplesystems.org/pub/libpng/png/src/libpng16/$libpng_pkg_name

libjpeg_folder=jpeg-6b
libjpeg_pkg_name=jpegsr6.zip
libjpeg_url=https://sourceforge.net/projects/libjpeg/files/latest/download?source=files
### init env
#sudo apt update
#sudo apt upgrade
#sudo apt install wget axel curl
cd ~
mkdir -p $pkg_folder
cd $pkg_folder
###

:<<!
### Lua
wget -O $lua_pkg_name $lua_url
tar -C ../ -zxvf $lua_pkg_name
cd ../$lua_folder
if [ $platform = $platform_win ];then
	make mingw
	make install
elif [ $platform = $platform_linux ];then
	make linux
	sudo make install
fi
cd $pkg_folder
###

### zlib
wget -O $zlib_pkg_name $zlib_url
tar -C ../ -zxvf $zlib_pkg_name
cd ../$zlib_folder
if [ $platform = $platform_win ];then	
	cp -f ./win32/Makefile.gcc Makefile
	make	
	make install
elif [ $platform = $platform_linux ];then
	./configure && make
	sudo make install
fi
cd $pkg_folder
###

### libpng
wget -O $libpng_pkg_name $libpng_url
tar -C ../ -zxvf $libpng_pkg_name
cd ../$libpng_folder
if [ $platform = $platform_win ];then	
	./configure && make	
	make install
elif [ $platform = $platform_linux ];then
	./configure && make
	sudo make install
fi
cd $pkg_folder
###

### libjpeg
wget -O $libjpeg_pkg_name $libjpeg_url
unzip -d ../ $libjpeg_pkg_name
cd ../$libjpeg_folder
if [ $platform = $platform_win ];then	
	./configure && make	
	make install
elif [ $platform = $platform_linux ];then
	./configure && make
	sudo make install
fi
cd $pkg_folder
###
!


