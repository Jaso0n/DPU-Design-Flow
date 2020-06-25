# Petalinux 使用指南

## 什么是Peatlinux？

​	Peatlinux能产生ZYNQ7000、ZYNQ7MP和MicroBlaze嵌入式芯片Linux操作系统的工具，包括编译U-Boot，Kernel，Root File System，生成嵌入式芯片的fsbl.elf，uImage，zImage等文件。

## 创建系统的基本流程

1. Vivado创建硬件平台

2. 建PetaLinux工程

   `petalinux-create -t project -n your_project_name`

3. 据硬件平台描述文件（.XSA/.BSP）创建工程

   `petalinux-config --get-hw-description /path/to/XSA/or/BSP`

4. 配置系统选项

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

#### 2.1 准备阶段

​	你需要熟练使用Vivado工具，完成Block Design等设计，生成Bitstream，导出**硬件描述文件（.XSA）**。在使用Vivado工具进行设计时，需要对PS模块做如下配置

__Zynq-7000 Devices__

1.添加一个TTC模块，当有多个TTC模块时，petalinux默认使用第一个。

2.至少32MB的内存（DDR3 RAM > 32MB）

3.PS模块的串口

4.外部存储器，例如QSPI Flash和SD/MMC

5.PS模块的以太网（一般选上）

__Zynq UltraScale+ MPSoC__

1.至少64MB的内存（DDR3/4 RAM > 64MB）

2.PS模块的串口

3.外部存储器，例如QSPI Flash和SD/MMC

4.PS模块的以太网（一般选上）

### 2.2 根据模板创建工程

`petalinux-create --type project --template <PLATFORM> --name <your_prj_name>`

_<PLATFORM>_ 

-----zynqMP (Zynq UltraScale+MPSoC)

-----zynq (Zynq-7000 devices)

-----microblaze (MicroBlaze processor)

*<your_prj_name>*

petalinux会在你的workspace下创建一个<your_prj_name>文件夹，所有的工程文件都在里面。

### 2.3 导入硬件信息初始化工程

`petalinux-config --get-hw-description /path/to/XSA`

![](https://github.com/Jaso0n/DPU-Design-Flow/blob/master/ZedBoard/petalinux_guide_image/config.png)

需要注意的是，确保__*Subsystem AUTO Hardware Setting*__ 被选上。该选项中包括了处理器、内存、串口、以太网、Flash、SD、RTC硬件信息，以及BOOT.BIN，U-Boot，内核，rootfs和dtb软件信息。**根据你的需要，通过这些子选项可以对系统进行修改，一定要记得save，再退出。**

补充：选择***DTG Settings***出现***(template)MACHINE_NAME***

如果你使用的是Xilinx的开发板，template参数可以是

ac701-full, ac701-lite, kc705-full, kcu105, zcu1275-revb,
zcu1285-reva, zc1751-dc1, zc1751-dc2, zc702, zc706, avnet-ultra96-rev1, zcu100-revc,
zcu102-rev1.0, zcu104-revc, zcu106-reva, zcu111-reva

### 2.4 进一步配置工程

##### 2.4.1 修改Rootfs的类型

`petalinux-config`

选择 ***Image Packaging Configuration***修改***Root filesystem type***为***EXT4(SD/eMMC/SATA/USB)***

 ***Root filesystem type***可以是

**---INITRAMFS---INITRD---JFFS2---NFS---EXT4(SD/eMMC/SATA/USB)**

##### 2.4.2 修改启动镜像的存储方式

选择*** Subsystem AUTO Hardware Settings***    ---> *** Advanced bootable images storages settings*** 

***boot image settings***该选项配置BOOT.BIN文件的存储方式，可选为**primary flash**或者**primary sd**

***u-boot env parition settings***该选项配置u-boot文件的存储方式，可选为**primary flash**或者**primary sd**

***kernel image settings***该选项配置linux内核的存储方式，可选为**primary flash**、**primary sd**和**ethernet**

***jffs2 rootfs image settings***和***dtb image settings***默认就好

##### 2.4.3 为Rootfs添加依赖库和包

复制[extra opencv][1]文件夹到***/path/to/your/prj/dir/project-spec/meta-user/recipes-ai/***
如果没有***recipes-ai***可以新建一个

找到*/path/to/your/prj/dir/project-spec/meta-user/conf/**user-rootfsconfig***文件，添加下列内容

```
# Xilinx Run Time, XRT support
CONFIG_xrt
CONFIG_xrt-dev
CONFIG_zocl
CONFIG_opencl-clhpp-dev
CONFIG_opencl-headers-dev
CONFIG_packagegroup-petalinux-opencv
CONFIG_packagegroup-petalinux-opencv-dev

# DPU support
CONFIG_glog
CONFIG_gtest
CONFIG_json-c
CONFIG_protobuf
CONFIG_python3-pip
CONFIG_apt
CONFIG_dpkg

CONFIG_packagegroup-petalinux-x11
CONFIG_packagegroup-petalinux-v4lutils
CONFIG_packagegroup-petalinux-matchbox

# Vitis AI packages
CONFIG_gtest-staticdev
CONFIG_json-c-dev
CONFIG_protobuf-dev
CONFIG_protobuf-c
CONFIG_libeigen-dev

# Native compiling support
CONFIG_packagegroup-petalinux-self-hosted
CONFIG_cmake

# Extra opencv support
CONFIG_opencv
```

`petalinux-config -c rootfs`





[1]:https://github.com/Jaso0n/vitis_ai_custom_platform_flow/tree/master/ref_files/opencv
