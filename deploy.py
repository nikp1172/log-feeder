import argparse
import logging

from servicefoundry import Build, PythonBuild, Resources, Service

logging.basicConfig(level=logging.INFO)

# parsing the input arguments
parser = argparse.ArgumentParser()
parser.add_argument(
    "--workspace_fqn",
    type=str,
    required=True,
    help="fqn of workspace where you want to deploy",
)
args = parser.parse_args()

# creating a service object and defining all the configurations
service = Service(
    name="log-feeder-np",
    image=Build(
        build_spec=PythonBuild(
            command="python main.py",
            python_version="3.9",
        ),
    ),
    ports=[{"port": 4000}],
    resources=Resources(
        cpu_request=0.5, cpu_limit=1.5, memory_limit=2500, memory_request=1500
    ),
)
service.deploy(workspace_fqn=args.workspace_fqn)
