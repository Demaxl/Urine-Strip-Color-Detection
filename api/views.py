import cv2 
import numpy as np 

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from PIL import Image
from pprint import pprint

def get_colors(img_array):
    """ Returns the colors in the image """
    reagents = ['URO', 'BIL', 'KET', 'BLD', 'PRO', 'NIT', 'LEU', 'GLU', 'SG', 'PH']
    colors = {}

    # Location of first reagent in image
    x, y = 160, 60
    for i in range(10):
        # Assign color to reagents as we detect them from top to bottom
        # Color is gotten from numpy array of image
        colors[reagents[i]] = img_array[y, x].tolist()

        # Move to next reagent by incrementing distanct
        y += 90 
    
    return colors

@api_view(['POST'])
def detect(request :Request):
    uploaded_image = request.FILES.get("image")

    # Read the image
    img = Image.open(uploaded_image)

    # Convert the image to numpy array
    img_array = np.array(img)
    
    # Get the colors in the image and return as response
    return Response(get_colors(img_array), status=status.HTTP_200_OK)