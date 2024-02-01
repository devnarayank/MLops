import os 
import logging
import argparse
import yaml 


if __name__=="__main__":
    args = argparse.ArgumentParser()
    default_config_path = os.path.join("config", "params.yaml")
    args.add_argument("--config", default=default_config_path)
    args.add_argument("--dataasource", default=None)

    parsed_args = args.parse_args()
    print(parsed_args.config, parsed_args.dataasource)