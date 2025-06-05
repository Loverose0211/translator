from googletrans import Translator

translator = Translator()

try:
    src_lang = input("请输入原始语言代码（如 en=英文, zh-CN=中文, ja=日文）：")
    dest_lang = input("请输入目标语言代码（如 en=英文, zh-CN=中文, ja=日文）：")
    text = input("请输入要翻译的内容：")

    result = translator.translate(text, src=src_lang, dest=dest_lang)
    print("翻译结果：", result.text)

except ValueError as ve:
    print("❗语言代码无效,请检查拼写。示例:en,zh-CN,ja")
    print("错误信息：", ve)

except Exception as e:
    print("❗发生了未知错误，请重试")
    print("错误信息：", e)


