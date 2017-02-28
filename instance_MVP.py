def GenerateConfig(context):
  """Helper method to create the config for a single compute instance."""
  name_prefix = context.properties['namePrefix']
  machine_type = ''.join(['https://www.googleapis.com/compute/v1/projects/',
                          context.env['project'], '/zones/',
                          context.properties['zone'], '/machineTypes/',
                          context.properties['machineType']])
  

  instance = {
      'type': 'compute.v1.instance',
      'name': name_prefix,
      'properties': {
          'zone': context.properties['zone'],
          'machineType': machine_type,
          'image': context.properties['image'],
      }
  }
  return instance
