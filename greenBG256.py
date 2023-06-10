from PIL import Image
import os

# 遍历目录下所有png文件
for filename in os.listdir('.'):
    if filename.endswith('.png'):
        # 打开图片
        image = Image.open(filename)
        # 无插值缩放为256x256
        image = image.resize((256, 256), resample=Image.NEAREST)
        # 替换透明背景为纯绿色
        image = image.convert('RGBA')
        data = image.getdata()
        new_data = []
        for item in data:
            if item[3] == 0:
                new_data.append((0, 255, 0, 255))
            else:
                new_data.append(item)
        image.putdata(new_data)
        # 保存图片
        image.save(filename)
        print(filename)
