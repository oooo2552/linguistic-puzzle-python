import cv2



def main(filename):

  #カメラを選びます。実際の実験はインデックス１を選んで、カメラ２を使って
  vid_capture = cv2.VideoCapture(1)

  # 映像のサイズ
  vid_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
  vid_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

  #  XVID エンコーダ
  fourcc = cv2.VideoWriter_fourcc(*'MP4V')

  # 建立 VideoWriter 物件，輸出影片至 output.mp4
  # FPS 值為 20.0，解析度為 640x480
  filename = filename + ".mp4"
  out = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))

  while(vid_capture.isOpened()):
    ret, frame = vid_capture.read()
    if ret == True:
      # 寫入影格
      out.write(frame)

      cv2.imshow('frame',frame)
      if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    else:
      break

  # 釋放所有資源
  vid_capture.release()
  out.release()
  cv2.destroyAllWindows()


