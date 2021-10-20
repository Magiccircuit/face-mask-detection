this a machine learning final project

#### More information please refer to 

[here]: https://zhangle.netlify.app/project/machine-learning/



## Code Structure

```
|__ inference
    |__ input 
    |__ output
|__ models --> model and settings for yolov5
|__ runs  
    |__ detect --> inference results 
    |__ train --> results after each train as well as weight 
and metrics
|__ utils --> general functions for datasetrs,loss, plots, metrics 
|__ weigths
	|__ best.pt--> loaded weights 
|__ detect.py --> detection function
|__ mask_window.py --> main window functions
|__ maskui.py --> main window ui
|__ train.py --> train the model
|__ test.py --> test on validation set
|__ voc_label.py --> convert the format of annotation and label name
```

## Getting Started

install with  `pip install -r requirements.txt` 

1. make sure there are `.pt` file for the model to load in the `weights`
2. run  `python mask_window.py`
