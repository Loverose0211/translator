from googletrans import Translator

translator = Translator()

src_lang = input("请输入原始语言代码（如 en=英文, zh-CN=中文, ja=日文）：")
dest_lang = input("请输入目标语言代码（如 en=英文, zh-CN=中文, ja=日文）：")

text = input("请输入要翻译的内容：")

result = translator.translate(text, src=src_lang, dest=dest_lang)

print("翻译结果：", result.pronunciation)

