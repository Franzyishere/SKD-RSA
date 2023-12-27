import cv2
import numpy as np

# Load the original image
demo = cv2.imread("C:/Users/Oddy/Documents/SEMESTER 3/Document Semester 3/SISTEM KEAMANAN DATA/Mythical Immortal.jpeg", 0)

# Get the shape of the image
r, c = demo.shape

# Generate a random key
key = np.random.randint(0, 256, size=(r, c), dtype=np.uint8)

# Save the key image with a different filename
cv2.imwrite("C:/Users/Oddy/Documents/SEMESTER 3/Document Semester 3/SISTEM KEAMANAN DATA/key_image.jpeg", key)

# Display the original image and the key (optional)
cv2.imshow("demo", demo)
cv2.imshow("key", key)

# Encrypt the image
encryption = cv2.bitwise_xor(demo, key)

# Save the encrypted image with a different filename
cv2.imwrite("C:/Users/Oddy/Documents/SEMESTER 3/Document Semester 3/SISTEM KEAMANAN DATA/encrypted_image.jpeg", encryption)

# Display the encrypted image (optional)
cv2.imshow("encryption", encryption)

# Decrypt the image
decryption = cv2.bitwise_xor(encryption, key)

# Save the decrypted image with a different filename
cv2.imwrite("C:/Users/Oddy/Documents/SEMESTER 3/Document Semester 3/SISTEM KEAMANAN DATA/decrypted_image.jpeg", decryption)

# Display the decrypted image (optional)
cv2.imshow("decryption", decryption)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
