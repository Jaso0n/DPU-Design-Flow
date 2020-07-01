#coding = utf-8
#!/bin/bash
import numpy as np
import caffe
import cv2
import matplotlib as plt
import time


workspace = '/home/jojo/DL-ACC/resnet50-deploy/'
caffe_root = '/home/jojo/tools/caffe-master/'
# resnet50 weights
caffe_model = workspace + 'model/ResNet-50-model.caffemodel'
# resnet50 model
net_file = workspace + 'model/ResNet-50-deploy.prototxt'
# test pic 640*480
origin_pic_file = workspace + 'PIC_001.jpg'
# test pic 224*224
image_file = workspace + 'dog.jpg'
# mean_file from He Kaiming
mean_file = workspace + 'model/ResNet_mean.binaryproto'
# mean_file_npy to be used 
npy_mean_file = workspace + 'model/mean.npy'
# labels in imageNet
labels_file = caffe_root + 'data/ilsvrc12/synset_words.txt'

# denote to reshape the pic
#im1 = cv2.imread(origin_pic_file)
#im2 = cv2.resize(im1,(224,224))
#cv2.imwrite(image_file,im2)

# deneto to generate mean_file_npy
#blob = caffe.proto.caffe_pb2.BlobProto()
#data = open(mean_file, 'rb').read()
#blob.ParseFromString(data)
#array = np.array(caffe.io.blobproto_to_array(blob))
#mean_npy = array[0]
#np.save(npy_mean_file, mean_npy)

caffe.set_mode_cpu();
net = caffe.Classifier(net_file,
		       caffe_model,
		       mean = np.load(npy_mean_file).mean(1).mean(1),
		       channel_swap=(2,1,0),
		       raw_scale=255,
                       image_dims=(224,224))

image = caffe.io.load_image(origin_pic_file)
time_start = time.time()
prediction = net.predict([image])
time_end = time.time()
labels = np.loadtxt(labels_file, str, delimiter='\t')
top_inds = prediction[0].argsort()[::-1][:5]
print('Top5 prob:')
print(prediction[0][top_inds])
print(labels[top_inds])

print('Inference cost',time_end-time_start)



#print ('prediciion class:',prediction[0].argmax())

#print('output label:', labels[prediction[0].argmax()])


