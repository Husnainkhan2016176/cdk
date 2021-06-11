from aws_cdk import (
    core as cdk,
    aws_ecr as ecr,
    aws_codebuild as codebuild
)

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core


class MyCdkStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        # ecrrepo= ecr.Repository(self, "ecrrepo", repository_name="grocer-api-ecr-prod")
        # core.CfnOutput(self, "ecrreponame",value=ecrrepo.repository_name)

        git_hub_source = codebuild.Source.git_hub(
        owner="Husnainkhan2016176",
        repo="customimage",
        branch_or_ref="main",
        clone_depth=1

)

        cb=codebuild.Project(
        self,
        "codebuildproject",
        project_name="cd-proj",
        source=git_hub_source,

        environment={
        "privileged": True
        },
        build_spec=codebuild.BuildSpec.from_source_filename('buildspec.yml')
        )


        
