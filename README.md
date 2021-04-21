# bmad-component-db-test

In order to use the packaged example, the package must be installed into the chosen environment such that the devices are defined with the Happi entrypoints.  
 
```$ conda env create -f environment.yml```  

```$ conda activate bmad-component-db-test```

```$ pip install -e .```

In order to use blender with the notebook:

```$ blender_notebook install --blender-exec={PATH TO BLENDER EXECUTABLE}```

This functions by creating a jupyter kernel for the python packaged with blender. It adds the `site-packages` directory of the active interpretor to Blender's python path. 