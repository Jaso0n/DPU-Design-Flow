# DPU 设计流程
  整个流程需要用到Vivado，vitis和petalinux等工具，版本均为2020.1。最新的设计分为两种，Vivado+Petalinux的设计，Vivado+Petalinux+vitis AI库的快速设计
## Vivado+Petalinux设计流程
1.下载[DPU TRD v3.0][1],从中获得DPU IP。

![](https://github.com/Jaso0n/DPU-Design-Flow/blob/master/ZedBoard/readme_image/dpu.png)

2.完成Block Design

1）添加ZYNQ7 Processing System








[1]:https://www.xilinx.com/products/design-tools/ai-inference/ai-developer-hub.html#edge
### 吐槽
   官方TRD是ZCU102的参考设计，这块开发板能发挥DPU的最大性能，部署了2个DPU，基本频率为325MHz，DDR-DSP的频率是650MHz，但是这块板子$2,495，穷人不配研究。参考TRD和参考资料，在ZedBoard上完成单核DPU设计，而且频率只有可怜的90MHz基本运行频率，DDR-DSP的频率是180MHz。

![](https://www.xilinx.com/products/boards-and-kits/ek-u1-zcu102-g/_jcr_content/root/parsys/xilinxtabs2/childParsys-hardware/xilinximage.img.jpg/1519410010855.jpg)
