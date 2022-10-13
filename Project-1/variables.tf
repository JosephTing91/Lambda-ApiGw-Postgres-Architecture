variable "vpc_name_tag" {}
variable "cidr_blocks" {}
variable "own_ip" {}
variable "instance_type" {}
variable "db_port" {}
variable "ec2_role" {}
variable "key_name" {
  type = string
}
variable "sm_kms_arn"{
  
}
variable "db_storage_min"{
}
variable "db_storage_max"{
}

variable "db_instance_class"{
}
variable "log_retention"{
}
variable "db_engine"{
}
variable "db_engine_version"{
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

