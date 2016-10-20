一.小工具：
xeyes
telnet towel.blinkenlights.nl
fortune
rev 翻转
cmatrix

二.sublime安装：
cd ~
wget http://c758482.r82.cf2.rackcdn.com/Sublime\ Text\ 2.0.2\ x64.tar.bz2
tar vxjf Sublime\ Text\ 2.0.2\ x64.tar.bz2
sudo mv Sublime\ Text\ 2 /opt/
sudo ln -s /opt/Sublime\ Text\ 2/sublime_text /usr/bin/sublime

三.watch 周期性做某事 如：watch -n 5 ls

四.系统update:
sudo apt-get update
sudo apt-get upgrade
sudo apt-get dist-upgrade

五.删除多余内核：
1.查看系统内存在的内核版本列表：
sudo dpkg --get-selections |grep linux
2.查看当前Ubuntu系统使用的内核版本
uname -a 
3.删除多余内核：
sudo apt-get purge linux-headers-3.0.0-12 linux-image-3.0.0-12-generic 
更新grub：
sudo update-grub

六.txt2pdf
1.sudo apt-get install enscript ghostscript 
2.enscript -p output.ps input.txt
3.ps2pdf output.ps output.pdf

七.从代码转pdf学到的
find . -name *.cs | xargs enscript --color -Ecpp -p out.ps
1.find查找指定的文件,列出所有文件的文件名。
2.enscript把源代码转为ps文件。其中--color对代码加高亮 -E后面可以跟以什么语言加高亮。
3.xargs把管道输入当作变量？如果不加xargs，管道传来的是文件名，而不是文件内容。

八.引导设置
etc. file is local at path: /etc/default/grub
you can set the background.
find a pic which named background.* and run the command: sudo mv background.* /boot/grub/
find the param of "GRUB_GFXMODE",to set the px.
after all of up,you should run command: sudo update-grub
and reboot.

九.Unity桌面主题
Numix:

    sudo apt-add-repository ppa:numix/ppa 
    sudo apt-get update 
    sudo apt-get install numix-icon-theme-circle //安装图标
    sudo apt-get install numix-gtk-theme          //安装主题

snwh:
    sudo add-apt-repository ppa:snwh/pulp
    sudo apt-get update
    sudo apt-get install paper-gtk-theme

十.出现无法获得锁的情况时，可以执行命令：
	sudo dpkg --configure -a

十一.设置环境变量：
you can modify /etc/profile(all user) or .bashrc(only your user)
add command belowe:
Export  PATH="$PATH:/NEW_PATH"

十二.天气插件
sudo apt-get install indicator-weather

十三.开启ssh
service sshd start
service sshd stop
service sshd restart
或者
/etc/init.d/sshd start

十四.提取视频中的音频
mencoder -oac mp3lame -ovc copy -of rawaudio 视频文件 -o 音频文件

十五.挂载
sudo mount -t cifs -o username=Guest,password= //192.168.0.109/"share" /"local_share"

十六.axrgs -I替换名字
ls | xargs -t -I{} adb push {} /..

十七.curl下载
-o 文件名

十八.多线程下载 axel

十九. MiniGUI

二十.查找
which gcc、whereis gcc
locate gcc
dpkg -l | grep ""
find / -name ""



   


















