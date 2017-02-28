"""Python template for creating a pool of similar instances."""

def GenerateConfig(context):

  machine_type = ''.join(['https://www.googleapis.com/compute/v1/projects/',
                          context.env['project'], '/zones/',
                          context.properties['zone'], '/machineTypes/',
                          context.properties['machineType']])
  
  resources = {
      'type': 'compute.v1.instanceGroup.managed',
      'name': context.properties['name'],
      'properties': {
          'size': resources
          'template': context.properties['template']
          'zone': context.properties['zone'],
          'base-instance-name': adlib
      }
  }
  return {'resources': resources}
