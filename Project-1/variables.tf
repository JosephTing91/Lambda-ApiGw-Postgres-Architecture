variable "vpc_name_tag" {}
variable "cidr_blocks" {}
variable "own_ip" {}
variable "instance_type" {}
variable "ec2_role" {}
variable "key_name" {
  type = string
}

variable "lambda_runtime" {
  type= string

}


variable "region" {
  type = string
}

variable "db_username"{
  description = "Database administrator username"
  type        = string
  sensitive   = true
}

variable "db_password"{
  description = "Database administrator password"
  type        = string
  sensitive   = true
}

