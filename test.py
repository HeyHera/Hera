import os
exp_user_path = os.path.expanduser("~/Music")
l = os.listdir(exp_user_path)
print(l)