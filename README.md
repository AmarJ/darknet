Darknet Neural Network Framework
 ---
 Darknet is an open source neural network framework written in C and CUDA by Joseph Redmon.
 
Using Redmon's darknet framework I created my own implemenation of YOLO (You Only Look Once) for my Kaptur logo recogntion project. YOLO is a new approach to object detection that uses a single neural network to predict bounding boxes and class probabilities on full images in one evaluation (hence the name). The [paper on YOLO](https://arxiv.org/pdf/1506.02640.pdf) is pretty easy to follow and nicely breaks down some machine learning concepts for none-PhDs like myself. 

### Custom features I added to the framework
* Watch folder: Images dropped into the watch folder are added to a queue and are run through the network. 

     ![alt text](https://preview.ibb.co/ciHfFQ/cmdLine.png)

* Threading for network preditions: Once the neural network's weights are loaded, multiple threads are created to make predicitons on images simultaneously. Before this only one image was processed at a time. This doubles and sometimes triples the rate at which images are processed on less powerful machines (like an AWS micro instance or a Raspberry pi).  

* Load balancing of the queue: Provides a pool of threads that are used to drain the queue. The number of threads created depends on the available virtual memory and stack size. Sometimes threads hang, so instead of loosing that image and the predicition, the image is added back to the queue and re-run through another thread. This avoids some OOM problems and stops the whole program from crashing.

### Results from YOLO

So far I've been really happy with the results that I've gotten with the YOLO approach. 
    
   ![alt text](https://preview.ibb.co/mYX0h5/20214229_1523254754385132_1723726012614705152_n_prediction.png)
   ![alt text](https://preview.ibb.co/crpVh5/20214007_1620378241366769_1436966993474355200_n_prediction.png)
   ![alt text](https://preview.ibb.co/d7k325/starbucks3_prediction.png)
   ![alt text](https://preview.ibb.co/hsgt25/20214298_1921053248159208_549290724764418048_n_prediction.png)

Even I had trouble seeing the really dark Starbucks logo in picture above.

