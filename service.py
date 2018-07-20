# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 09:30:13 2017
@author: zhangxun
"""
import json
from bottle import route, request, run
from logConf.logger import get_logger
from NER_BILSTM_CRF import main
logger = get_logger()
model=main.Infer()
@route("/nlp/getPER", method='POST')
def getPER():
    try:
        result = {}
        full_entities = []
        short_entities = []
        code = 502
        data = request.body.read()
        data = json.loads(str(data, encoding = "utf-8"))
        if "text" not in data.keys():
            code = 401
            raise Exception("text参数有误")
        if not data['text']:
            code = 402
            raise Exception("文本为空")
        text = data.get("text")
        # if isinstance(text, str):
        #     text = text

        # 文本预处理
        # text = text.replace(r"","")
        # todo
        model_type = data.get("version", "1.0")
        if model_type == "1.0":
            entities = model.infer(text)
            result['text'] = entities['string']
            result['entities'] = entities["entities"]
            # print type(entities)
            # print entities
        else:
            code = 401
            raise Exception("其他版本正在开发中，请用1.0版本")
        code = 200
        msg = "Succeed"
    except Exception as e:
        msg = str(e)
        print(e)
    result['code'] = code
    result['msg'] = msg
    return result
if __name__ == "__main__":
    run(host='0.0.0.0', port=19070, workers=8)




