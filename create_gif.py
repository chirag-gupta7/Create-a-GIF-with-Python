import imageio.v3 as iio

filenames = ['pic1.jpg', 'pic2.jpg']
image = []

for filename in filenames:
    image.append(iio.imread(filename))

iio.imwrite('team.gif', image, duration = 300, loop = 0)