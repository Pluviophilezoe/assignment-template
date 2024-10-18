import numpy as np
from PIL import Image

def generate_image(width, height):
    # 生成随机颜色的图像whuc
    data = np.random.rand(height, width, 3) * 255
    img = Image.fromarray(data.astype('uint8')).convert('RGB')
    return img