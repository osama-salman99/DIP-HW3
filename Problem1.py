from Helping import *

# original_image = read_GIF('res/HouseNoisy.gif')
original_image = read_GIF('res/HouseNoisy.gif').astype('uint8')

consistent_intensity_region = original_image[0:110, 350:505]

show_image_and_wait(consistent_intensity_region)

print(f"mean before any mathematical computations -- > {np.mean(consistent_intensity_region)}")
print(f"var of the noisy image -- > {np.var(consistent_intensity_region)}")
print(f"std of the noisy image --> {np.std(consistent_intensity_region)}")

smoothed_region = consistent_intensity_region.copy()

for i in range(1000):
    smoothed_region = cv2.blur(smoothed_region, (50, 50))

print(f"The mean of excessive smoothed image -- > {np.mean(smoothed_region)}")
print(f"Mean of the noise -- > {np.mean(consistent_intensity_region) - np.mean(smoothed_region)}")

show_image_and_wait(smoothed_region, 'smoothed image')
