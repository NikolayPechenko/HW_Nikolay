import multiprocessing
from PIL import Image


def resize_image(image_path):
    image = Image.open(image_path)
    image = image.resize((800, 600))
    image.save(image_path)


# for i in range(1,201):
#     image_path = f'./images/img_{i}.jpg'  # путь к директории, картинкам, пример без мультипроцессинга
#     resize_image(image_path)

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        all_images = []
        for images in range(201, 401):
            a = f'./images/img_{images}.jpg'
            all_images.append(a)
        pool.map(resize_image, all_images)


