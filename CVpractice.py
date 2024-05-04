import numpy as np

# Define the Laplacian-filtered image
laplacian_image = np.array([[400, -400],
                            [-400, 400]])

# Function to perform zero crossing detection
def zero_crossing_detection(image):
    rows, cols = image.shape
    zero_crossings = np.zeros(image.shape, dtype=np.uint8)

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if (image[i][j] > 0 and image[i - 1][j] < 0) or (image[i][j] < 0 and image[i - 1][j] > 0):
                zero_crossings[i][j] = 255  # Set as white for visualization
            elif (image[i][j] > 0 and image[i + 1][j] < 0) or (image[i][j] < 0 and image[i + 1][j] > 0):
                zero_crossings[i][j] = 255  # Set as white for visualization
            elif (image[i][j] > 0 and image[i][j - 1] < 0) or (image[i][j] < 0 and image[i][j - 1] > 0):
                zero_crossings[i][j] = 255  # Set as white for visualization
            elif (image[i][j] > 0 and image[i][j + 1] < 0) or (image[i][j] < 0 and image[i][j + 1] > 0):
                zero_crossings[i][j] = 255  # Set as white for visualization

    return zero_crossings

# Perform zero crossing detection
zero_crossings = zero_crossing_detection(laplacian_image)

# Print the zero crossings
print("Zero Crossings:")
print(zero_crossings)
