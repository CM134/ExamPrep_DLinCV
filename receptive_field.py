#%%
import numpy as np

def conv_layer(pixel,kernel_size,stride,padding):
    """
    !!! Only for 1 axis like x or y    
    returns upper and lower bound of receptive field
    
    """
    
    
    if len(pixel) == 1:
        p_low = pixel[0]
        p_up = pixel[0]
    elif len(pixel) == 2:
        p_low = min(pixel)
        p_up = max(pixel)
    else:
        print("List elements should only be of size 1 or 2")
    
    lower = p_low * stride +1 -padding - np.floor(kernel_size/2)
    upper = p_up  * stride +1 -padding + np.floor(kernel_size/2)
    
    return [lower,upper]

def max_pool(pixel,kernel_size,stride,padding = None):
    """
    returns output of max_pool layer
    !!! only for 1 axis like x or y
    !!! padding not implemented. Dont know how to do
    
    Args:
        pixel (list): list of pixels.
        kernel_size (int): _description_
        stride (int): _description_
        padding ( optional): Not implemented. Defaults to None.

    Returns:
        _type_: _description_
    """
    
    assert type(pixel) == list
    
    if len(pixel) == 1:
        p_low = pixel[0]
        p_up = pixel[0]
    elif len(pixel) == 2:
        p_low = min(pixel)
        p_up = max(pixel)
    else:
        print("List elements should only be of size 1 or 2")

    # for lower
    pool_windows = [] # create all possible pool windows
    for i in range(0,p_low+kernel_size*2, stride):  # +K*2 just to be sure we do not miss anything
        window = [i,i+kernel_size-1]
        pool_windows.append(window)
    
    p_low_range = min(pool_windows[p_low])
    
    # for upper
    pool_windows = []
    for i in range(0,(p_up+kernel_size*2), stride):  # +K*2 just to be sure we do not miss anything
        window = [i,i+kernel_size-1]
        pool_windows.append(window)
    
    p_up_range = max(pool_windows[p_up])
    
    return [p_low_range,p_up_range]
    
    
    
#%% Ex: 16

# for x

x_pool = max_pool([2],2,1)
print(x_pool)
x_conv = conv_layer(x_pool,3,2,0)
print('x:', x_conv)

# for y 
# for x

y_pool = max_pool([1],2,1)
print(y_pool)
y_conv = conv_layer(y_pool,3,2,0)
print('y:', y_conv)



# %% Ex: 8

# for x

x_pool = max_pool([1],2,2)
print(x_pool)
x_conv = conv_layer(x_pool,3,1,0)
print('x:', x_conv)

# for y 
# for x

y_pool = max_pool([2],2,2)
print(y_pool)
y_conv = conv_layer(y_pool,3,1,0)
print('y:', y_conv)