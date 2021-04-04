import face_recognition
import numpy as np
import cv2




# fb_fpath = "boxed_in.jpg"
# ex_fpath = r"picktures/ex.png"

def find_ex(ex_fpath, fb_fpath):
    ex_image = face_recognition.load_image_file(ex_fpath)
    ex_encoding = face_recognition.face_encodings(ex_image)[0]

    facebook_image = face_recognition.load_image_file(fb_fpath)
    face_locations = face_recognition.face_locations(facebook_image)
    face_encodings = face_recognition.face_encodings(facebook_image, face_locations)

    distances = [0]*len(face_encodings)

    for i, face_encoding in enumerate(face_encodings):
        distances[i] = face_recognition.face_distance([ex_encoding], face_encoding)

    best_match = np.argmin(distances)
    ex_face_location = face_locations[best_match]

    # print(ex_face_location)

    # im = cv2.imread(fb_fpath)
    # h,w = im.shape[:2]
    # pt1 = (w-ex_face_location[1], h-ex_face_location[0])
    # pt2 = (w-ex_face_location[3], h-ex_face_location[2])

    pt1 = (ex_face_location[1], ex_face_location[0])
    pt2 = (ex_face_location[3], ex_face_location[2])
    # cv2.rectangle(im, pt1, pt2, (0,255,0))

    return (pt1, pt2)

# cv2.imshow("test", im)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# print(results)