# File discription
These files is the foward inference of ResNet50 on PC to be campared with pruned ResNet50 accelarated by DPU on ZedBoard.

The ***model*** dir includes the ***ResNet-50-deploy.prototxt*** and train mean files ***mean.npy*** 
which is generated from ***ResNet50.binaryproto*** in the ***resnet50-fdinf.py***.

The caffe model file ***ResNet-50-deploy.caffemodel*** is too big to upload, you can download from [here][1]


# How to run this demo?

Change the ***workspace*** and ***caffe_root*** to your path

Type `python resnet50-fdinf.py` in the console and you will know the classify resultm, excution time and Top5.

[1]:https://onedrive.live.com/?authkey=%21AAFW2-FVoxeVRck&id=4006CBB8476FF777%2117887&cid=4006CBB8476FF777
