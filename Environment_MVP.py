"""Python template for creating a pool of similar instances."""

def GenerateConfig(context):
  
  resources = {
      'type': 'compute.v1.instanceGroup.managed',
      'name': context.properties['name'],
      'properties': {
          'size': context.properties['count'],
          'template': context.properties['template']
          'zone': context.properties['zone'],
          'base-instance-name': adlib
      }
  }
  return {'resources': resources}
