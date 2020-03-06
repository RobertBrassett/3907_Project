import qrcode
import zxing
import cv2

class QR:
    photo = 'camera.jpg'
    #photo = './home/pi/3907_Project/testtest/camera.jpg'

    def code(self):
        data1 = "盒子"                       # 二维码内容
        img = qrcode.make(data=data1)       # 生成二维码
        img.save("box.jpg")                 # 保存二维码为文件
        box_path = 'box.jpg'                # 盒子二维码地址，根据自己路径修改！！

        data2 = "非盒子"                     # 二维码内容
        img = qrcode.make(data=data2)       # 生成二维码
        img.save("noBox.jpg")               # 保存二维码为文件
        nobox_path = 'noBox.jpg'            # 非盒子二维码地址，根据自己路径修改！！

    def open_camera(self):
        cap = cv2.VideoCapture(0)  # 调用摄像头‘0'一般是打开电脑自带摄像头，‘1'是打开外部摄像头（只有一个摄像头的情况）
        width = 160
        height = 160
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)  # 设置图像宽度
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)  # 设置图像高度
        # 显示图像
        while True:
            ret, frame = cap.read()  # 读取图像(frame就是读取的视频帧，对frame处理就是对整个视频的处理)
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 转灰度图

            if cv2.imwrite(self.photo, img):
                self.scan()             # 检测二维码

            cv2.imshow("img", img)    # 显示摄像头捕捉画面

            input = cv2.waitKey(1)
            if input == ord('q'):  # 如过输入的是q就break，结束图像显示，鼠标点击视频画面输入字符
                break

        cap.release()  # 释放摄像头
        cv2.destroyAllWindows()  # 销毁窗口


    def scan(self):
        reader = zxing.BarCodeReader()
        barcode = reader.decode('box.jpg')
        if barcode != None:
            print(barcode.parsed)       # 二维码识别内容
        else:
            print("识别不到二维码")


qr = QR()
qr.code()
qr.open_camera()
qr.scan()





