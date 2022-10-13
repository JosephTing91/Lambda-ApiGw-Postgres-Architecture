variable "privsubnet3_id"{
}
variable "privsubnet4_id"{
}

variable "dbsg_id"{
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


