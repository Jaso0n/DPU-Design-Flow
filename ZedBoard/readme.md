#  DPU in ZedBoard 设计指南

## 开发环境

__设计工具__

1.[Vivado 2020.1][1]

2.[Petalinux 2020.1][2]

3.[Vitis2020.1][3]

4.VMware + Ubuntu18.04 LTS

5.Windows10

__环境介绍：__ Vivado和Vitis安装在Windows下，Petalinux安装在Ubuntu系统中。Vivado完成硬件设计，Petalinux完成ZedBoard_DPU的操作系统设计，Vitis完成应用软件的设计。

__开发板介绍：__ 板载芯片是XC7Z020CLG484 -1，DSP资源220，Block RAM资源4.9Mb

## Vivado搭建硬件环境

__1.获取[DPU_IP][4]__

![](https://github.com/Jaso0n/DPU-Design-Flow/blob/master/ZedBoard/readme_image/dpu.png)

__2.完成Block Design__

1）依次添加*ZYNQ7 Processing System*,*DPU IP*,*Clock Wizard*,*AXI Interconnect*,*Processor System Reset*模块；

2）选择PS中的*PS-PL Configuration*，展开*HP Slave AXI Interface*，勾选*HP0*到*HP2*。这些IO在后面会与DPU的*DATA0*,*DATA1*,*INSTR*接口相连接；

3）配置*DPU IP*，选择*Arch*界面，DPU的大小设置为为B1152，*RAM Usage*的大小为High，关闭*DepthWiseConv*，*ReLU Type*为*ReLU+LeakyReLU+ReLU6*，与ZYNQ7000使用时，DPU不支持SoftMax的计算，这个得放在ARM CPU里面算（问题不大）。选择*Advanced*界面，*S-AXI Clock Mode*这里可选*Common with M-AXI Clock*也可以选*Independent*，这里我们选*Independent*。配置完按OK；**Tips:这么配置后*DSP Slice Count = 194, Block-RAM Count = 139.5*。**

4）配置*Clock Wizard*输出两路时钟，频率分别为90MHz和180MHz，90MHz的时钟是DPU的系统时钟，180MHz的时钟是DDR-DSP的时钟将这两路时钟依次与DPU相连接。DPU上*S_AXI*的时钟由ZYNQ模块的*FCLK_CLK0*提供。__时钟与复位信号的搭配关系是：相同时间域的复位信号连接到一起。__

5）将*DPU0_M_AXI_DATA0-1*，*DPU0_M_AXI_INSTR*与*AXI Interconnect*连接到一起（可能是起到缓冲的作用，应该是可以直接与*HP0-2*相连）。

![](https://github.com/Jaso0n/DPU-Design-Flow/blob/master/ZedBoard/readme_image/block_design.png)

![](https://github.com/Jaso0n/DPU-Design-Flow/blob/master/ZedBoard/readme_image/hier_clk_rst_gen.png)

![](https://github.com/Jaso0n/DPU-Design-Flow/blob/master/ZedBoard/readme_image/hier_dpu2hp.png)

__3.生成Bitstream，导出XSA文件__

1）通过Address Editor分配DPU的内存，貌似自动分配就行了

![](https://github.com/Jaso0n/DPU-Design-Flow/blob/master/ZedBoard/readme_image/address.png)

2）点击*Validate Block Design*。

3）点击*Generate Bitstream*

4）点击*Export hardware*，注意勾选*include bitstream*

__到这里Vivado上的工作就做完了__

## Petalinux搭建DPU+ARM CPU的Linux系统，详细见[Petalinux 使用指南][5]





[1]:https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/vivado-design-tools.html
[2]:https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/vitis.html
[3]:https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/embedded-design-tools.html
[4]:https://www.xilinx.com/products/design-tools/ai-inference/ai-developer-hub.html#edge
[5]:https://github.com/Jaso0n/DPU-Design-Flow/blob/master/ZedBoard/Petalinux%20%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97.md
