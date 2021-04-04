from google.cloud import vision
import cv2

# impath = r"dicktures/infill_in.jpg"
#
# im = cv2.imread(impath)
# h,w = im.shape[:2]

def find_human(path):
    """
    Finds humans in image at path, returns all bounding box vertices
    """

    im = cv2.imread(path)
    h, w = im.shape[:2]

    client = vision.ImageAnnotatorClient()

    with open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    objects = client.object_localization(image=image).localized_object_annotations

    bbox_pts = []
    for person in objects:
        if person.name in ["Human", "Person", "Man", "Woman"]:
            vertices = person.bounding_poly.normalized_vertices
            # print(vertices)
            p1 = (int(vertices[0].x * w), int(vertices[0].y * h))
            p2 = (int(vertices[2].x * w), int(vertices[2].y * h))
            bbox_pts.append((p1,p2))
            # cv2.rectangle(im, p1, p2, (255,0,0))
            # congrats u found a person, now do stuff

    # cv2.imsave("boxed_in.jpg", im)

    return bbox_pts

    # cv2.imshow("test", im)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


# find_human(impath)