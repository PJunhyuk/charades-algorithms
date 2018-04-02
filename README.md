# charades-pytorch

Train and Read [Charades Dataset](http://allenai.org/plato/charades/), implemented on Python and [PyTorch](http://pytorch.org/), on Windows.  

Based on [PyTorch Starter Code for Activity Classification and Localization on Charades](https://github.com/gsig/charades-algorithms)  

## Demo  
<img src="/samples/TX020_action.gif" width="600">  
video_id = TX020

## Usage  

#### Settings  

You have to download trained files.  

```
> bash
/pytorch$ ./get_alreadytrained.sh
```

You have to fix routes to datasets folder in `datasets/charadesrgb.py` and `datasets/charadesflow.py`.  

#### Train  

Train RGB!

```
charades-algorithms> python exp/rgbnet.py --data={PATH_TO_DATASET_FOLDER}
```

Train FLOW!

```
charades-algorithms> python exp/flownet.py --data={PATH_TO_DATASET_FOLDER}
```

Test with pretrained-model!

```
charades-algorithms> python exp/rgbnet.py --pretrained-weights={PATH_TO_PRETRAINED_WEIGHTS_FILE-~.pth.tar}
```

#### Read results  

Read and show specific video!

```
charades-algorithms> python read.py -id={VIDEO_ID}
```

Read and save specific video!  

```
charades-algorithms> python read.py -id={VIDEO_ID} -s=True
```

Read and save all video!  

```
charades-algorithms> python read.py -id=all
```

## Reference
