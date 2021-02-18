import requests

if __name__ == '__main__':

    # 免费的人脸识别核对在线接口 ， 商业合作，联系作者： 1371117942@qq.com
    # free face verification online api , commercial purpose contact author at : 1371117942@qq.com


    #########################
    # 网页演示： http://zonetech.natapp1.cc/
    # try it at web page: http://zonetech.natapp1.cc/
    #########################


    #########################
    # 检测两张图片中 最大人脸 进行人脸比对，返回包含分数json ，要求图片不能大于200 k .
    # detect the largest face in the picture  for face verification , then return the json string with score of face similarity , each picture is supposed to be smaller than 200k .
    #########################

    url = 'http://zonetech.natapp1.cc/1vs1'
    files = {}
    files['file1'] = open('r1.jpg', 'rb')
    files['file2'] = open('r2.jpg', 'rb')

    r = requests.post(url, files=files)
    print(r.content)

    # {"score": 0.9203611794783778}


