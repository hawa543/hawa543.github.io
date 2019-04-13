from  PIL import Image
my_image=Image.open("assets/before1.jpg")
image_pixels=my_image.load()
width,height= my_image.size
for i in range(0,width):
    for j in range(0,height):
        current_pixel=image_pixels[i,j]
        blue_component=image_pixels[i,j][0]
        green_component=image_pixels[i,j][1]
        red_component=image_pixels[i,j][2]
        gray_value=(int)(0.07 * blue_component+0.72 * green_component + 0.21 * red_component)
        if(gray_value<80):
            new_color =(28,19,196,255)
        elif(gray_value<160):
            new_color=(196,19,175,255)
        elif(gray_value<200):
            new_color=(196,37,19,255)
        elif(gray_value<220):
            new_color=( 19,196,175,255)
        else:
            new_color=(119,196,19,255)
        image_pixels[i,j]= new_color
my_image.show()
