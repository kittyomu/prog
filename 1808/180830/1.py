from PIL import Image
import sys

import pyocr
import pyocr.builders

tools = pyocr.get_available_tools() # OCRツールの有無の確認
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)

tool = tools[0]
print("Will use tool '%s'" % (tool.get_name())) # 使用するOCRツールの名前が出ます，変えたい場合は一個前の参照先を変えること

langs = tool.get_available_languages() # 使用できる言語の確認
print("Available languages: %s" % ", ".join(langs))

lang = langs[0]
print("Will use lang '%s'" % (lang)) # 使用する言語について