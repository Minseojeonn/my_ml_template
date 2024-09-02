import argparse

# Parsing arguments
def parsing(): 
    parser = argparse.ArgumentParser(description='Python parser usage.')
    parser.add_argument('--device', default="cuda:0", type=str, help='device')
    parser.add_argument('--seed', default=0, type=int, help='seed')
    parser.add_argument('--use_mlflow', default=False, type=bool, help='use_mlflow')
    args = parser.parse_args()
    return args