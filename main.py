from translate import Translator

# 创建翻译器对象，设置翻译方向：从中文到英文
translator = Translator(from_lang="zh", to_lang="en")

# 用户输入
word = input("请输入要翻译的中文词语：")

# 翻译
try:
    translation = translator.translate(word)
    print("翻译结果：", translation)
except Exception as e:
    print("翻译出错：", e)
