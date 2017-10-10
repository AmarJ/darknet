Darknet Neural Network Framework
 ---
 Darknet is an open source neural network framework written in C and CUDA by Joseph Redmon.
 
Using Redmon's darknet framework I created my own implementation of YOLO (You Only Look Once) for my Kaptur logo recognition project. YOLO is a new approach to object detection that uses a single neural network to predict bounding boxes and class probabilities on full images in one evaluation (hence the name). The [paper on YOLO](https://arxiv.org/pdf/1506.02640.pdf) is pretty easy to follow and nicely breaks down some machine learning concepts for none-PhDs like myself. 

### Use case
[Kaptur](https://kaptur.tech) is an application running in the cloud that scrapes images off social media sites and looks for logos of popular brands such as Starbucks, Nike and Corona. Once a logo is found, the metadata around the post is collected and several object classifiers are run on the image to get more information about what’s in it. I am collecting data about how people around the world are using these brands and working on transforming this mountain of information into business insights.

### Custom features I added to the framework
* **_Watch folder:_** Images that are dropped into the watch folder are added to a queue and then run through the network for logo detection. 

     ![alt text](https://preview.ibb.co/ciHfFQ/cmdLine.png)

* **_Threading for network predictions:_** Once the neural network's weights are loaded, multiple classifier threads are created to make predictions on images simultaneously. Before this only one image was processed at a time. On less powerful machines, like an AWS micro instance or a Raspberry pi, this doubles and sometimes triples the rate at which images are processed.  

* **_Load balancing of the queue:_** Provides a pool of threads that are used to drain the queue. The number of threads created depends on the available virtual memory and stack size. Sometimes threads hang, so instead of losing that image and prediction, the image is added back to the queue and re-run through another thread. This avoids some OOM problems and keeps everything running smoothly.

### Results from YOLO

So far I've been really happy with the results that I've gotten with YOLO. 
    
   ![alt text](https://preview.ibb.co/mYX0h5/20214229_1523254754385132_1723726012614705152_n_prediction.png)
   ![alt text](https://preview.ibb.co/crpVh5/20214007_1620378241366769_1436966993474355200_n_prediction.png)
   ![alt text](https://preview.ibb.co/d7k325/starbucks3_prediction.png)
   ![alt text](https://preview.ibb.co/hsgt25/20214298_1921053248159208_549290724764418048_n_prediction.png)

