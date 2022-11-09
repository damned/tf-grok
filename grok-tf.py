import glob
import json

import hcl2


def load_hcl_dict(filename):
    with open(filename, 'r') as hcl_file:
        return hcl2.load(hcl_file)


def extract_resources(hcl_filename, resource_type):
    file_dict = load_hcl_dict(hcl_filename)
    if 'resource' in file_dict:
        resources = file_dict['resource']
        return [resource[resource_type] for resource in resources if resource_type in resource]
    return []


def pretty_json(json_data):
    return json.dumps(json_data, indent=2)


def pprint_json(resource):
    print(pretty_json(resource))


def extract_resources_of_type(hcl_files, resource_type):
    target_resources = {}
    for hcl_filename in hcl_files:
        typed_resources = extract_resources(hcl_filename, resource_type)
        for typed_resource in typed_resources:
            if len(typed_resource.keys()) != 1:
                raise Exception('oh dear i thought each resource was a 1 key dict: ' + typed_resource.keys())
            resource_name = list(typed_resource.keys())[0]
            target_resources[resource_name] = typed_resource[resource_name]
    return target_resources


def dump_target_resources(target_resources):
    for resource_name in target_resources.keys():
        resource = target_resources[resource_name]
        pprint_json(resource)


tf_files = glob.glob('*.tf')
ssm_parameters = extract_resources_of_type(tf_files, 'aws_ssm_parameter')
dump_target_resources(ssm_parameters)

pprint_json(load_hcl_dict('test.tfvars'))
