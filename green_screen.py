import numpy as np
import cv2
import sys
import datetime

# Function to crop the center of the large image to match the size of the small image
def crop(small, large, suffix):
    img_large = cv2.imread(large)
    img_small = cv2.imread(small)
    s_h, s_w, s_c = img_small.shape
    l_h, l_w, l_c = img_large.shape

    # Calculate the region to be cropped from the large image
    crop_img = img_large[(round(l_h / 2) - round(s_h / 2)):(round(l_h / 2) + round(s_h / 2)), (round(l_w / 2) - round(s_w / 2)):(round(l_w / 2) + round(s_w / 2))]
    
    # Create a new filename for the cropped image
    new_name = "cropped/" + "cropped_" + suffix + ".jpg"
    
    # Save the cropped image
    save = cv2.imwrite(new_name, crop_img)
    return new_name

# Function to convert green pixels to black and non-green pixels to white
def remove_green(green, suffix):
    img = cv2.imread(green)
    
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    kernel = np.ones((5, 5), np.uint8)
    
    lower = np.array([50, 100, 50]) 
    # lower = np.array([52, 0, 55]) 
    upper = np.array([70, 255, 255]) 
    # upper = np.array([104, 255, 255]) 
    
    mask = cv2.inRange(hsv, lower, upper)
    # mask = cv2.erode(mask, kernel, iterations=1) 
    # mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel) 
    # mask = cv2.dilate(mask, kernel, iterations=1) 
    
    mask = cv2.bitwise_not(mask)

    black = np.array([0,0,0])
    white = np.array([255,255,255])

    # Create a new filename for the black and white image
    black_and_white = "masks/" + "black_and_white_" + suffix + ".jpg"
    
    # Save the black and white image
    save = cv2.imwrite(black_and_white, mask)
    return black_and_white

# Function to combine the black and white mask with the new image
def add_new_image(baw, green, new_img, filename):
    img = cv2.imread(baw)
    new = cv2.imread(new_img)
    green = cv2.imread(green)

    for i in range(len(green)):
        for j in range(len(green[i])):
            if (img[i][j][0] != 255):
                green[i][j] = new[i][j]
                
    # Create a new filename for the output image
    name = "output/" + filename + ".jpg"
    
    # Save the final output image
    save = cv2.imwrite(name, green)

# Main function orchestrating the entire green screen process
def green_screen(green, background, filename, suffix):
    cropped = crop(green, background, suffix)
    black_and_white = remove_green(green, suffix)
    add_new_image(black_and_white, green, cropped, filename)

if __name__ == "__main__":
    # Get the green screen image, background, and set up filenames
    green_screen_image = sys.argv[1]
    background = sys.argv[2]
    basename = "output"
    suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    filename = "_".join([basename, suffix])
    
    # Perform the green screen effect
    green_screen(green_screen_image, background, filename, suffix)
