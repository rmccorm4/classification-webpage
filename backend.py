import torchvision.models as models

def get_model(modelname):
  if hasattr(models, modelname):
    model = getattr(models, modelname)(pretrained=True)
  else:
    model = None

  return model


