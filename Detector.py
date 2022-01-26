import cv2
import imutils

hogDes = cv2.HOGDescriptor()
hogDes.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


def detection(photo):
    pic = cv2.imread(photo)
    pic = imutils.resize(pic,
                         width=min(450, pic.shape[1]))
    (area, _) = hogDes.detectMultiScale(pic,
                                        winStride=(5, 5),
                                        padding=(4, 4),
                                        scale=1.06)
    p = 1
    for x, y, h, w in area:
        cv2.rectangle(pic, (x, y), (x + w, y + h), (255, 15, 255), 1)
        cv2.putText(pic,
                    f'Osoba numer {p}',
                    (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                    (255, 15, 255), 1)
        p += 1
    print('Ludzi na zdjęciu: '
          + str(len(area)))
    cv2.imshow('Zdjęcie', pic)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
