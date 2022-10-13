# terraform plan --var-file=variables/test.tfvars

module "iam" {
  source   = "../Modules/iam"
  ec2_role = var.ec2_role
}

module "vpc" {
  source       = "../Modules/vpc"
  vpc_name_tag = var.vpc_name_tag
  cidr_blocks  = var.cidr_blocks
}

module "sgs" {
  source       = "../Modules/sgs"
  vpc_id  = module.vpc.vpc_id
  db_port=var.db_port
  cidr_blocks  = var.cidr_blocks
}

module "lambda" {
  source = "../Modules/lambda"
  privsubnet1_id=module.vpc.privsubnet1_id
  privsubnet2_id=module.vpc.privsubnet2_id
  secret_kms_keyArn=module.db.secret_kms_keyArn
  db_pass_arn=module.db.db_pass_arn
  db_user_arn=module.db.db_user_arn
  db_endpoint_arn=module.db.db_endpoint_arn
  # sg_id_default=module.sgs.sg_id_default
  sg_id_lambda=module.sgs.sg_id_lambda 
  ssm_kms_arn=var.ssm_kms_arn
  lambda_runtime=var.lambda_runtime
}





module "apigw" {
  source          = "../Modules/apigw"
  app_lambda_uri  = module.lambda.app_lambda_uri
  app_lambda_name = module.lambda.app_lambda_name
}


module "db" {
 source="../Modules/db"
 db_username=var.db_username
 db_password=var.db_password
 db_instance_class=var.db_instance_class
 db_storage_min=var.db_storage_min
 db_storage_max=var.db_storage_max
 dbsg_id=module.sgs.dbsg_id
 log_retention=var.log_retention
 db_engine=var.db_engine
 db_engine_version=var.db_engine_version
 privsubnet3_id= module.vpc.privsubnet3_id
 privsubnet4_id= module.vpc.privsubnet4_id  
}



