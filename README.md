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
/charades-algorithms$ ./get_alreadytrained.sh
```

You have to download csv files from [Charades Data Set](https://allenai.org/plato/charades/) and locate it on `./` folder.  

You have to fix routes to datasets folder in `datasets/charadesrgb.py` and `datasets/charadesflow.py`.  

#### Show & Save video with labels  

Show specific video!

```
charades-algorithms> python read.py -id={VIDEO_ID}
```

Save specific video!  
> Save it at `D:/workspace-dataset/charades/Charades_v1_with_actions`. You have to fix location in `read.py`.  

```
charades-algorithms> python read.py -id={VIDEO_ID} -s=True
```

Save all video!  

```
charades-algorithms> python read.py -id=all
```

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

## Reference
