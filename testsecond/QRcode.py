import qrcode
import zxing
import cv2

class QR:
    #photo = 'camera.jpg'
    photo = './Users/user/Desktop/testtest/camera.jpg'

    def code(self):
        data1 = "box"                       # QR inside
        img = qrcode.make(data=data1)       # generate QR code
        img.save("box.jpg")                 # save QR code
        box_path = '/Users/user/Desktop/testtest/camera.jpg'
        #box_path = 'box.jpg'                # address of the QR code

        data2 = "not box"                     # QR inside
        img = qrcode.make(data=data2)       # generate QR code
        img.save("noBox.jpg")               # save QR code
        nobox_path = '/Users/user/Desktop/testtest/camera.jpg'
        #nobox_path = 'noBox.jpg'            # address of the QR code

    def open_camera(self):
        cap = cv2.VideoCapture(0)  # 0 to open the laptop camera, 1 to open the outside camera
        width = 320
        height = 240
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)  # set the image width
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)  # set the image height
        # 显示图像
        while True:
            ret, frame = cap.read()  # read the image(frame就是读取的视频帧，对frame处理就是对整个视频的处理)
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # turn to gery

            if cv2.imwrite(self.photo, img):
                self.scan()             # detect the QR code

            cv2.imshow("img", img)    # display the camera

            input = cv2.waitKey(1)
            if input == ord('q'):  # q to break the camera
                break

        cap.release()  # release the camera
        cv2.destroyAllWindows()  # destory the windows


    def scan(self):
        reader = zxing.BarCodeReader()
        barcode = reader.decode(self.photo)
        if barcode != None:
            print(barcode.parsed)       # 二维码识别内容
        else:
            print("cant find the QR code")


qr = QR()
qr.code()
qr.open_camera()
#qr.scan()






