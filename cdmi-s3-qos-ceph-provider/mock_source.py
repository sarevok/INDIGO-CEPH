import json


class DataProvider:

    def get_profiles_json(self):
        json_string = "[{'metadata_provided': {'cdmi_latency_provided': '20', 'cdmi_data_redundancy_provided': '2','cdmi_geographic_placement_provided': ['PL', 'GB']},{'metadata': {'cdmi_latency': '20', 'cdmi_data_redundancy': '2','cdmi_geographic_placement': ['PL', 'GB']}, 'pools': ['.rgw.buckets'],'type': 'container', 'name': 'Profile1', 'allowed_profiles': []},{'metadata': {'cdmi_latency': '300', 'cdmi_data_redundancy': '2','cdmi_geographic_placement': ['DE', 'CZ']}, 'pools': ['.rgw.buckets.cdmi2'],'type': 'dataobject', 'name': 'Profile2', 'allowed_profiles': []}]"
        dumped_profiles = json.dumps(json_string)
        if len(dumped_profiles) == 0:
                return None
        return dumped_profiles

    def get_profile_json(self, bucket_name):
        json_string = "{'type': 'container', 'metadata': {'cdmi_geographic_placement': ['PL', 'GB'], 'cdmi_data_redundancy': '2', 'cdmi_latency': '20'}, 'name': 'Profile1', 'allowed_profiles'': [], 'pools'': ['.rgw.buckets']}"
        dumped_profile = json.dumps(json_string)
        if len(dumped_profile) == 0:
                return None
        return dumped_profile

    def __get_profiles_names(self):
        return self.__config.sections()

    def __init__(self, config):
        self.__config = config

