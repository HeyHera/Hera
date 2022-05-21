### Setting up virtual environment
```
sudo apt install python3-venv
```
```
python3 -m venv Hera
```

### Installing dependencies
```
python -m pip install --user scipy matplotlib ipython jupyter pandas sympy nose
```
```
pip install librosa
```

### Installing tensorflow  
```
pip install --upgrade tensorflow
```

### Testing mic  
```
arecord -f cd -d 10 --device="hw:0,0" /tmp/test-mic.wav
aplay /tmp/test-mic.wav
```
### Preprocessing data
preprocessing_data.py

### Preparing data  
```
python preparing_data.py
```

### Run wake-word model
```
prediction.py
```

### Run in threading mode
```
run-parallel.py
```
