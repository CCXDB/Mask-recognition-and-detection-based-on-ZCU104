import os
root_dress=r"/workspace/image_augment_300_test"
count=0
with open("/workspace/train.txt","w") as f:

    for root,dirs,files in os.walk(root_dress):
        for file in files:
                f.write(os.path.join(root,file)+"\n")
                count=count+1
print(count)
print("completed!!")

