# Calculate the output size of an image after convolution

def output_image_size(img_size, conv_kernel, conv_stride, conv_pad, pooling_kernel, pooling_stride, pooling_pad):

    conv_out = calc_out_size(img_size, conv_kernel, conv_stride, conv_pad)
    pool_out = calc_out_size(conv_out, pooling_kernel,
                             pooling_stride, pooling_pad)

    return (pool_out, pool_out)


def calc_out_size(img_size, kernel, stride, pad):
    return ((img_size - kernel + 2 * pad)/stride + 1)


if __name__ == '__main__':
    # out = output_image_size(512, 3, 0, 2)
    #----------------------------
    # Ex: 9
    out = output_image_size(img_size=512,
                            conv_kernel=3,
                            conv_stride=1,
                            conv_pad=0,
                            pooling_kernel=2,
                            pooling_stride=2,
                            pooling_pad=0)
    print('9:', out)
    
    # Ex: 15
    out = output_image_size(img_size=205,
                            conv_kernel=3,
                            conv_stride=2,
                            conv_pad=0,
                            pooling_kernel=2,
                            pooling_stride=1,
                            pooling_pad=0)
    print('15:', out)
    

