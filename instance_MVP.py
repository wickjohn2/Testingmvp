"""Python template for creating a pool of similar instances."""

def GenerateConfig(context):
  """Generate the yaml config for a pool of instances."""
  resources = []
  for index in range(1, context.properties['count'] + 1):
    resources.append(GenerateInstanceConfig(context, index))
  return {'resources': resources}


def GenerateInstanceConfig(context, index):
  """Helper method to create the config for a single compute instance."""
  name_prefix = ''.join([context.properties['namePrefix'], '-',
                         context.env['deployment'], '-', str(index)])
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