import os
from PIL import Image, ImageFont, ImageDraw

# 字体文件路径
font_path = "argos.ttf"  # 替换为你的字体文件路径

# 图像尺寸
image_size = (256, 256)

# 创建 output 目录（如果不存在）
if not os.path.exists("output"):
    os.makedirs("output")

# 读取字符列表
with open("inputEN.txt", "r", encoding="utf-8") as file:
    characters = file.read().replace("\n", "").replace(" ", "")

# 加载字体
font = ImageFont.truetype(font_path, size=256)  # 替换为你的字体大小

# 符号描述映射字典
symbol_mapping = {
    "!": "exclamation mark",
    "(": "left parenthesis",
    ")": "right parenthesis",
    ",": "comma",
    ".": "period",
    "?": "question mark",
    ";": "semicolon",
    ":": "colon",
    "'": "apostrophe",
    '"': "quotation mark",
    "-": "hyphen",
    "—": "em dash",
    "–": "en dash",
    "…": "ellipsis",
    " ": "space",
    "/": "slash",
    "\\": "backslash",
    "[": "left bracket",
    "]": "right bracket",
    "{": "left brace",
    "}": "right brace",
    "<": "less than",
    ">": "greater than",
    "@": "at sign",
    "#": "number sign",
    "$": "dollar sign",
    "%": "percent sign",
    "^": "caret",
    "&": "ampersand",
    "*": "asterisk",
    "_": "underscore",
    "+": "plus sign",
    "=": "equal sign",
    "|": "vertical bar",
    "~": "tilde",
    "`": "grave accent",
    "°": "degree sign",
    "§": "section sign",
    # 添加更多符号的映射
}

# 逐个生成图像和文本文件
for i, char in enumerate(characters):
    # 创建一个新的图像对象
    image = Image.new("1", image_size, color=1)  # "1" 表示黑白图像，color=1表示初始背景为白色

    # 创建绘图对象
    draw = ImageDraw.Draw(image)

    # 在图像上绘制文本
    draw.text((0, 0), char, font=font, fill=0)  # fill=0表示文本颜色为黑色

    # 生成文件路径
    image_filename = f"output/ch_{str(i).zfill(4)}.png"
    text_filename = f"output/ch_{str(i).zfill(4)}.txt"

    # 保存图像为PNG格式
    image.save(image_filename)

    # 生成对应的单词或描述
    if char.isupper():
        word = "upper case, "+char
    elif char.islower():
        word = "lower case, "+char
    elif char.isalnum():
        word = "number, "+char
    elif char in symbol_mapping:
        word = "symbol, " + symbol_mapping[char]
    else:
        word = "complex symbol,"+char

    # 保存文本文件
    with open(text_filename, "w+", encoding="utf-8") as text_file:
        text_file.write(word)

print("图像和文本生成完成！")
