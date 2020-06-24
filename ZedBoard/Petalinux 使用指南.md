# Petalinux 使用指南

## 什么是Peatlinux？

​	Peatlinux能产生ZYNQ7000、ZYNQ7MP和MicroBlaze嵌入式芯片Linux操作系统的工具，包括编译U-Boot，Kernel，Root File System，生成嵌入式芯片的fsbl.elf，uImage，zImage等文件。

## 创建系统的基本流程

1. Vivado创建硬件平台

2. 建PetaLinux工程

   `petalinux-create -t project -n yourprojectname`

3. 据硬件平台描述文件（.XSA/.BSP）创建工程

   `petalinux-config --get-hw-description /path/to/XSA/or/BSP`

4. 置系统选项

   `petalinux-config`

5. 建用户组件

   `petalinux-create -t COMPONENT`

6. 配置Linux内核

   `petalinux-config -c kernel`

7. 配置rootfs

   `peatlinux-config -c rootfs`

8. Build系统

   `petalinux-build`

9. 为部署系统打包

   `petalinux-package`

10. 启动系统和测试

    `petalinux-boot`

## Create a Project

### 1、通过BSP来创建工程

​	Board Support Package, BSP是对硬件电路的描述文件，通过它能够快速生成相应的Linux系统。一般Xilinx的开发板都有对应的BSP文件，通过这些文件可以快速上手Petalinux，但是如果用户自己设计的开发板，官方BSP就失效了。

`petalinux-create -t project -s /path/to/bsp`

### 2、通过Vivado输出的硬件描述文件创建工程

​	你需要熟练使用Vivado工具，完成Block Design等设计，生成Bitstream，导出**硬件描述文件（.XSA）**。在设计时，需要对芯片做如下配置

__Zynq-7000 Devices__

1.添加一个TTC模块

2.至少32MB的内存

3.串口

4.外部存储器，例如QSPI Flash和SD/MMC

5.以太网（一般都选上）

__Zynq UltraScale+ MPSoC__

1.至少64MB的内存

2.串口

3.外部存储器，例如QSPI Flash和SD/MMC

4.以太网（一般选上）

