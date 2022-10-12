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
  # sg_id_default=module.sgs.sg_id_default
  sg_id_lambda=module.sgs.sg_id_lambda 
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
 dbsg_id=module.sgs.dbsg_id
 privsubnet3_id= module.vpc.privsubnet3_id
 privsubnet4_id= module.vpc.privsubnet4_id  
}




