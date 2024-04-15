---
title: Ubuntu和Windows时间同步
tags: Linux
category: 环境
abbrlink: bb48d48e
date: 2024-04-08 21:49:24
---

## Windows和Ubuntu双系统时间不同步的解决方案

### 分析 

在安装Windows和Ubuntu双系统时，两个操作系统会分别使用自己的时间设置。Windows默认使用本地时间（Local Time），而Ubuntu则默认使用协调世界时（Coordinated Universal Time，UTC）。

造成这种不同的原因是因为操作系统对于硬件的时间处理方式不同。Windows将计算机的硬件时钟视为本地时间，即当前所在时区的时间；而Ubuntu及其他类Unix系统则将硬件时钟视为UTC时间，标准化的国际时间。

因此，在双系统中，当进入Ubuntu系统的时候，会根据UTC时间来显示当前的时间；而当进入Windows系统时，会根据本地时间来显示当前的时间。这也就是为什么在双系统中，两个操作系统的时间可能会不一样的原因。
*** 

### 解决方案
安装ntpdate：

``` shell
sudo apt install ntpdate
```

设置校正服务器：

``` shell
sudo ntpdate time.windows.com
```

设置硬件时间为本地时间：
``` shell
sudo hwclock --localtime --systohc
```