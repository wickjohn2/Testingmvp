"""Python template for creating a pool of similar instances."""

def GenerateConfig(context):
  
  resources = {
      'type': 'compute.v1.instanceGroup.managed',
      'properties': {
          'size': 3,
          'template': context.properties['template']
          'zone': context.properties['zone'],
          'base-instance-name': app,
      }
  }
  return {'resources': resources}
