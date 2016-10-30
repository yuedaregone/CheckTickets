#! /bin/sh
platform_win=window_mingw
platform_linux=linux
platform=$platform_linux

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

libpng_folder=libpng-1.6.26
libpng_pkg_name=$libpng_folder.tar.gz
libpng_url=http://prdownloads.sourceforge.net/libpng/$libpng_pkg_name

libjpeg_folder=jpeg-6b
libjpeg_pkg_name=jpegsr6.zip
libjpeg_url=https://sourceforge.net/projects/libjpeg/files/latest/download?source=files

install_program()
{
	if [ -z `which $1` ];then
		yes | sudo apt install $1
	fi
}
install_program git
install_program wget
install_program axel
install_program curl
install_program vim

cd ~
mkdir -p $pkg_folder
cd $pkg_folder

### Lua
if [ -z `which lua` ];then
	yes | sudo apt-get install libreadline-dev
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
fi
###

### zlib
if [ ! -f "/usr/local/lib/libz.a" ];then
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
fi
###

### libpng
if [ ! -f "/usr/local/lib/libpng16.a" ];then	
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
fi
###

### libjpeg
if [ 0 = 1 ];then
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
fi
###



