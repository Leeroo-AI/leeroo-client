import requests
from typing import Dict

class LeerooClient:
    def __init__(self, api_key: str, local_host=False):
        """
        Initialize the Leeroo client for workflow management.

        Args:
            user_id (str): The unique identifier for the user.
            api_key (str): The API key for authentication and authorization with Leeroo's services.
        """
        self.url = "https://api.leeroo.com"
        if local_host:
            self.url = "http://local_host:8000"
        self.api_key = api_key
        self._authenticate()
    
    def _authenticate(self):
        url = f"{self.url}/authenticate/"
        data = {
            "api_key": self.api_key,
        }
        response = requests.post(url, data=data)
        # print(response)
        response = response.json()
        user_id = response.get('user_id')
        if user_id:
            self.user_id = user_id
            print(f"User: {self.user_id} Logged in!")
        else:
            raise "Incorrect API key"
        
    def initialize_workflow_configs(self,
        evaluation_description : str,
        workflow_name : str,
        seed_data_path : str,
        budget : int = 2,
    ):
        """
        Initializes a workflow by analyzing the provided task and generating a Directed Acyclic Graph (DAG) of experiments.
        The DAG is created based on the task description, the number of seed data points, and the allocated budget.
        Each node in the DAG represents a distinct experiment.

        The workflow can encompass various stages, including but not limited to:
        - Synthetic dataset generation
        - Evaluation system setup
        - Fine-tuning procedures (e.g., Supervised Fine-Tuning (SFT), Direct Preference Optimization (DPO))
        - Model evaluation
        - Best model selection

        Args:
            evaluation_description (str): A brief description of the task the model is intended to perform.
            workflow_name (str): A unique identifier for the workflow, facilitating easy identification.
            seed_data_path (str): Path to the seed dataset, which can be an example dataset or a full training dataset.
                Defaults to "eval_config.json".The seed data should be in the following json format:
                your_seed_dataset.json
                [
                    {
                        "query": str, 
                        "response": str
                    },
                    ...
                ]
            budget (int, optional): The maximum budget allocated for this workflow, specified in USD. Defaults to 1000.

        Returns:
            dict: A dictionary containing configurations for all the experiments within the workflow. These configurations
                can be modified as required. Users with domain expertise can modify the necessary parameters of output configs as needed.
        """

        url = f"{self.url}/initialize_workflow_configs/"
        data = {
            "user_id": self.user_id,
            "api_key": self.api_key,
            "task_description": evaluation_description,
            "workflow_name":workflow_name,
            "budget": budget,            
        }
        if seed_data_path:
            with open(seed_data_path, "rb") as file:
                # multipart/form-data
                files = {
                    "seed_data": (seed_data_path, file, "application/octet-stream")
                }
                response = requests.post(url, data=data, files=files)
        else:
            data['seed_data'] = None
            response = requests.post(url, data=data)
        
        workflow_configs = response.json()
        print(response)
        return workflow_configs

    def submit_workflow(self,
        workflow_configs : Dict
    ):
        """
        Submit the workflow for execution.
        This method submits the Directed Acyclic Graph (DAG) of experiments for execution on Leeroo servers.
        Each node in the DAG will be executed sequentially or in parallel as defined.
        Ensure that you have sufficient balance to cover the execution costs.

        Args:
            workflow_configs (dict): The configuration dictionary output from `initialize_workflow_configs`. 
                Domain experts may edit this configuration as needed.

        Returns:
            dict: Contains useful metadata for the submitted job, including the `workflow_running_state_id` which 
                can be used to track the execution status.
        """

        url = f"{self.url}/submit_workflow/"
        workflow_configs["user_id"] = self.user_id
        workflow_configs["api_key"] = self.api_key
        response = requests.post(url, json=workflow_configs)
        running_workflow_status = response.json()
        print(response)
        return running_workflow_status
    
    def all_workflows(self):
        """
        Retrieve all workflows associated with the user.

        Returns:
            dict: A dictionary containing details about the user's running and completed workflows.
        """
        url = f"{self.url}/get_user_workflows/"
        response = requests.post(url, json={"user_id":self.user_id,
            "api_key":self.api_key})
        print(response)
        return response.json()

    def get_workflow_status(self,
        workflow_runnning_state_id : str,
        print_workflow=True
    ):
        """
        Retrieve the status of an workflow.

        Args:
            workflow_running_state_id (str): The unique identifier for the running workflow.
                This ID is provided upon submission of the workflow via `submit_workflow`.

        Returns:
            dict: A dictionary containing detailed metadata about the current status of the workflow.
        """

        url = f"{self.url}/get_workflow_status/"
        response = requests.post(url, json={"user_id":self.user_id ,
            "workflow_runnning_state_id": workflow_runnning_state_id,
            "api_key":self.api_key})
        print(response)
        response = response.json()
        if response and print_workflow:
            for k,v in response.get('workflow_node_status',{}).items():
                print(k,":",v.replace("Executed", '\033[92mExecuted\033[0m').replace("running", '\033[94mrunning\033[0m'))
                
        # response = response
        # response = response.replace("running", '\033[94mrunning\033[0m')
        return response
    
    def deploy_workflow(self,
        workflow_runnning_state_id : str
    ):
        """
        Deploy the workflow.

        Args:
            workflow_running_state_id (str): The unique identifier for the running workflow.
                This ID is provided upon submission of the workflow via `submit_workflow`.

        Returns:
            dict: A dictionary containing detailed metadata about the deployment status of the workflow.
        """
        url = f"{self.url}/deploy_workflow/"
        response = requests.post(url, json={
            "workflow_runnning_state_id": workflow_runnning_state_id,
            "api_key":self.api_key})
        print(response)
        return response.json()

    def get_workflow_deployment_status(self,
        cluster_name : str
    ):
        """
        Retrieve the status of the deployed workflow.

        Args:
            cluster_name (str): The unique identifier for the deployed workflow.
                This ID is provided upon deployment of the workflow via `deploy_workflow`.

        Returns:
            dict: A dictionary containing detailed metadata about the deployment status of the workflow.
        """
        url = f"{self.url}/check_deployment_status/"
        response = requests.post(url, json={
            "cluster_name": cluster_name,
            "api_key":self.api_key})
        print(response)
        return response.json()

    def kill_deployment(self,
        cluster_name : str
    ):
        """
        Terminate the deployed workflow.

        Args:
            cluster_name (str): The unique identifier for the deployed workflow.
                This ID is provided upon deployment of the workflow via `deploy_workflow`.

        Returns:
            dict: A dictionary containing detailed metadata about the deployment status of the workflow.
        """
        url = f"{self.url}/kill_deployment/"
        response = requests.post(url, json={
            "cluster_name": cluster_name,
            "api_key":self.api_key})
        print(response)
        return response.json()
    
    def print_workflow(self,
        workflow_runnning_state_id : str
    ):
        """
        Print the workflow.

        Args:
            workflow_running_state_id (str): The unique identifier for the running workflow.
                This ID is provided upon submission of the workflow via `submit_workflow`.

        Returns:
            dict: A dictionary containing detailed metadata about the deployment status of the workflow.
        """
        url = f"{self.url}/print_workflow/"
        response = requests.post(url, json={
            "workflow_runnning_state_id": workflow_runnning_state_id,
            "api_key":self.api_key})
        print(response)
        return response.json()
    
    def kill_workflow(self, 
        workflow_runnning_state_id : str
    ):
        """
        Kill the workflow.

        Args:
            workflow_running_state_id (str): The unique identifier for the running workflow.
                This ID is provided upon submission of the workflow via `submit_workflow`.

        Returns:
            dict: A dictionary containing detailed metadata about the deployment status of the workflow.
        """
        url = f"{self.url}/kill_workflow/"
        response = requests.post(url, json={
            "workflow_runnning_state_id": workflow_runnning_state_id,
            "api_key":self.api_key})
        print(response)
        return response.json()
