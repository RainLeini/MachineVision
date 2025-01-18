#kasutaja annab inputi, kui mitu erinevat asja ta näha tahab. (1-6)
#kui kasutaja sisestab 4 siis avaneb 4 akent mis näitavad erinevaid asju. nt rotate resize jms vaata pilditöötlus projekti
#boonus kui randomiga.
#kui vajutad klahvi siis kõik aknad sulguvad.

import cv2


print(cv2.__version__)

image = cv2.imread('testpic.jpg')
#kuva pilt aknas


#kas on pilt
if image is None:
    print("Viga")
    exit()

#kui mitu pilti näitan?
nr=int(input("Kui palju pilte tahad 1-6? "))
if nr>6 or nr<1:
    print("Vale number")
    exit()


resized_image = cv2.resize(image, (1000, 600))

#mustvalge
gray_image = cv2.cvtColor(resized_image, cv2.COLOR_RGB2BGR)
painty_image = cv2.cvtColor(resized_image, cv2.COLOR_RGB2YCrCb)


im_height = gray_image.shape[0]
im_width = gray_image.shape[1]
center = (im_width // 2, im_height // 2)
rotation_matrix = cv2.getRotationMatrix2D(center, 90, 1)
rotated_image = cv2.warpAffine(gray_image, rotation_matrix, (im_width, im_height))
rotate_image = cv2.warpAffine(painty_image, rotation_matrix, (im_width, im_height))
cv2.destroyAllWindows()

if nr==1:
    cv2.imshow('kaunitar', rotated_image)
    cv2.waitKey(0)

elif nr==2:
    cv2.imshow('kaunitar', rotated_image)
    cv2.imshow('kaunitar2', gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif nr==3:
    cv2.imshow('kaunitar', rotated_image)
    cv2.imshow('kaunitar2', gray_image)
    cv2.imshow('kaunitar3', resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

elif nr==4:
    cv2.imshow('kaunitar', rotated_image)
    cv2.imshow('kaunitar2', gray_image)
    cv2.imshow('kaunitar3', resized_image)
    cv2.imshow('kaunitar4', painty_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

elif nr==5:
    cv2.imshow('kaunitar', rotated_image)
    cv2.imshow('kaunitar2', gray_image)
    cv2.imshow('kaunitar3', resized_image)
    cv2.imshow('kaunitar4', painty_image)
    cv2.imshow('kaunitar5', rotate_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

elif nr==6:

    cv2.imshow('kaunitar', rotated_image)
    cv2.imshow('kaunitar2', gray_image)
    cv2.imshow('kaunitar3', resized_image)
    cv2.imshow('kaunitar4', painty_image)
    cv2.imshow('kaunitar5', rotate_image)
    cv2.imshow('kaunitar6', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
