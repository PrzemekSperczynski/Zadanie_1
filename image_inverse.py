import cv2
import numpy as np
from fastapi import File, APIRouter
from fastapi.responses import StreamingResponse

image_router = APIRouter()

@image_router.post("/picture")

def inv_img():
    image = cv2.imread('YEBOI.jpg')
    cv2.imshow("Original Image",image)

    inverted_image = cv2.bitwise_not(image)
    cv2.imshow("Inverted Image",inverted_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return StreamingResponse(inverted_image, media_type="image/jpeg")