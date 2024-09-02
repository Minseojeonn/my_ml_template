#import
import mlflow
import torch 
import dotmap

#from
from fire import Fire
from parser import parsing
from utils import set_random_seed



def main():
    args_enviroments = dotmap.DotMap(vars(parsing()))
    #set env parameters
   
    # Set MLflow
    if args_enviroments.use_mlflow:
        remote_server_uri = "http://localhost:5000"
        mlflow.set_tracking_uri(remote_server_uri)
        experiment_name = f"exper_name"
        mlflow.set_experiment(experiment_name)
        mlflow.start_run()

    # Step 0. Initialization
    args_enviroments.device = args_enviroments.device if torch.cuda.is_available() else 'cpu'
    set_random_seed(seed=args_enviroments.seed, device=args_enviroments.device)


    # Step 1. Preprocessing the dataset



if __name__ == "__main__":
    Fire(main)