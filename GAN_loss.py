import torch

def discriminator_loss(loss_fn, prediction_real, prediction_fake):
    """
    ! does not return the same as we expect from the question 3
    """
    
    real_labels = torch.ones(prediction_real.size(0))
    fake_labels = torch.zeros(prediction_fake.size(0))

    error_real = loss_fn(prediction_real, real_labels)

    error_fake = loss_fn(prediction_fake, fake_labels)
    print('error real:', error_real )
    print('fake real:', error_fake)
    
    total_error = error_real + error_fake
    return total_error

# TODO: Wasserstein loss




#-------------------------------------------------

prediction_real = torch.tensor([0.5,0.9])
prediction_fake = torch.tensor([0.5,0.1])

loss_fn = torch.nn.BCELoss()

print(discriminator_loss(loss_fn, prediction_real, prediction_fake))