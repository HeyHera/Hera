import os

print("Preparing Data")
os.system('python preprocessing_data.py')
print("\n")
print("Preparation Done Succesfully")

print("Now Training the model")
os.system('python training.py')