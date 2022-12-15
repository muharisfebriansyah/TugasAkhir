def Recovery(image, image_result):
    f = open(image, 'rb')
    original_image = f.read()
    f = open(image_result, 'rb')
    result_image = f.read()
    originalimage_length = len(original_image)

    total = 0
    for i in range(originalimage_length):
        try:
            if(original_image[i]==result_image[i]):
                total+=1
        except:
            print('Ukuran kedua file tidak sama')
            continue
    print(f"Score Recovery: {(total/originalimage_length * 100):.2f}%")
    print("Pengecekan Selesai!")
