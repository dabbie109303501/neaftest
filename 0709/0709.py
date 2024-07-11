import numpy as np
import pandas as pd

l=[];times=10
np.random.seed(0)
for i in range(times):
    images = np.random.randint(0, 256, size=(64, 64, 3), dtype=np.uint8)
    gray_images = np.mean(images, axis=2).astype(np.uint8)
    max_values = np.max(gray_images, axis=(0, 1))
    min_values = np.min(gray_images, axis=(0, 1))
    mean_values = np.mean(gray_images, axis=(0, 1))
    std_values = np.std(gray_images, axis=(0, 1))
    l.append([max_values,min_values,mean_values,std_values])
data={
    'Max':[l[i][0] for i in range(times)],
    'Min':[l[i][1] for i in range(times)],
    'Mean':[l[i][2] for i in range(times)],
    'Std':[l[i][3] for i in range(times)],
}
df = pd.DataFrame(data)
df.to_excel(f'test.xlsx')