def conv_params(input_channels, output_channels, kernel_height, kernel_width):
    return output_channels*(input_channels*kernel_height*kernel_width + 1)


def dense_params(input_channels, output_channels):
    return output_channels*(input_channels +1)


def max_pooling_shape(input_height, input_width, num_channels, size=2, stride=2,):
    if input_height % size == 0 and input_width % size == 0:
        return ((input_height - stride)/size +1, (input_width - stride)/size +1, num_channels)
    else:
        print("Needs padding")


def conv_out_shape(input_height, input_width, kernel_height, kernel_width, num_filters, stride, padding=0):
    return (((input_height - kernel_height + 2*padding)/stride) + 1,((input_width - kernel_width + 2*padding)/stride) + 1, num_filters)

## Working on receptive field calculations