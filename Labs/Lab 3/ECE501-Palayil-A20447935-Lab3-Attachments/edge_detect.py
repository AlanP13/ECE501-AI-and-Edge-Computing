import cv2
import sys
from matplotlib import pyplot as plt

for image in sys.argv[1:]:
    print('Processing image:', image)

    img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    edges = cv2.Canny(img, 100, 200)

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].imshow(img, cmap='gray')
    axes[0].set_title('Original Image')
    axes[0].axis('off')
    axes[1].imshow(edges, cmap='gray')
    axes[1].set_title('Edge Image')
    axes[1].axis('off')
    plt.tight_layout()
    plt.show()

    out = image.rsplit('.', 1)[0] + '_edges.png'
    cv2.imwrite(out, edges)

    print('Finished processing')
    print('Output saved to:', out)

