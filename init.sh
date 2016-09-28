#! /bin/sh
pkg_folder=~/program/package

lua_folder=lua-5.3.3
lua_pkg_name=$lua_folder.tar.gz
lua_url=http://www.lua.org/ftp/$lua_pkg_name

### init env
#sudo apt update
#sudo apt upgrade
#sudo apt install wget axel curl
cd ~
mkdir -p $pkg_folder
cd $pkg_folder
###


### Lua5.3.3
wget -O $lua_pkg_name $lua_url
tar -C ../ -zxvf $lua_pkg_name
cd ../$lua_folder
make linux
sudo make install
###

