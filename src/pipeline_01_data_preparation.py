import os 
import logging
import argparse
import yaml 


def read_parms(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def main(config_path, dataasource):
    config = read_parms(config_path)
    print(config)

if __name__=="__main__":
    args = argparse.ArgumentParser()
    default_config_path = os.path.join("config", "params.yaml")
    args.add_argument("--config", default=default_config_path)
    args.add_argument("--dataasource", default=None)

    parsed_args = args.parse_args()
    main(config_path = parsed_args.config, dataasource=parsed_args.dataasource)