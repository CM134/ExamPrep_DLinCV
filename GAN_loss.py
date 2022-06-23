import torch

def discriminator_loss(loss_fn, prediction_real, prediction_fake):
    """
    Fixed to solve question 5. Needs sigmoid.
    """
    
    prediction_fake = torch.sigmoid(prediction_fake)
    prediction_real = torch.sigmoid(prediction_real)
    
    real_labels = torch.ones(prediction_real.size(0))
    fake_labels = torch.zeros(prediction_fake.size(0))

    error_real = loss_fn(prediction_real, real_labels)

    error_fake = loss_fn(prediction_fake, fake_labels)
    
    print('error real:', error_real )
    print('fake real:', error_fake)
    
    total_error = error_real + error_fake
    return total_error


def discriminator_loss_v2(prediction_real, prediction_fake):
    """
    Fixed to solve question 5. Applies minmax loss
    """
        
    real_labels = torch.ones(prediction_real.size(0))
    fake_labels = torch.zeros(prediction_fake.size(0))
    
    sigmoid = lambda x: 1/(1+torch.exp(-x))

    loss = -(torch.mean(torch.log(sigmoid(prediction_real))) + torch.mean(torch.log(1 - sigmoid(prediction_fake))))

    return loss

# TODO: Wasserstein loss

 


#-------------------------------------------------

prediction_real = torch.tensor([0.5,0.9])
prediction_fake = torch.tensor([0.5,0.1])

loss_fn = torch.nn.BCELoss()

print('V1:', discriminator_loss(loss_fn, prediction_real, prediction_fake))

print('V2:', discriminator_loss_v2(prediction_real, prediction_fake))