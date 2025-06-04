from translate import Translator

# 显示提示，让用户输入源语言和目标语言
from_lang = input("请输入原始语言代码（如 en 表示英文）：")
to_lang = input("请输入目标语言代码（如 zh 表示中文,ja 表示日文,fr 表示法文）：")

# 创建翻译器对象
translator = Translator(from_lang=from_lang, to_lang=to_lang)

# 让用户输入要翻译的内容
text = input("请输入要翻译的内容：")

# 翻译并输出结果
try:
    translation = translator.translate(text)
    print("翻译结果：", translation)
except Exception as e:
    print("翻译失败：", e)
